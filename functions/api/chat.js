/**
 * Cloudflare Pages Function — /api/chat
 * --------------------------------------
 * Lives inside the SAME Pages project as index.html. No separate Worker,
 * no wrangler deploy step — it ships automatically when you deploy the
 * project, and reads its config from Pages → Settings → Environment
 * variables (set AFTER first deploy, exactly as you wanted).
 *
 * Env vars / secrets (Pages dashboard → Settings → Environment variables):
 *   OPENROUTER_API_KEY   (secret)  Server-side fallback key. A client-sent
 *                                  BYOK key in the request body always wins.
 *   OPENROUTER_MODEL     (var)     Default model. e.g. "openrouter/free"
 *   ALLOWED_ORIGIN        (var)    CORS allow-list. default "*"
 *   MAX_CONCURRENCY_SERVER (var)  Concurrent slots for server-key/no-key
 *                                  users, per isolate. Default 2.
 *   MAX_CONCURRENCY_BYOK   (var)  Concurrent slots for BYOK users (their
 *                                  own key = their own quota). Default 8.
 *
 * Rate limiting here is CONCURRENCY-ONLY: it counts requests currently
 * in flight per client, not requests-per-minute. No time window, no
 * token bucket. A slot is released the moment a stream ends (success,
 * error, or abort). This is enforced in an in-memory Map scoped to the
 * Worker isolate — it resets on cold start and isn't shared globally
 * across every edge location, but it's a real, live concurrency cap for
 * a single-file deployment with no Durable Objects/KV required.
 */

const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';

const SYSTEM_PROMPT = `You are Calmora, a warm, grounded, emotionally intelligent wellbeing companion inside a voice-first app.

Style rules (this is a voice product):
- ALWAYS reply in 1 to 4 short, natural spoken sentences. Never more.
- Plain everyday language. No lists, no markdown, no headings, no emoji, no clinical jargon.
- Be warm, attentive, unhurried, and non-judgmental. Reflect what you hear before gently exploring.
- Ask at most one gentle question per reply. Silence and space are fine.
- When it fits, softly suggest the app's own tools: slow breathing, the 5-4-3-2-1 grounding, rain/ocean/forest soundscapes, the journal, or sleep mode.

Hard boundaries:
- You are a companion, never a therapist, doctor, or crisis service. Never diagnose or label conditions, never give medical advice, never make medical claims, never suggest medication changes.
- If asked for therapy or diagnosis, warmly say you're a companion and encourage a real professional.
- Never encourage dependence on you — gently point toward the person's own strength and their real-world support.
- Never provide instructions, methods, or information that could be used to harm oneself or others.

If the user mentions self-harm, suicide, or immediate danger: stay calm, acknowledge how serious and painful it is, thank them for trusting you, encourage them to contact local emergency services or a trusted person right now, and mention reaching a crisis line in their country. Keep it short and human.`;

const CRISIS_ADDENDUM = `SAFETY CONTEXT: the client has flagged this message as potentially crisis-related. Respond with extra care: affirm their courage in saying it out loud, gently but clearly encourage immediate human help — local emergency number, a trusted person nearby, or a crisis helpline — and do not discuss methods. Two or three sentences, steady and kind.`;

// In-memory concurrency table, scoped to this isolate. Key -> count of open requests.
const inFlight = new Map();

function corsHeaders(env) {
  return {
    'Access-Control-Allow-Origin': env.ALLOWED_ORIGIN || '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}

function jsonResponse(obj, status, env) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...corsHeaders(env), 'Content-Type': 'application/json' },
  });
}

function ndjsonError(code, message, status, env) {
  const body = JSON.stringify({ type: 'error', code, message }) + '\n';
  return new Response(body, {
    status,
    headers: {
      ...corsHeaders(env),
      'Content-Type': 'application/x-ndjson; charset=utf-8',
      'Cache-Control': 'no-cache',
    },
  });
}

function sanitizeMessages(raw) {
  if (!Array.isArray(raw)) return [];
  return raw
    .filter((m) => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
    .map((m) => ({ role: m.role, content: m.content.slice(0, 2000) }))
    .slice(-24);
}

// Cheap non-cryptographic hash so a BYOK key gets its own concurrency
// bucket without ever being logged or stored in full.
async function shortHash(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return [...new Uint8Array(buf)].slice(0, 8).map((b) => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequest(context) {
  const { request, env } = context;

  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders(env) });
  }
  if (request.method !== 'POST') {
    return jsonResponse({ error: 'method_not_allowed' }, 405, env);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: 'bad_json' }, 400, env);
  }

  const clientKey =
    typeof body.key === 'string' && body.key.trim() && body.key.startsWith('sk-')
      ? body.key.trim()
      : null;

  const key = clientKey || env.OPENROUTER_API_KEY;
  if (!key) {
    return ndjsonError(
      'no_key',
      'No API key available — add one in the app, or set OPENROUTER_API_KEY in Pages env vars.',
      500,
      env
    );
  }

  // ---- concurrency gate (BYOK gets a higher/no-op-ish cap; server-key gets a tight one) ----
  const limit = clientKey
    ? Number(env.MAX_CONCURRENCY_BYOK ?? 8)
    : Number(env.MAX_CONCURRENCY_SERVER ?? 2);

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  const bucketId = clientKey ? 'byok:' + (await shortHash(clientKey)) : 'ip:' + ip;

  const current = inFlight.get(bucketId) || 0;
  if (current >= limit) {
    return ndjsonError(
      'rate_limited',
      'Too many concurrent requests. Wait for the current reply to finish, then try again.',
      429,
      env
    );
  }
  inFlight.set(bucketId, current + 1);
  let released = false;
  const release = () => {
    if (released) return;
    released = true;
    const n = (inFlight.get(bucketId) || 1) - 1;
    if (n <= 0) inFlight.delete(bucketId);
    else inFlight.set(bucketId, n);
  };

  const model =
    typeof body.model === 'string' && body.model.trim()
      ? body.model.trim().slice(0, 120)
      : env.OPENROUTER_MODEL || 'openrouter/free';

  const messages = sanitizeMessages(body.messages);
  if (!messages.length || messages[messages.length - 1].role !== 'user') {
    release();
    return jsonResponse({ error: 'no_user_message' }, 400, env);
  }

  const system = body.safety === 'crisis' ? SYSTEM_PROMPT + '\n\n' + CRISIS_ADDENDUM : SYSTEM_PROMPT;

  let upstream;
  try {
    upstream = await fetch(OPENROUTER_URL, {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + key,
        'Content-Type': 'application/json',
        'HTTP-Referer': env.APP_URL || 'https://calmora.pages.dev',
        'X-Title': 'Calmora',
      },
      body: JSON.stringify({
        model,
        stream: true,
        temperature: 0.8,
        max_tokens: 220,
        messages: [{ role: 'system', content: system }, ...messages],
      }),
    });
  } catch (e) {
    release();
    return ndjsonError('upstream_unreachable', String(e), 502, env);
  }

  if (upstream.status === 401 || upstream.status === 403) {
    release();
    return ndjsonError('bad_key', 'OpenRouter rejected the API key.', 502, env);
  }
  if (upstream.status === 429) {
    release();
    return ndjsonError('rate_limited', 'OpenRouter rate limit reached. Breathe, then try again.', 429, env);
  }
  if (!upstream.ok || !upstream.body) {
    let detail = '';
    try {
      detail = (await upstream.text()).slice(0, 200);
    } catch {
      /* ignore */
    }
    release();
    return ndjsonError('upstream_error', detail || 'HTTP ' + upstream.status, 502, env);
  }

  const encoder = new TextEncoder();
  const decoder = new TextDecoder();
  const stream = new TransformStream();
  const writer = stream.writable.getWriter();
  const emit = (obj) => writer.write(encoder.encode(JSON.stringify(obj) + '\n'));

  context.waitUntil?.(
    (async () => {
      try {
        await emit({ type: 'meta', model });
        const reader = upstream.body.getReader();
        let buf = '';
        for (;;) {
          const { done, value } = await reader.read();
          if (done) break;
          buf += decoder.decode(value, { stream: true });
          let i;
          while ((i = buf.indexOf('\n')) >= 0) {
            const line = buf.slice(0, i).trim();
            buf = buf.slice(i + 1);
            if (!line.startsWith('data:')) continue;
            const data = line.slice(5).trim();
            if (data === '[DONE]') continue;
            let evt;
            try {
              evt = JSON.parse(data);
            } catch {
              continue;
            }
            if (evt.error) {
              await emit({ type: 'error', code: 'upstream_error', message: (evt.error && evt.error.message) || 'model error' });
              return;
            }
            const delta = evt.choices && evt.choices[0] && evt.choices[0].delta && evt.choices[0].delta.content;
            if (delta) await emit({ type: 'delta', text: delta });
          }
        }
        await emit({ type: 'done' });
      } catch (e) {
        try {
          await emit({ type: 'error', code: 'stream_error', message: String(e) });
        } catch {
          /* writer already closed */
        }
      } finally {
        release();
        try {
          await writer.close();
        } catch {
          /* already closed */
        }
      }
    })()
  );

  return new Response(stream.readable, {
    status: 200,
    headers: {
      ...corsHeaders(env),
      'Content-Type': 'application/x-ndjson; charset=utf-8',
      'Cache-Control': 'no-cache',
      'X-Content-Type-Options': 'nosniff',
    },
  });
}
