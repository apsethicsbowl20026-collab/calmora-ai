/* Calmora service worker — makes the app installable and works offline.
   Strategy: cache the app shell; always hit the network for /api/* (the AI);
   network-first for page navigations with a cached fallback. */
const CACHE = 'calmora-v1';
const SHELL = ['/', '/index.html', '/manifest.webmanifest', '/icon.svg'];

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await Promise.all(SHELL.map((u) => c.add(u).catch(() => {})));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.indexOf('/api/') === 0) return; // never cache the AI server

  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      try {
        const r = await fetch(req);
        const cp = r.clone();
        const c = await caches.open(CACHE);
        c.put('/index.html', cp);
        return r;
      } catch (err) {
        const m = await caches.match('/index.html');
        return m || caches.match('/');
      }
    })());
    return;
  }

  e.respondWith((async () => {
    const m = await caches.match(req);
    if (m) return m;
    try {
      const r = await fetch(req);
      if (r && r.ok) {
        const cp = r.clone();
        const c = await caches.open(CACHE);
        c.put(req, cp);
      }
      return r;
    } catch (err) {
      return m;
    }
  })());
});
