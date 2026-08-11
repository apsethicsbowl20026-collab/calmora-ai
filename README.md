# CALMORA — Cloudflare Pages deploy

Everything lives in one Pages project:

```
index.html            → the entire app (HTML/CSS/JS, no build step)
functions/api/chat.js  → Pages Function, proxies to OpenRouter + rate limiting
```

No Worker, no wrangler, no build. Deploy this folder as-is.

## Deploy

1. Push this folder to a GitHub repo (or drag-and-drop the folder in the dashboard).
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** (or "Upload assets" for drag-and-drop).
   - Build command: *(none)*
   - Build output directory: `/`
3. Deploy. You'll get `https://<project>.pages.dev`.

## Set env vars AFTER deploy

**Workers & Pages → your project → Settings → Environment variables → Production**

| Name | Type | Required | Default | Notes |
|---|---|---|---|---|
| `OPENROUTER_API_KEY` | **Secret** | optional | — | Server-side fallback key. Any user-supplied BYOK key in the app always overrides this. Leave unset to force BYOK-only. |
| `OPENROUTER_MODEL` | var | optional | `openrouter/free` | Default model id. |
| `ALLOWED_ORIGIN` | var | optional | `*` | Lock to your `pages.dev` / custom domain in production. |
| `APP_URL` | var | optional | `https://calmora.pages.dev` | Sent as `HTTP-Referer` to OpenRouter. |
| `MAX_CONCURRENCY_SERVER` | var | optional | `2` | Max concurrent in-flight requests per IP for users **without** a BYOK key (i.e. using your server key). |
| `MAX_CONCURRENCY_BYOK` | var | optional | `8` | Max concurrent in-flight requests per BYOK key. Higher because it's their own OpenRouter quota, not yours. |

After setting/changing vars, click **Retry deployment** (or trigger a redeploy) — Pages Functions env vars apply at deploy time.

## How the rate limit works

Concurrency-only, no time window, no token bucket:
- Every request in flight occupies one "slot" for its client bucket.
- BYOK users get their own bucket (keyed by a hash of their key, key itself never stored/logged).
- Non-BYOK users share a bucket per IP, using your `OPENROUTER_API_KEY`.
- A slot is released the instant the stream ends — success, error, or client abort.
- Over the limit → immediate `429 rate_limited`, no queueing.

This is enforced in-memory per Worker isolate. It resets on cold start and isn't a hard global guarantee across every edge PoP simultaneously — for a single-file, no-database deployment this is the practical ceiling. If you later need a hard global concurrency cap, that requires a Durable Object, which means moving off "index.html does everything."

## BYOK vs server key

- **BYOK (recommended):** user pastes their own OpenRouter key in Settings. Sent to `/api/chat` per-request, never stored server-side, gets the higher `MAX_CONCURRENCY_BYOK` cap.
- **Server key:** if you set `OPENROUTER_API_KEY`, users with no key configured fall back to it, capped at `MAX_CONCURRENCY_SERVER`.
- **Neither:** app runs in local/offline companion mode — no network call at all.

## Free OpenRouter models

Model id is set in Settings → AI → Model, or via `OPENROUTER_MODEL`. OpenRouter's free-tier model lineup changes over time — check [openrouter.ai/models?max_price=0](https://openrouter.ai/models?max_price=0) for current options and swap the id any time; no redeploy needed for per-user changes.
