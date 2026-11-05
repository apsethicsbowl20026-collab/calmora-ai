/**
 * Cloudflare Pages Function — /api/search
 * Server-side Tavily proxy for the `web_search` agent tool.
 * Keeps TAVILY_API_KEY off the browser and returns only sanitized results.
 */

const TAVILY_URL = 'https://api.tavily.com/search';
const MAX_QUERY = 400;
const DEFAULT_RESULTS = 5;
const MAX_RESULTS = 6;
const inFlight = new Map();

function corsHeaders(env) {
  return {
    'Access-Control-Allow-Origin': env.ALLOWED_ORIGIN || '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
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

function clampResults(value) {
  const n = Number(value);
  if (!Number.isFinite(n)) return DEFAULT_RESULTS;
  return Math.max(1, Math.min(MAX_RESULTS, Math.round(n)));
}

function cleanText(value, max) {
  return String(value || '').replace(/\s+/g, ' ').trim().slice(0, max);
}

function safeUrl(value) {
  try {
    const url = new URL(String(value || ''));
    return url.protocol === 'http:' || url.protocol === 'https:' ? url.toString() : null;
  } catch {
    return null;
  }
}

async function withTimeout(promise, ms) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), ms);
  try {
    return await promise(controller.signal);
  } finally {
    clearTimeout(timer);
  }
}

export async function onRequest(context) {
  const { request, env } = context;

  if (request.method === 'GET') {
    return jsonResponse({ service: 'calmora-search', configured: !!env.TAVILY_API_KEY }, 200, env);
  }
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders(env) });
  }
  if (request.method !== 'POST') {
    return jsonResponse({ error: 'method_not_allowed' }, 405, env);
  }
  if (!env.TAVILY_API_KEY) {
    return jsonResponse({ error: 'search_not_configured', message: 'Web search is not configured on this deployment.' }, 503, env);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: 'bad_json' }, 400, env);
  }

  const query = cleanText(body.query, MAX_QUERY);
  if (!query) return jsonResponse({ error: 'missing_query' }, 400, env);

  const topic = body.topic === 'news' ? 'news' : 'general';
  const timeRange = ['day', 'week', 'month', 'year'].includes(body.time_range) ? body.time_range : undefined;
  const maxResults = clampResults(body.max_results);

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  const bucket = 'search:' + ip;
  const current = inFlight.get(bucket) || 0;
  if (current >= 4) {
    return jsonResponse({ error: 'rate_limited', message: 'Too many searches at once. Try again in a moment.' }, 429, env);
  }
  inFlight.set(bucket, current + 1);
  const release = () => {
    const next = (inFlight.get(bucket) || 1) - 1;
    if (next <= 0) inFlight.delete(bucket);
    else inFlight.set(bucket, next);
  };

  try {
    const upstream = await withTimeout((signal) => fetch(TAVILY_URL, {
      method: 'POST',
      signal,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + env.TAVILY_API_KEY,
      },
      body: JSON.stringify({
        query,
        topic,
        ...(timeRange ? { time_range: timeRange } : {}),
        search_depth: 'basic',
        max_results: maxResults,
        include_answer: false,
        include_raw_content: false,
        include_images: false,
        safe_search: topic === 'general',
      }),
    }), 9000);

    if (!upstream.ok) {
      let detail = '';
      try { detail = cleanText(await upstream.text(), 180); } catch { /* ignore */ }
      const code = upstream.status === 401 || upstream.status === 403
        ? 'search_key_rejected'
        : upstream.status === 429
          ? 'rate_limited'
          : 'search_error';
      return jsonResponse({ error: code, message: detail || 'Search request failed.' }, upstream.status === 429 ? 429 : 502, env);
    }

    const data = await upstream.json();
    const results = Array.isArray(data.results) ? data.results.slice(0, maxResults).map((item) => ({
      title: cleanText(item.title, 140) || 'Source',
      url: safeUrl(item.url),
      content: cleanText(item.content, 360),
      published_date: cleanText(item.published_date, 60) || null,
    })).filter((item) => item.url) : [];

    return jsonResponse({ results, provider: 'tavily' }, 200, env);
  } catch (error) {
    const aborted = error && error.name === 'AbortError';
    return jsonResponse({ error: aborted ? 'search_timeout' : 'search_unreachable', message: aborted ? 'Search took too long.' : String(error) }, 502, env);
  } finally {
    release();
  }
}
