# CALMORA — 30″ LAUNCH FILM · Production Blueprint

**Product:** Calmora — a voice-first wellbeing companion that *listens, comforts, remembers — and acts.*
**Source of truth:** this repository (`github.com/apsethicsbowl20026-collab/calmora-ai`). Every claim in the film is drawn from shipped code, not marketing invention.
**Master:** `video/calmora-launch.html` — 1920×1080, 30.00s, 120 BPM, Canvas 2D, live Web Audio score, four VO clips.
**Companions:** `video/storyboard.png` (12 key frames), `video/audio/*.mp3` (VO), this document.

> **Play it:** serve the repo (`python3 -m http.server 8000`) and open `/video/calmora-launch.html`. Space = play, ←/→ = scrub, R = restart, M = mute. The player has chapter jumps, a scene dossier, PNG frame export, and real-time WebM recording with the score + VO baked in.

---

## 0. CORE BRAND PROFILE

### The ultimate hook — the "magic moment"
> **You speak one sentence — *"play some rain for me"* — and the room changes.**

The orb turns cyan as it listens, your words fill a live transcript, a tool call fires, rain actually starts playing through a live Web Audio engine, and Calmora tells you what it did. Nothing is downloaded. Nothing about you is uploaded. **It is the exact second a "chatbot" becomes an agent.** That transformation — *words → action, in your own voice, on your own device* — is the entire film.

The competitor set is a chat box. So the film opens on a chat box, kills it, and spends the next 20 seconds proving Calmora is a different category of thing.

**Positioning line:** *A quiet place to think out loud.*
**Launch tagline:** **Be gentle with yourself.** (already the closing line of the repo README)
**Promise ladder:** Voice → Understanding → Action → Privacy.

### The pain, precisely
Wellness apps are thin chat wrappers: they reply, they don't *do*. At 3:17 AM a person says "I can't switch off tonight" and gets "I hear you. That sounds hard." plus a typing indicator that never resolves into anything. **Zero actions taken.** That is the villain of the film — not anxiety itself, but the emptiness of a product that only talks.

### Premium high-contrast aesthetic — "MIDNIGHT CLINICAL"
A deliberate collision of two light temperatures, not generic "Apple blue":

| Role | Token | Hex | Use |
|---|---|---|---|
| Base / negative space | `--bg0` / app shell | `#070d0e`, `#05060f` | 85% of frame |
| Warm key light | `--amber` / `--amber-hi` | `#e9c08c` / `#f6ddb6` | Rim light on the orb, rules, tracked caps, CTA |
| Proof / truth accent | `--foam` | `#93d6c6` | "EXECUTED" states, privacy seal, waveforms |
| Cold glass | orb idle | `#3ea2ff` → `#1b4fae` → `#0a1f4a` | The hero object |
| State machine | listen / think / speak | `#38bdf8` / `#facc15` / `#fb923c` | Narrative beats |
| Disruption only | stress red | `#ff5a5a` | Hook act exclusively — never after 5s |

- **Contrast logic:** cold, near-black teal glass against a warm champagne-amber rim. The orb is the only saturated object allowed in Acts 02 and 04. Act 03 earns its color through UI proof, never decoration.
- **Type:** `Fraunces` (display serif, italic for the human line) / `Karla` (tracked UI caps) / `IBM Plex Mono` (code, tool calls, URL, timecode). Matches the app's real font stack.
- **Texture:** 5.5% film grain, soft vignette, volumetric smoke, drifting bokeh dust, anamorphic horizontal flares. Never a lens-flare preset pack, never a gradient-mesh corporate background.
- **Deliberately absent:** stock footage of breathing women on beaches, hands holding phones, smiling headsets, meditation clichés, "AI" sparkle particles, streaks/streak-shaming UI, medical claims, dashboard screenshots with fake numbers.

### Claims → evidence (so the film stays honest)

| On-screen claim | Repo evidence |
|---|---|
| `play_sound`, `start_breathing`, `note_thought` | `functions/api/chat.js` TOOLS array + `executeTool()` in `index.html` |
| 7 soundscapes, synthesised live | Web Audio engine in `index.html`; rain/ocean/forest/brown/fire/night/cave |
| Binaural · 7.83 Hz · Solfeggio 174–963 Hz | Frequency Lab in `index.html` |
| Live transcript, orb state colours | SpeechRecognition pipeline + `body.state-*` CSS in `index.html` |
| On your device / no account / export / erase | `localStorage` + You panel in `index.html` |
| Offline PWA · zero build | `sw.js`, `manifest.webmanifest`, single `index.html` |

⚠️ **Compliance:** Calmora is a wellbeing **companion**, not a medical device, therapist, or crisis service. The film makes no diagnostic, treatment, or outcome claims. Keep that constraint in every cut-down and localization.

---

## 1. VIDEO STRUCTURE & PACING

**120 BPM → 0.5s per beat → 60 beats / 15 bars in 30 seconds.** Every hard cut lands on a beat or half-bar. No dissolve, no crossfade anywhere except two deliberate 300ms copy fades.

| Act | Time | Beats | Job | Energy |
|---|---|---|---|---|
| **01 THE HOOK** | 0.00–5.00 | 0–10 | Disrupt / name the pain | Tense, staccato, 8 cuts, near-silence at the end |
| **02 THE REVEAL** | 5.00–15.00 | 10–30 | Hero object, magic moment setup | Impact → warm, expansive, one continuous dolly |
| **03 VALUE IN ACTION** | 15.00–25.00 | 30–50 | 3 proof pillars | Peak kinetic, 3 sub-cuts, rhythmic UI |
| **04 THE CTA** | 25.00–30.00 | 50–60 | Lock the brand, convert | Strip back to air → hard blackout |

**Hard cut list (s):** `0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 9.0, 11.5, 12.6, 13.2, 15.0, 15.5, 16.3, 17.1, 18.5, 19.0*, 19.4*, 19.8*, 20.2*, 20.6*, 21.0*, 22.0, 25.0, 28.86→fade, 29.5 blackout`  (*= chip entrances, not scene cuts).

**Conversion logic:** the first 5 seconds earn attention with a *category* insult, not a feature. Seconds 5–15 sell desire with one beautiful object. Seconds 15–25 remove risk with three concrete proofs (it *acts*, it *sounds*, it *stays yours*). The last 5 seconds give one action and one URL, then get out of the way. No feature list, no pricing, no "learn more".

---

## 2. VOICEOVER SCRIPT (measured, sparse, calm)

Deliberate anti-hype delivery: warm, low, unhurried, ~95 wpm. The calm voice against kinetic frames *is* the product demo. Mixed at −2 dB against a score bus ducked to 0.62, with 10% plate reverb.

| File | In → Out | Duration | Line |
|---|---|---|---|
| `audio/vo-hook.mp3` | 0.40 → 3.61 | 3.21s | "Another chat box. Nothing changes." |
| `audio/vo-reveal.mp3` | 5.35 → 14.04 | 8.69s | "This is Calmora. An orb that listens, and acts. A quiet place to think out loud." |
| `audio/vo-value.mp3` | 15.10 → 24.63 | 10.10s @ 1.06× | "Play rain. Breathe. Save the thought. Sound, made live. Yours, always." |
| `audio/vo-cta.mp3` | 25.40 → 28.76 | 3.36s | "Calmora. Be gentle with yourself." |

**VO-negative space:** 4.45–5.00 (500ms of dead air before the reveal impact), 3.61–5.00, 14.04–15.10, 24.63–25.40. Those gaps are the loudest part of the edit.

---

## 3. SCENE-BY-SCENE PROMPT BLUEPRINT

Each block below is a complete, paste-ready direction: **visual prompt / text overlays / camera / lighting & graphics / audio / asset directions**.

---

### ACT 01 — THE HOOK · `0.00–5.00s` · Problem / Disruption

**Intent:** In five seconds the viewer should feel the specific insult of a wellness chatbot. No product. No logo.

**VISUAL PROMPT (for an external renderer / live-action reshoot):**
> Ultra-close macro of a cold, sterile chat interface at 3:17 AM, shot on a probe lens at 100mm, 2×–4× magnification. A rounded dark-glass panel fills the frame. One user bubble reads "I can't switch off tonight." One assistant bubble reads "I hear you. That sounds hard." A third bubble shows a typing indicator with three dots that never resolves. A single perfectly flat white waveform line cuts horizontally through the centre of frame — dead, no signal. Eighteen small notification pills drift across the panel like debris. Harsh red chromatic aberration splits on every cut, subtle volumetric haze, faint grain, near-black background with a bruised red stress glow in the upper right. Photorealistic studio, moody, high contrast, no people, no hands, no phone bezel. 16:9, 24fps look, deep focus on glass texture.

**TEXT OVERLAYS (screen-locked, punching through the chaos):**
- `03:17` + `A WAKEFUL NIGHT` — top-left, mono, 0.0–4.45s
- `ANOTHER CHAT BOX.` — 56px bold tracked caps, 0.65–2.85s
- `ANOTHER "I HEAR YOU."` — 26px muted, 1.45–2.90s
- `NOTHING CHANGES.` — 88px heavy white with 26px bloom, 3.00–4.45s
- `WELLNESS, AS USUAL` — 18px amber tracked, 3.15–4.40s
- Diegetic proof chip: `0 ACTIONS TAKEN` with a red status dot
- `EVERYTHING IS NOISE.` — faint, 4.45–5.00s, fading out

**CAMERA:** Macro 1.42×→1.93× punch-ins on every beat, ±170px random pan, ±90px vertical jitter, ±0.018 rad tilt. Zero static frames. No wide shot. Motion blur streaks on every second cut, chromatic RGB split on the flatline ±3px.

**LIGHTING / GRAPHICS:** Cold 6500K key, red stress wash from upper right, 5.5% grain, vignette. The horizontal flatline is the compositional spine — it becomes the reveal flare.

**AUDIO CUES:** Dissonant unresolved drone (110 / 155.56 / 233.08 Hz), ticking 8th-note hats increasing in level each beat, sub pulses on beats 0/2/4/6, glitch clicks, riser from 3.50s. **At 4.50s all sound stops** — 500ms of silence. VO: "Another chat box. Nothing changes." (0.40s).

**TRANSITION OUT — THE MATCH CUT (4.45–5.00s):** every UI element falls away. Only the flat white line remains; it grows from centre to full frame width and cools from white to blue. At 5.00s that line *is* the anamorphic flare behind the orb. This is the single most important edit in the film.

**ASSET DIRECTIONS:** chat panel (1620×740 rounded 34px, `#101820`, 1.6px `#e9f0ea` @18% stroke), 3 bubbles, typing dots, 18 notification pills, 44 motion-blur shards, flatline (2.5px, `#d7e6f0` @85%), red/cyan split copies. All code-drawn in `hook()`; no external assets.

---

### ACT 02 — THE REVEAL · `5.00–15.00s` · The Hero Shot

**Intent:** One object, one continuous move, four colour states. Sell desire before proof.

**VISUAL PROMPT:**
> Sweeping dolly-in through black volumetric smoke. A single blue glass orb enters from the lower right, floating and breathing, with a warm champagne-amber rim light against a cold cyan fresnel edge. Fine bokeh dust drifts in parallax, two soft volumetric light cones rake down from above, and a long horizontal anamorphic flare threads through the orb's equator. The orb's glass shows a specular highlight at 10 o'clock, inner caustics, faint concentric instrument rings, and 22 orbiting particles. As it listens, three cyan ripple rings expand; as it speaks, a 48-bar waveform halo pulses. Floating 3D UI cards with a −0.06 shear hover nearby: "LIVE TRANSCRIPT · play some rain for me", then `play_sound("rain") · EXECUTED`. Photorealistic studio, moody rim lights, subtle lens flare, volumetric particles, no environment, infinite black. 16:9.

**TEXT OVERLAYS:**
- `MEET` (21px amber, tracked 12) + `CALMORA.` (104px heavy white, bloom) — 0.85–4.60s local
- `A quiet place to think out loud.` — 39px italic Fraunces, amber highlight, 1.60–5.10s local
- `LIVE TRANSCRIPT` + typewriter `play some rain for me` — 4.35–7.80s local
- `play_sound( "rain" ) · EXECUTED` — mono pill with foam status dot, 8.15–10.00s local
- `LISTENS · COMFORTS · REMEMBERS · ACTS` — 19px tracked, bottom centre, 5.60–9.90s local
- State legend: `IDLE / LISTENING / THINKING / SPEAKING` with live colour dots (blue/cyan/yellow/orange)

**CAMERA:** Single continuous **dolly-in 0.70× → 1.00×** over 4.3s, easing out; tilt −5.4° → 0°; pan 250px → 0; orb travels (1540, 790) → (1180, 566), radius 96 → 292px. No cut inside the act — only beat accents. Bloom ramps with the dolly. Motion-blur streaks fade out as the camera settles.

**LIGHTING / GRAPHICS:** Warm amber rim (#f6ddb6 → #e9c08c) on the left arc, cold white/cyan fresnel on the right, blue volumetric bloom at 52% screen, anamorphic streak 400→1750px, two sky-blue volumetric cones, parallax dust 150 particles. Grain + vignette maintained.

**STATE CHOREOGRAPHY (the product demo):** `idle` blue 5.0–9.2 · `listening` cyan + ripples 9.2–11.6 · `thinking` yellow 11.6–12.8 · `speaking` orange + waveform halo 12.8–15.0. The tool chip at 13.2s is the magic moment planted before Act 03 explains it.

**AUDIO CUES:** At 5.00s a full **impact** (135→42Hz kick, filtered noise sweep, 70Hz sub) plus a warm D minor add9 pad `[146.83, 174.61, 220, 329.63]` — the tonal resolution of the hook's dissonance. Heartbeat kick on beats 1 & 3, claps on 2 & 4, 8th hats, pentatonic pluck arpeggio from 8.0s. Bell at 9.6s (transcript), short riser 11.9s, bright bell + whoosh at 13.2s (tool fires). VO: "This is Calmora. An orb that listens, and acts. A quiet place to think out loud."

**ASSET DIRECTIONS:** orb mesh (radial gradient `#cdefff` → `#3ea2ff` → `#1b4fae` → `#0a1f4a`, specular ellipse at −34%/−38%, amber rim arc from 0.62π to 1.86π, 3 inner caustic strokes, 22 orbiting particles), bloom (2.9× radial), 2 instrument rings, volumetric smoke (5 drifting radial gradients), anamorphic flare (4 stacked gradient layers), transcript card (520×92, −0.06 shear), tool pill. All code-drawn in `reveal()` + `orb()`.

---

### ACT 03 — VALUE IN ACTION · `15.00–25.00s` · Three Core Pillars

**Shared grammar:** numbered outline `01/02/03` in Fraunces at 9% opacity, 62px tracked title, 21px one-line descriptor, 370px amber rule, a vertical split-screen hairline at x=690 with a travelling amber scan node, lateral tracking camera, floating 3D UI cards (−0.055 shear, 46px shadow), motion-blur streaks, beat-locked entrances. Each pillar gets one impact + whoosh.

#### PILLAR 01 · `15.00–18.50s` · **IT ACTS**
> **Visual prompt:** Beat-cut split screen. Left: a voice prompt pill "play some rain for me" above a live cyan waveform, with a small listening orb and an expanding coherent-breathing ring. Right: three floating glass tool cards slide in from off-right on consecutive beats, each with a mono function signature and a coloured "EXECUTED / LAUNCHED / SAVED" status. Fine diagonal rain streaks fall across the whole right field. Moody rim light, dark teal panels, foam/amber status dots.

- **Overlays:** `01 / IT ACTS`, `A voice agent that does things, not just replies.`, `YOU SAY`, `“play some rain for me”`, `play_sound( "rain" ) · SOUNDSCAPE STARTED`, `start_breathing( "coherent" ) · EXERCISE LAUNCHED`, `note_thought( "proud of today" ) · SAVED TO JOURNAL`, `ACT, THEN NARRATE.`
- **Camera:** 1.03× with a −70→+40px lateral track, 0.008 rad tilt. Cards enter at 15.45 / 16.30 / 17.15s with 0.55s ease-out + 40px overshoot.
- **Audio:** four-on-the-floor kick from 15.0s, 16th hats, bass D2/F2, pluck sequence, bells on each card landing (15.5 / 16.35 / 17.2), impact+whoosh at 15.0. Rain SFX implied by the score's high-pass noise shimmer.
- **Assets:** 3 cards (760×128, rounded 18), waveform generator (2.4px gradient stroke), 70 rain motes, mini orb (r=74), breathing ring (r=112±22%). Uses the real tool signatures from `functions/api/chat.js`.

#### PILLAR 02 · `18.50–22.00s` · **IT SOUNDS**
> **Visual prompt:** A wide stereo waveform ribbon: five layered sine traces in cyan and seafoam, mirrored L/R like a binaural beat, floating over a 64-bar live spectrum analyser. Seven small soundscape chips ("RAIN OCEAN FOREST BROWN FIRE NIGHT CAVE") snap in one per beat. A giant ghosted serif `07` sits behind the ribbon. Two tracked callouts read binaural 7.83 Hz Schumann and Solfeggio 174–963 Hz. Camera tracks left to right with directional motion blur. No audio files, no waveforms from stock libraries — everything is generated motion.

- **Overlays:** `02 / IT SOUNDS`, `Seven soundscapes. Zero audio files.`, `BINAURAL · 7.83 Hz SCHUMANN`, `SOLFEGGIO 174–963 Hz`, `SYNTHESISED LIVE IN THE BROWSER`, chips `RAIN · OCEAN · FOREST · BROWN · FIRE · NIGHT · CAVE`.
- **Camera:** 1.06×, pan −150 → +170px, tilt −0.006 rad, 18px vertical offset. Streak intensity 1.0 — the fastest move in the film.
- **Audio:** impact+whoosh at 18.5s, sustained Dm pad, rising 16th-note pluck density, short riser at 21.6s into Pillar 03.
- **Assets:** 5 waveform traces (1060px wide, 0.012–0.028 freq), 64 spectrum bars (7px, foam→blue vertical gradient), 7 chips (152px pitch), ghost numeral (330px Fraunces @5.5%).

#### PILLAR 03 · `22.00–25.00s` · **IT STAYS YOURS**
> **Visual prompt:** A glass device card holds four rows — JOURNAL, MOOD CHECK-INS, CONVERSATION HISTORY, SETTINGS — each stamped LOCAL in seafoam. To the right, a translucent vertical barrier: coral data packets stream toward it, hit the glass, and reflect back. Beyond it, a red X over `SERVER / NO ACCOUNT`. Three proof chips land at the bottom: OFFLINE PWA, EXPORT ANYTHING, ERASE ALL DATA. A tiny idle orb sits to the left. Cool, clean, forensic lighting — the calm after the kinetic peak.

- **Overlays:** `03 / IT STAYS YOURS`, `Your data never leaves the device.`, `ON THIS DEVICE`, the four row labels + `LOCAL`, `SERVER`, `NO ACCOUNT`, `OFFLINE PWA / EXPORT ANYTHING / ERASE ALL DATA`.
- **Camera:** 1.02×, pan +60 → −50px, 0.004 rad tilt. Slower than Pillar 02 — the edit decelerates into the CTA.
- **Audio:** impact+whoosh at 22.0s, groove continues but hats thin out, one rising riser toward 25.0s. VO resolves on "Yours, always." at 24.6s.
- **Assets:** device card (560×560, −0.02 shear), 4 rows (480×72) with staggered 0.22s entrances, glass barrier (36px gradient + 1.4px sky stroke), 12 bouncing packets, red X, 3 proof chips.

---

### ACT 04 — THE CTA · `25.00–30.00s` · The Outro

**Intent:** Zero new information. One object, one line, one URL, one blackout.

**VISUAL PROMPT:**
> Clean, locked-off minimalist end card on infinite near-black. A small breathing blue orb sits left of centre with a single horizontal anamorphic flare threading behind it. Right column: wide-tracked wordmark, an italic serif tagline, a hairline amber rule, a small seafoam promise line, a monospaced URL, a tracked proof line, and one pill-shaped CTA button. Volumetric smoke reduced to a whisper, sparse dust. Everything fades to black at 28.86s; at 29.50s one final blue pulse ring, then a confident hard cut to pure black.

**TEXT OVERLAYS:**
- `C A L M O R A` — 76px heavy tracked, 16px bloom
- `A quiet place to think out loud.` — 38px italic Fraunces, amber highlight
- `BE GENTLE WITH YOURSELF.` — 18px tracked seafoam
- `github.com/apsethicsbowl20026-collab/calmora-ai` — 25px mono white (⚠️ **swap for the deployed domain at publish**)
- `OPEN SOURCE · INSTALLABLE PWA · ZERO BUILD · PRIVATE BY DESIGN`
- `TALK TO CALMORA` — amber-outline pill with status dot

**CAMERA:** Locked off. No move. The orb only breathes (1.8% scale, 1.75 rad/s). This stillness is the payoff for 25 seconds of motion.

**LIGHTING / GRAPHICS:** 15% blue radial bloom, 1500px anamorphic flare, single sky instrument ring, 40% dust, grain + vignette.

**AUDIO CUES:** At 25.00s impact + warm Dm(add9) pad, then the beat drops away entirely — four sparse plucks (25.5 / 26.5 / 27.5 / 28.25) and one high bell at 26.5s. VO: "Calmora. Be gentle with yourself." (25.40s). **At 29.50s a final 55Hz sub boom + impact, then absolute silence and a hard blackout.** No fade-out music, no logo sting, no "brought to you by".

**ASSET DIRECTIONS:** orb (r=132), flare, wordmark, rule (760px amber gradient), URL in mono, 3 proof lines, CTA pill, final pulse ring. All code-drawn in `cta()`.

---

## 4. ASSET MANIFEST

| Asset | Path | Type | Status |
|---|---|---|---|
| Motion-graphics master | `video/calmora-launch.html` | Self-contained HTML/Canvas/Web Audio | ✅ Shipped — no build, no dependencies |
| Key-frame storyboard | `video/storyboard.png` | 1980×1140 PNG, 12 captioned frames | ✅ Shipped, rendered from the master |
| VO · hook | `video/audio/vo-hook.mp3` | 3.21s, 56 kbps | ✅ Shipped |
| VO · reveal | `video/audio/vo-reveal.mp3` | 8.69s | ✅ Shipped |
| VO · value | `video/audio/vo-value.mp3` | 10.10s (played 1.06×) | ✅ Shipped |
| VO · cta | `video/audio/vo-cta.mp3` | 3.36s | ✅ Shipped |
| Score | generated at runtime | Web Audio oscillators + procedural noise + convolution IR | ✅ No audio files — mirrors the product's own "no audio files" engine |
| Orb, UI, particles, flares | generated at runtime | Canvas 2D primitives | ✅ No image assets |
| Poster / thumbnail | exportable | `↓ PNG frame` at ~9.8s (hero) or ~26.6s (end card) | ▶ Use the player |

---

## 5. AI-GENERATION PROMPT LIBRARY (if re-creating in Runway / Blender / AE)

Use these as **single-image, single-shot** prompts. One prompt per shot — never a grid or montage. Append the shared suffix to each:

> *Shared suffix:* "photorealistic studio lighting, moody rim lights, subtle anamorphic lens flare, volumetric smoke and fine floating particles, deep near-black teal background `#070d0e`, warm champagne-amber `#e9c08c` rim light, cold cyan/blue glass, 35mm or 100mm macro, shallow depth of field on the hero object, high contrast, fine film grain, no text artifacts, no people, no hands, no phone bezels, 16:9, cinematic colour grade, no corporate stock aesthetic."

1. **Hook macro:** "extreme macro of a dark glass chat panel, a single flat horizontal light line cutting across the centre, hollow grey chat bubbles, red chromatic split, notification debris, 3:17 AM tension" + suffix.
2. **Match cut:** "a single hairline of white-blue light stretching across infinite black, minimal, high contrast, negative space" + suffix.
3. **Hero orb:** "a luminous blue glass sphere floating in black volumetric smoke, warm amber rim light on the left edge, cyan fresnel on the right, specular highlight, concentric instrument rings, orbiting dust, long anamorphic flare through its equator" + suffix.
4. **Listening state:** same orb in bright cyan with three expanding ripple rings and a floating translucent glass transcript card" + suffix.
5. **Speaking state:** same orb in warm orange with a circular waveform halo and rain motes" + suffix.
6. **Acts split screen:** "three floating glass tool cards stacked in perspective over dark teal, mono code labels, seafoam status dots, fine diagonal rain" + suffix.
7. **Sounds ribbon:** "layered cyan and seafoam sine-wave ribbon with a live spectrum analyser, ghosted numeral 07, studio black" + suffix.
8. **Privacy barrier:** "translucent vertical glass barrier, coral data particles reflecting back off it, dark forensic lighting" + suffix.
9. **End card:** "small breathing blue orb left of centre in infinite black, single horizontal anamorphic flare, generous negative space on the right for typography" + suffix.

**Negative prompt (all shots):** stock photo, smiling person, beach, sunset, meditation pose, headset, laptop on desk, gradient mesh, purple AI sparkles, lens-flare preset, watermark, UI text gibberish, clutter, low contrast, flat lighting, generic corporate blue.

**Grade / LUT:** lift blacks slightly toward `#070d0e`, crush midtones, warm the highlights only (amber), keep cyan/blue saturation in the orb, red reserved for Act 01. Grain 5.5%, vignette 0.78 at corners.

---

## 6. SOUND DESIGN SPEC

- **Tempo:** 120 BPM. All cuts and card/chip entrances land on beats or half-bars.
- **Synthesis:** the score is built live from oscillators, filtered white noise, and a procedurally generated convolution impulse response. No audio files — an intentional echo of Calmora's Web Audio soundscape engine.
- **Structure:** Act 01 unresolved drone `[110, 155.56, 233.08]` + rising ticks + riser → 500ms silence · Act 02 impact resolves into D minor add9 `[146.83, 174.61, 220, 329.63]`, heartbeat groove, pentatonic plucks · Act 03 four-on-the-floor, 16th hats, three pillar impacts · Act 04 groove strips to air + plucks → one final sub boom → silence.
- **Mix:** music bus 0.62, VO bus 0.95, VO send 10% to plate, compressor −14 dB threshold / 3.5:1. VO deliberately sits *above* but never *over* the score; the 500ms silence at 4.5s is the loudest moment.
- **SFX hits:** impact (5.0, 15.0, 18.5, 22.0, 25.0, 29.5), whoosh on pillar cuts, tool ping (13.2), transcript bell (9.6), card bells (15.5 / 16.35 / 17.2).

---

## 7. EDITING STYLE — non-negotiables

- **Cut strictly on the beat.** No dissolve, no whip-pan transition preset, no crossfade between acts.
- **Motion matches music:** Act 01 staccato 0.5s cuts; Act 02 one sustained 4.3s dolly; Act 03 0.42–0.85s rhythmic entrances; Act 04 locked-off stillness.
- **Motion blur:** directional streaks on camera pans and beat cuts, ghosted orb blooms, never a global blur filter.
- **Camera:** macro close-ups, smooth tracking, dynamic tilt. Zero static flat angles in Acts 01–03; the single static frame is the CTA and it is a deliberate contrast.
- **No generic corporate stock video templates.** Every graphic is product-specific: real tool signatures, real soundscape names, real orb state colours, real repo URL.

---

## 8. HOW TO RUN / EXPORT / PUBLISH

```bash
cd calmora-ai
python3 -m http.server 8000 --bind 0.0.0.0
# open http://localhost:8000/video/calmora-launch.html
```

| Control | What it does |
|---|---|
| `▶ Play` / `Space` | Play/pause with sample-accurate audio rescheduling |
| Timeline / chapter cards | Scrub or jump to any act; audio re-cues from the new playhead |
| `◉ Sound` / `◉ Voiceover` | Independent buses; toggle for an instrumental-only cut |
| `↓ PNG frame` | Exports the current 1920×1080 frame — use ~9.8s for a poster |
| `● Record WebM` | Renders the full 30s in real time via `canvas.captureStream` + the live audio bus; downloads `calmora-launch-film-30s.webm` (Chromium). Keep the tab visible and unmuted. |

**Before publishing:** (1) replace the end-card URL with the deployed domain — the film currently points at the GitHub repo because that is the only real address this project has; (2) keep the "wellbeing companion, not a medical device" constraint in any platform copy; (3) export a 9:16 cutdown by reframing the orb at x=960 and stacking the copy vertically (the title block and end card both need a safe-area pass).

---

## 9. DIRECTOR'S ADDENDA

- **15s cutdown:** 0–2.2 hook (keep `ANOTHER CHAT BOX.` + `NOTHING CHANGES.`), 2.2–6.8 hero reveal, 6.8–12.5 compress the three pillars to one card each, 12.5–15 CTA. Drop the state legend and all tracked sub-copy.
- **6s bumper:** the match cut at 4.45 → hero orb at 5.0 → `CALMORA. Be gentle with yourself.` → blackout.
- **Localization:** the film ships with English VO, but `index.html` already supports en/es/fr/de/pt. Re-record four VO clips per locale and swap the overlay strings; the timing map is unchanged because the score is VO-independent.
- **A/B test:** variant A opens on `NOTHING CHANGES.` first (pain-forward); variant B opens cold on the orb at 5.0s (desire-forward). Keep the match cut and the 29.5s blackout identical in both — they are the brand signatures.
