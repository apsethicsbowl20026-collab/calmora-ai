import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { JSDOM, VirtualConsole } from 'jsdom';
const html = await readFile(new URL('../index.html', import.meta.url), 'utf8');
function workspace({ recognition = false, streaming = false, direct = false, savedTheme, systemDark = false } = {}) {
  const errors = [];
  const console = new VirtualConsole();
  console.on('jsdomError', error => errors.push(error.message));
  const dom = new JSDOM(html, {
    url: 'https://calmora.test', runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: console,
    beforeParse(w) {
      w.requests=[];w.requestUrls=[];w.utterances=[];w.TextDecoder=TextDecoder;
      if(direct)w.localStorage.setItem('calmora:settings',JSON.stringify({apiKey:'sk-test-key'}));
      w.fetch = async (url, options) => {
        if(streaming&&options?.method==='POST'){
          w.requests.push(JSON.parse(options.body));w.requestUrls.push(url);
          if(direct)return new Response('data: '+JSON.stringify({choices:[{delta:{content:'Take your time. I am here.'}}]})+'\n\ndata: [DONE]\n\n');
          return new Response(JSON.stringify({type:'delta',text:'Take your time. I am here.'})+'\n'+JSON.stringify({type:'done'})+'\n');
        }
        return { ok: false, status: 503, json: async () => ({}), text: async () => '' };
      };
      if(savedTheme)w.localStorage.setItem('calmora:theme',savedTheme);
      let mediaListener;
      const media={matches:systemDark,addEventListener(type,fn){mediaListener=fn}};
      w.changeSystemTheme=function(dark){media.matches=dark;mediaListener?.()};
      w.matchMedia = query => query.includes('prefers-color-scheme')?media:{matches:false,addEventListener(){}};
      w.AbortController = AbortController;
      if (recognition) w.SpeechRecognition = class {
        start() { w.lastRecognizer = this; }
        stop() { this.onend?.(); }
      };
      w.SpeechSynthesisUtterance = function(text) { this.text = text; };
      w.speechSynthesis = { getVoices: () => [], speak(u) { if(u.volume!==0)w.utterances.push(u); }, cancel() {}, resume() {} };
    },
  });
  return { dom, w: dom.window, d: dom.window.document, errors };
}
test('workspace boots, controls share settings, dialogs and mood data work', async () => {
  const { dom, w, d, errors } = workspace();
  try {
    assert.deepEqual(errors, []);
    assert.equal(d.querySelector('#sidebar-nav #dock').children.length, 5);
    d.querySelector('#session-auto').click();
    assert.equal(d.querySelector('#session-auto').getAttribute('aria-pressed'), 'false');
    assert.equal(JSON.parse(w.localStorage.getItem('calmora:settings')).auto, false);
    d.querySelector('[data-mood="Good"]').click();
    const moods = JSON.parse(w.localStorage.getItem('calmora:moods'));
    assert.equal(moods[0].level, 4);
    assert.deepEqual(moods[0].tags, []);
    d.querySelector('#workspace-settings').click();
    assert.equal(d.querySelector('#sheet-settings').hidden, false);
    d.querySelector('[data-open="breathe"]').click();
    assert.equal(d.querySelector('#sheet-breathe').hidden, false);
    assert.deepEqual(errors, []);
  } finally { await new Promise(resolve => setTimeout(resolve, 50)); dom.window.close(); }
});
test('unsupported speech input falls back to the text field', async () => {
  const { dom, w, d, errors } = workspace();
  try {
    // Speech recognition is intentionally unavailable in this environment.
    d.querySelector('#talk-cta').click();
    assert.equal(d.activeElement.id, 'input-text');
    assert.match(d.querySelector('#toast-region').textContent, /Voice input needs/);
    assert.deepEqual(errors, []);
  } finally { await new Promise(resolve => setTimeout(resolve, 50)); dom.window.close(); }
});
test('listening can end explicitly and stale recognizers cannot replace a new session', async () => {
  const { dom, w, d, errors } = workspace({ recognition: true });
  try {
    d.querySelector('#talk-cta').click();
    assert.ok(d.body.classList.contains('state-listening'));
    const old = w.lastRecognizer;
    const oldResult=old.onresult,oldEnd=old.onend;
    d.querySelector('#session-end').click();
    assert.ok(d.body.classList.contains('state-idle'));
    assert.equal(d.querySelector('#session-end').hidden, true);
    d.querySelector('#talk-cta').click();
    assert.notEqual(w.lastRecognizer, old);
    oldResult({ resultIndex: 0, results: [Object.assign([{ transcript: 'stale words' }], { isFinal: true })] });
    oldEnd();
    assert.equal(d.querySelector('#input-text').value, '');
    assert.ok(d.body.classList.contains('state-listening'));
    d.querySelector('#session-end').click();
    assert.deepEqual(errors, []);
  } finally { await new Promise(resolve => setTimeout(resolve, 50)); dom.window.close(); }
});

test('call persists across silence, mute releases recognition, unmute reconnects and hangup cleans up', async () => {
  const { dom, w, d, errors } = workspace({ recognition: true });
  try {
    d.querySelector('#talk-cta').click();
    assert.equal(d.querySelector('#call-console').hidden, false);
    const first=w.lastRecognizer;
    first.onend();
    await new Promise(resolve => setTimeout(resolve, 400));
    assert.notEqual(w.lastRecognizer, first);
    assert.equal(d.querySelector('#call-console').hidden, false);
    d.querySelector('#call-mute').click();
    assert.equal(d.querySelector('#call-mute').getAttribute('aria-pressed'), 'true');
    assert.match(d.querySelector('#call-status-text').textContent, /muted/);
    const second=w.lastRecognizer;
    d.querySelector('#call-mute').click();
    assert.notEqual(w.lastRecognizer, second);
    d.querySelector('#call-hangup').click();
    assert.equal(d.querySelector('#call-console').hidden, true);
    assert.equal(d.body.classList.contains('in-call'), false);
    assert.ok(d.body.classList.contains('state-idle'));
    assert.deepEqual(errors, []);
  } finally { await new Promise(resolve => setTimeout(resolve, 50)); dom.window.close(); }
});
test('microphone denial ends the call and offers an actionable recovery', async () => {
  const { dom, w, d, errors } = workspace({ recognition: true });
  try {
    d.querySelector('#talk-cta').click();
    w.lastRecognizer.onerror({ error: 'not-allowed' });
    assert.equal(d.querySelector('#call-console').hidden, true);
    assert.match(d.querySelector('#toast-region').textContent, /permission denied/);
    assert.deepEqual(errors, []);
  } finally { await new Promise(resolve => setTimeout(resolve, 50)); dom.window.close(); }
});
test('no external speech provider or additional keyed integration remains', () => {
  assert.equal(html.includes('/api/speech'), false);
  assert.equal(html.includes('NATURAL'), false);
  assert.equal(html.includes('TTS_API_KEY'), false);
});

test('a spoken turn streams a reply, supports barge-in, and resumes without another call click', async () => {
  const { dom, w, d, errors } = workspace({ recognition: true, streaming: true });
  const result=(text,index=0,final=true)=>({resultIndex:index,results:Object.assign(Array(index).fill(null),{[index]:Object.assign([{transcript:text}],{isFinal:final})})});
  const wait=ms=>new Promise(resolve=>setTimeout(resolve,ms));
  try {
    d.querySelector('#talk-cta').click();
    const rec=w.lastRecognizer;
    rec.onresult(result('I have had a difficult day'));
    rec.onspeechend();await wait(900);
    assert.equal(w.requests.length,1);
    assert.equal(w.requests[0].messages.at(-1).content,'I have had a difficult day');
    assert.ok(w.utterances.length>0);
    w.utterances[0].onstart();
    assert.ok(d.body.classList.contains('state-speaking'));
    // Echo must not become a new user turn.
    rec.onresult(result('Take your time. I am here.',1));
    assert.ok(d.body.classList.contains('state-speaking'));
    // A distinct phrase interrupts, preserving the same call / recognizer.
    rec.onresult(result('Actually I want to talk about work',2));
    assert.ok(d.body.classList.contains('state-listening'));
    rec.onspeechend();await wait(900);
    assert.equal(w.requests.length,2);
    const audio=w.utterances.at(-1);audio.onstart();audio.onend();
    // Finish all remaining queued speech events (the browser normally does this).
    for(const utterance of w.utterances.slice(-2))utterance.onend?.();
    assert.equal(d.querySelector('#call-console').hidden,false);
    assert.equal(w.lastRecognizer,rec);
    d.querySelector('#call-hangup').click();
    assert.deepEqual(errors,[]);
  } finally { await wait(50);dom.window.close(); }
});

test('OpenRouter BYOK uses its streaming endpoint directly without an extra service', async () => {
  const { dom,w,d,errors }=workspace({recognition:true,streaming:true,direct:true});
  try {
    d.querySelector('#talk-cta').click();
    w.lastRecognizer.onresult({resultIndex:0,results:[Object.assign([{transcript:'Tell me something kind'}],{isFinal:true})]});
    w.lastRecognizer.onspeechend();
    await new Promise(resolve=>setTimeout(resolve,950));
    assert.equal(w.requests.length,1);
    assert.equal(w.requestUrls[0],'https://openrouter.ai/api/v1/chat/completions');
    assert.equal(w.requests[0].messages[0].role,'system');
    assert.equal(w.requests[0].tools.length,6);
    assert.ok(w.utterances.length);
    d.querySelector('#call-hangup').click();
    assert.deepEqual(errors,[]);
  } finally {await new Promise(resolve=>setTimeout(resolve,50));dom.window.close()}
});

test('first paint is dark even when the OS uses light mode', async () => {
  const {dom,d,errors}=workspace();
  try {
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(d.documentElement.dataset.theme,'dark');
    assert.equal(d.documentElement.style.colorScheme,'dark');
    assert.equal(d.querySelector('meta[name="theme-color"]').content,'#101816');
    assert.equal(d.querySelector('#theme-picker').value,'dark');
    assert.deepEqual(errors,[]);
  } finally {dom.window.close()}
});
test('appearance selectors synchronize and save an explicit preference', async () => {
  const {dom,d,w,errors}=workspace();
  try {
    await new Promise(resolve=>setTimeout(resolve,0));
    const picker=d.querySelector('#theme-picker');picker.value='light';picker.dispatchEvent(new w.Event('change'));
    assert.equal(d.documentElement.dataset.theme,'light');
    assert.equal(d.querySelector('#set-theme').value,'light');
    assert.equal(w.localStorage.getItem('calmora:theme'),'light');
    w.changeSystemTheme(true);
    assert.equal(d.documentElement.dataset.theme,'light','OS changes must not override an explicit choice');
    const setting=d.querySelector('#set-theme');setting.value='dark';setting.dispatchEvent(new w.Event('change'));
    assert.equal(picker.value,'dark');
    assert.equal(d.documentElement.dataset.theme,'dark');
    assert.deepEqual(errors,[]);
  } finally {dom.window.close()}
});
test('system preference tracks OS changes and a saved light choice restores before paint', async () => {
  const {dom,d,w}=workspace({savedTheme:'system',systemDark:true});
  try {
    assert.equal(d.documentElement.dataset.theme,'dark');
    w.changeSystemTheme(false);
    assert.equal(d.documentElement.dataset.theme,'light');
    w.CalmoraTheme.set('invalid');
    assert.equal(w.CalmoraTheme.get(),'system');
  } finally {dom.window.close()}
  const next=workspace({savedTheme:'light',systemDark:true});
  try{assert.equal(next.d.documentElement.dataset.theme,'light')}finally{next.dom.window.close()}
});
test('core Nightfall text color pairs meet WCAG AA normal-text contrast', () => {
  const luminance=hex=>{
    const channels=hex.match(/[a-f0-9]{2}/gi).map(v=>parseInt(v,16)/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4);
    return channels[0]*.2126+channels[1]*.7152+channels[2]*.0722;
  };
  const pairs=[['e2ece4','101816'],['afbeb1','202e20'],['afbeb1','293d28'],['b4c99f','19261e'],['172b1a','abc897'],['acbba1','101b14'],['c0cdb5','23301e']];
  for(const [fg,bg] of pairs){const a=luminance(fg),b=luminance(bg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);assert.ok(ratio>=4.5,`${fg} on ${bg}: ${ratio}`)}
});
