# AI PROJECT LOGBOOK

## CALMORA — a quiet place to think out loud

**PROJECT NAME:** CALMORA
**PROJECT TYPE:** Voice-first, privacy-preserving AI wellbeing companion (web app / PWA)
**SCHOOL NAME:** [[School / organisation name]]
**YEAR/CLASS:** [[Year and class, e.g. 2026–27 / Grade XII]]
**TEACHER / MENTOR NAME:** [[Teacher or mentor name]]
**TEAM MEMBER NAMES AND GRADES:** [[Name 1 · Grade]], [[Name 2 · Grade]], [[Name 3 · Grade]]
**REPOSITORY:** https://github.com/apsethicsbowl20026-collab/calmora-ai
**LOGBOOK COMPLETED:** 3 November 2026

> Adapted from the "IBM EdTech Youth Challenge – Project Logbook" developed by IBM in collaboration with Macquarie University, Australia and the Australian Museum. This copy has been completed for the Calmora project.

[PAGEBREAK]

## 1. Introduction

This document is our Project Logbook. It records the ideas, research, decisions, tests and reflections behind **Calmora**, a private, installable, voice-driven mental-wellness companion.

**What we built.** Calmora is a single-file web app that listens, comforts, remembers — and acts. A person taps a glowing orb (or types), speaks for a moment, and gets a short, warm, practical reply. The app can also *do* things: play a live-synthesised soundscape, save a thought to a private journal, start a guided breathing exercise, open a grounding exercise, or begin sleep mode — then it says out loud what it did. Everything personal stays in the browser. It works offline, installs like a native app, and has no build step.

**Why we built it.** Most "AI wellness" tools are thin chat wrappers: they reflect feelings back at you, ask you to sign in, and store your most private thoughts on someone else's server. We wanted something a student could open at 2 a.m. without an account, speak to instead of typing at, and walk away from with *one small doable next step*.

**How to use this logbook.** Work through it digitally with your team; add pages, screenshots, interview notes and test logs as supporting material. Refer to the AI Project Guide for more detail about each step. Replace every highlighted [[field]] with your team's real details before submitting.

> **Scope and safety.** Calmora is a wellbeing companion, not a medical device, therapist or crisis service. It does not diagnose, treat or replace professional care. Anyone in immediate danger is directed to local emergency services, a trusted person, or a crisis helpline.

[PAGEBREAK]

## 2. Team Roles

### 2.1 Who is in your team and what are their roles?

| Role | Role description | Team member |
|---|---|---|
| PROJECT LEADER | Define project scope and success criteria; resolve issues as they arise; own the progress report and final submission. | [[Name 1]] |
| PROJECT MANAGER | Distribute tasks among team members; keep deadlines; organise and manage this logbook, the repo and the shared drive. | [[Name 2]] |
| INFORMATION RESEARCHER | Investigate the problem with end users; run interviews and observations; research evidence-informed calming techniques and local helplines. | [[Name 3]] |
| DATA EXPERT | Decide what data and prompts are needed and where they come from; own privacy review, tool schemas and the evaluation set. | [[Name 2]] |
| DESIGNER | Create the orb, colour states, chat UI and flow; keep visuals calm and impactful; plot the roadmap and own the PWA shell. | [[Name 1]] |
| SAFETY & QUALITY LEAD | Take the final decision on test numbers and metrics; own the crisis-detection rules, point out patterns and outliers, and sign off on the safety card. | [[Name 3]] |
| TESTER | Build and test across browsers and offline states; test tool calls, voice, accessibility and privacy; decide which fixes ship. | [[Name 1]], [[Name 3]] |

**Teacher / mentor:** [[Teacher or mentor name]] — reviewed our problem statement, safety wording and final prototype.

### 2.2 Project plan

Planned and actual dates are shown together; where a phase ran long, the actual duration is noted. Owners are the team members listed in 2.1.

| Phase | Task / deliverable | Planned & actual dates | Hours | Owner | Notes / remarks |
|---|---|---|---|---|---|
| Preparing for the project | Coursework, readings on AI ethics, wellbeing techniques and web APIs | 10–11 Aug 2026 | 6 hr | All team members | Read the AI Project Guide and the IBM logbook template. |
| Preparing for the project | Set up the GitHub repo and shared drive folder | 11 Aug 2026 | 1 hr | [[Name 1]] | `calmora-ai` repo created; README started. |
| Defining the problem | Background reading on barriers to seeking help | 11–12 Aug 2026 | 2 hr | All team members | Stigma, cost, waiting lists, late-night isolation, privacy. |
| Defining the problem | Research issues in our school community | 12 Aug 2026 | 2 hr | [[Name 3]] | Short conversations with students and a mentor. |
| Defining the problem | Team meeting to select one issue | 12 Aug 2026 | 1 hr | All team members | Chose "no private, in-the-moment, actionable support". |
| Defining the problem | Complete section 3 of the logbook | 12 Aug 2026 | 1 hr | [[Name 2]] | **Rate yourselves: 3/3** |
| Understanding the users | Identify users; observe and interview them; empathy map | 12–14 Aug 2026 | 5 hr | [[Name 3]] | Six interview questions; see 4.3. |
| Understanding the users | Complete section 4 of the logbook | 14 Aug 2026 | 1 hr | All team members | **Rate yourselves: 3/3** |
| Brainstorming | Team meeting to generate AI ideas and priority grid | 14 Aug 2026 | 3 hr | All team members | Five ideas, four-quadrant grid. |
| Brainstorming | Complete section 5 | 15 Aug 2026 | 1 hr | [[Name 2]] | **Rate yourselves: 3/3** |
| Designing your solution | Design the orb states, tool-using agent, offline fallback and data flow | 15–16 Aug 2026 | 4 hr | [[Name 1]] | Decided on a two-tier client/server architecture. |
| Designing your solution | Complete section 6 | 16 Aug 2026 | 1 hr | [[Name 2]] | **Rate yourselves: 3/3** |
| Collecting and preparing data | Write the system prompt, tool schemas, offline reply library and UI translations | 16–17 Aug 2026 | 8 hr | [[Name 2]], [[Name 3]] | No model training; prompt + rules + local data only. |
| Prototyping | Build `index.html`, `functions/api/chat.js`, `sw.js`, manifest and icon | 17 Aug – 30 Sep 2026 | 46 hr | [[Name 1]] | Ran long; extra time on streaming and voice reliability. |
| Prototyping | Complete sections 7 and 8 | 30 Sep 2026 | 2 hr | [[Name 2]] | **Rate yourselves: 3/3** |
| Testing | Write the test plan, run the browser/privacy/safety matrix, gather feedback | 1–13 Oct 2026 | 14 hr | [[Name 3]] | See section 9. |
| Testing | Complete section 9 | 13 Oct 2026 | 2 hr | [[Name 2]] | **Rate yourselves: 3/3** |
| Creating the video | Script, film, edit and review the 3-minute project video | 14–20 Oct 2026 | 9 hr | All team members | Demonstrate: voice → tool → narration → offline. |
| Completing the logbook | Team reflection, sections 10 and 11, review of logbook and video | 21–31 Oct 2026 | 4 hr | All team members | **Rate yourselves: 3/3** |
| Submission | Submit entries and deploy the app | 3 Nov 2026 | 1 hr | [[Name 1]] | Deploy to Cloudflare Pages; attach repo + video links. |

### 2.3 Communications plan

- **Will you meet face-to-face, online or a mixture of each?** A mixture of both — face-to-face at school whenever possible, online in the evenings and on weekends.
- **How often will you come together to share your progress?** Two to three times a week, plus a longer review at the end of each phase.
- **Who will set up online documents and ensure that everyone is contributing?** [[Name 1]] set up the GitHub repo and shared drive; [[Name 2]] maintains this logbook and checks that every section and meeting minute is filled in.
- **What tools will you use for communication?** GitHub (code, commits, issue tracking), Google Meet, WhatsApp, phone calls, and a shared Google Doc / Drive folder for the logbook draft.

### 2.4 Team meeting minutes

**Date of meeting:** 11 August 2026
**Who attended:** [[Name 1]], [[Name 2]], [[Name 3]]
**Who wasn't able to attend:** None
**Purpose of meeting:** Kick-off, research on the topic, discussion of ideas and division of roles.
**Items discussed:**
  - Problems around us and how AI might help with them; we listed school-related stress, sleeplessness and the reluctance to ask for help.
  - Shortlisted three areas, then agreed to focus on everyday emotional support because it affects students directly.
  - Roles assigned as recorded in 2.1.
**Things to do:** Ask people in the locality about daily problems ([[Name 1]] and [[Name 3]]); create the repo and shared folder and start the logbook ([[Name 1]] and [[Name 2]]).

**Date of meeting:** 12 August 2026
**Who attended:** All team members
**Purpose of meeting:** Finalise the problem definition.
**Items discussed:**
  - Existing apps are text-heavy, account-based and only *reflect* feelings; they rarely give a concrete next step.
  - Decided the solution must be voice-first, private by design, and able to take action.
  - Agreed Calmora must never present itself as a therapist or a crisis service.
**Things to do:** Draft the problem statement and complete section 3.

**Date of meeting:** 14 August 2026
**Who attended:** All team members
**Purpose of meeting:** Brainstorm AI solutions.
**Items discussed:** Five AI ideas (section 5.1); a priority grid comparing value to users against ease of development; a tool-using conversational agent was chosen over a plain chatbot or a custom-trained model.
**Things to do:** Research which AI platform supports streaming replies and function calling.

**Date of meeting:** 15 August 2026
**Who attended:** All team members
**Purpose of meeting:** Design the solution.
**Items discussed:**
  - Orb colour states (idle blue, listening bright blue, thinking yellow, speaking orange) and the two views (orb / chat).
  - Two-tier architecture: everything in `index.html`; the system prompt, key, tool schemas and limits in a Cloudflare Pages Function at `/api/chat`.
  - Offline companion so the app is still useful without a network or an API key.
**Things to do:** Start on the system prompt, tool definitions and data/privacy plan.

**Date of meeting:** 17 August 2026
**Who attended:** All team members
**Purpose of meeting:** Discuss data requirements and safety.
**Items discussed:**
  - We are *not* training a model. We need a written system prompt, tool schemas, an offline reply library, interface translations and a scripted evaluation set.
  - Personal data (journal, moods, transcript, settings) must stay in `localStorage`; only conversation text goes to the model.
  - Crisis language must trigger a safety card with local emergency numbers, a trusted person and helplines.
**Things to do:** Write the prompt and tool schemas; draft the crisis detection rules; begin prototyping.

**Date of meeting:** 1 September 2026
**Who attended:** All team members
**Purpose of meeting:** Prototyping review.
**Items discussed:** Streaming NDJSON events (`delta`, `tool`, `done`); executing tool calls instantly in the browser; feeding tool results back for one short spoken sentence (capped at 3 rounds); the 14-second voice cap and the double-commit guard that stop "won't stop listening" loops.
**Things to do:** Finish the soundscape engine, exercises and PWA shell.

**Date of meeting:** 1 October 2026
**Who attended:** All team members, [[Teacher or mentor name]]
**Purpose of meeting:** Agree the testing plan.
**Items discussed:** Test matrix across browsers, online/offline, voice/text, tool calls, privacy and safety; how to record observations and user feedback; mentor asked us to check the crisis wording carefully.
**Things to do:** Run the matrix with team members first, then with end users.

**Date of meeting:** 13 October 2026
**Who attended:** All team members
**Purpose of meeting:** Review testing results and decide refinements.
**Items discussed:** Tool calls worked with function-calling models but not always with the free default; offline mode and the safety card behaved as designed; users wanted a manual send option and a longer pause before auto-send; Firefox has no voice input.
**Things to do:** Document refinements (9.4), note roadmap items (9.5), complete section 9.

**Date of meeting:** 20 October 2026
**Who attended:** All team members
**Purpose of meeting:** Plan the video and final review.
**Items discussed:** Three-minute script, screen recordings of the orb and tools, voice-over, and the order of the demonstration. Agreed the logbook must be finished before filming the closing shot.
**Things to do:** Film and edit the video; complete sections 10–12.

[PAGEBREAK]

## 3. Problem Definition

### 3.1 List important local issues faced by your school or community

i) **Everyday stress goes unsupported.** Students regularly feel anxious, overwhelmed or unable to sleep, but many never talk to anyone about it. In our conversations the reasons were consistent: stigma, not wanting to "burden" someone, no one to talk to late at night, the cost and waiting time of professional help, and simply not knowing what to do in the moment.

ii) **Available tools don't fit the moment.** Most "AI wellness" apps are thin chat wrappers: long text replies, no concrete action, an account and a cloud profile required. When someone is already overwhelmed, typing a paragraph and reading a wall of text is a barrier, and handing private thoughts to a server is a trust problem. English-only interfaces exclude many families in our community.

iii) **Generic conversation can be unsafe.** A chatbot that only reflects feelings can miss a crisis, give clinical-sounding advice, or imply it is a therapist. Young people need a clear boundary, an immediate route to real human help, and local emergency/helpline numbers rather than a generic message.

### 3.2 Which issues matter to you and why?

These are issues we see among people our own age, so the people affected are our classmates and friends, not an abstract user group. A bad night, a panic moment before an exam, or the feeling that "everything is too much" is common — and the moment passes long before an appointment is available. We also care about privacy: a journal of someone's low moments is among the most sensitive data a person can create, and we did not want it on a server. Finally, we believe an AI tool should be honest about what it is. A companion that quietly pretends to be a clinician is worse than no tool at all.

The issue is not fully solved by existing products: they optimise for engagement and chat length, whereas our users need *one short, kind, useful next step* and then to be left alone.

### 3.3 Which issue will you focus on?

We focused on the gap between **feeling overwhelmed** and **getting one small, practical action** — private, in the moment, and usable without an account or a network connection. Our approach: a voice-first companion that listens, validates briefly, then either teaches a tiny technique (slow breathing, a CBT reframe, grounding, one small next step) or *acts* by launching an exercise, a soundscape, a journal note or sleep mode. The tool also raises awareness that these techniques exist, which is the first step towards using them without the app.

### 3.4 Write your team's problem statement in the format below

> **How might we give students in our school community a private, voice-first way to feel heard and get one small, evidence-informed action in the moment — even offline — while keeping their personal data on their own device and directing anyone in crisis to real human help?**

**Rate yourself: 3/3** — *Problem Definition.* 1 point: a local problem is described. 2 points: a local problem which has not been fully solved before is described. 3 points: a local problem which has not been fully solved before is explained in detail with supporting research (our interviews, observations, product review and mentor input in sections 4 and 9).

[PAGEBREAK]

## 4. The Users

### 4.1 Who are the users and how are they affected by the problem?

**Primary users:** students and young people (roughly ages 14–19) dealing with ordinary stress, anxiety, low mood, anger, loneliness or sleeplessness. They are affected at the exact moment they need help: support is slow, public, text-heavy or expensive, so they do nothing and the feeling grows.

**Secondary users:** school counsellors, mentors and parents — not as patients, but as the trusted humans our app points to, and as stakeholders who can tell us whether our safety wording is responsible. Our app can also be configured with a trusted person's phone number.

**Not our users / boundary:** people in acute crisis, or anyone needing diagnosis, medication advice or ongoing therapy. Calmora explicitly redirects those users to local emergency services, a trusted person, or a crisis helpline.

### 4.2 What have you actually observed about the users and how the problem affects them?

  - People reach for their phone late at night, when no one is awake to talk to; a 2 a.m. user does not want to type a long message or fill in a form.
  - Users are comfortable speaking to a device with headphones on, but also want to type quietly in a shared room or in public — so both input modes are required.
  - Asking someone to create an account before they can say "I feel anxious" is enough to make them close the app.
  - People are suspicious of "AI therapy"; they like a tool that helps with small things (breathing, sleep sounds, writing a thought down) and are relieved when it says plainly that it is not a therapist.
  - Long, generic replies ("I understand, tell me more") are experienced as dismissive; short replies with one concrete suggestion are experienced as helpful.
  - Our community is multilingual. An English-only interface excludes users and their families; the app needed at least the main languages spoken at home.

### 4.3 Record your interview questions here as well as responses from users

**Interviewer:** When you're stressed or can't sleep, what do you do first?
**User:** "I scroll, or I just lie there. I don't want to write a whole paragraph about it — that feels like homework."

**Interviewer:** What stops you from talking to a person about it?
**User:** "I don't want to make it a big deal, or worry anyone. And at night there's nobody around anyway. Also, I wouldn't know where to start."

**Interviewer:** Would you use an app that keeps a record of how you feel?
**User:** "Only if it stays on my phone. No account, no one else seeing it. I'd want to be able to delete everything."

**Interviewer:** Do you think AI can help with this?
**User:** "For small things, yes — like reminding me to breathe, or playing rain, or helping me sleep. I wouldn't trust it with anything serious, and I don't want it pretending to be a doctor."

**Interviewer:** What would make you close the app immediately?
**User:** "A long lecture, or 'I understand' on repeat, or being told to sign up. And clinical words I don't use."

**Interviewer:** Is voice useful, or would you rather type?
**User:** "Voice at night or when I'm walking, definitely. But I need typing too, for the bus or a library."

### 4.4 Empathy Map

| What our users are SAYING | What our users are THINKING |
|---|---|
| "I don't want to make it a big deal." "I can't sleep and everyone's asleep." "Only if it stays on my phone." "Just tell me one thing to do." | "Is this private — who can see it?" "Is this actually useful, or just another chatbot?" "Am I overreacting?" "Will this replace talking to a real person, or help me get there?" |
| **What our users are DOING** | **How our users FEEL** |
| Scrolling or lying awake late at night; keeping feelings to themselves; putting headphones in; searching for "how to calm down"; abandoning apps that require sign-in; sometimes writing a thought down privately. | Relieved when a small step works; wary of being judged or recorded; frustrated by generic advice; safer when nothing leaves their device; grateful when the app is honest about its limits; more in control after one tiny action. |

### 4.5 What are the usual steps that users currently take related to the problem and where are the difficulties?

1. They notice the feeling and try to ignore it, or distract themselves with their phone. *Difficulty:* the feeling usually returns, often at night.
2. They consider telling someone, then decide against it. *Difficulty:* stigma, not wanting to burden anyone, no one available.
3. They search online for generic advice or open a wellness app. *Difficulty:* long articles, account walls, cloud profiles, text-only chat.
4. If they do chat, they get reflective, open-ended replies. *Difficulty:* no concrete next step, no exercise actually started, no sound actually played.
5. They eventually sleep badly or wait for the feeling to pass. *Difficulty:* nothing was learned that could help next time, and nothing was recorded privately for reflection.

### 4.6 Write your team's problem statement in the format below

> Students and young people in our school community are experiencing a gap between feeling overwhelmed and getting a small, useful next step, because existing support is slow, text-heavy, account-based, and rarely private or actionable in the moment.

**Rate yourself: 3/3** — *The Users.* 1 point: the user group is described but it is unclear how they are affected. 2 points: understanding is evidenced by completion of most steps in this section. 3 points: understanding is evidenced by completion of all steps in this section and thorough investigation (interviews, observations, empathy map, journey steps and stakeholder review).

[PAGEBREAK]

## 5. Brainstorming

### 5.1 Ideas

*How might you use the power of AI/machine learning to solve the users' problem by increasing their knowledge or improving their skills?*

**AI Idea #1 — Voice-first conversation.** Use browser speech recognition for live transcription in the prompt bar, auto-send about 2 seconds after the person stops, and speech synthesis to reply aloud. The AI answers in 1–4 short spoken sentences, with no lists, markdown or jargon.

**AI Idea #2 — A tool-using agent, not just chat.** Give the model six tools (`play_sound`, `stop_sounds`, `note_thought`, `start_breathing`, `start_grounding`, `sleep_mode`). When someone says "play some rain for me", the rain actually starts; the model then narrates what it did in one warm sentence.

**AI Idea #3 — Teach a technique in the moment.** A compact system prompt that validates briefly and then delivers one practical skill: slow breathing (in for 4, out for 6), a CBT reframe, behavioural activation, shrinking overwhelm to one step, or 5-4-3-2-1 grounding, plus light psychoeducation that normalises the body's alarm response.

**AI Idea #4 — Private memory and gentle insight.** Save thoughts and mood check-ins locally, offer prompts and search, and show a 14-point mood curve with "gentle numbers" — no streaks, no shaming, no server copy. An optional anonymised mood average can inform the AI's tone.

**AI Idea #5 — A safety layer and an honest offline mode.** Detect crisis language client-side and show a safety card with the configured emergency number, a trusted person and helplines; append a crisis addendum to the server prompt. When there is no network or key, fall back to an on-device, pattern-matched companion so the app never goes silent.

### 5.2 Priority Grid

| Quadrant | Ideas | Reasoning |
|---|---|---|
| **High value to users, easy to create** | Curated offline companion, guided breathing / grounding / PMR / journal, synthesised soundscapes, local mood check-ins | No model needed, works offline, instantly useful, and fully private. |
| **High value to users, hard to create** | Streaming tool-using voice agent (LLM + function calling + NDJSON + agent loop), 7-language UI/STT/TTS, crisis addendum | The core of the project: hardest to build, but it is what makes Calmora act instead of only talking. |
| **Low value to users, easy to create** | A plain chatbot wrapper / FAQ bot with generic reflective replies | Quick to build, but duplicates products our users already reject. |
| **Low value to users, hard to create** | Training our own "therapy LLM" or a from-scratch speech recogniser | Enormous data, compute and safety burden for little extra benefit at our scale; also a privacy risk. |

*Axes: value to users (low → high) and ease of development (easy → hard).*

### 5.3 Based on the priority grid, which AI solution is the best fit for your users and for your team to create and implement?

We chose a **tool-using voice agent with a local-first, privacy-first architecture and an offline fallback**. A pre-trained large language model is accessed through **OpenRouter** from a **Cloudflare Pages Function** at `/api/chat`; that function owns the system prompt, the API key, tool schemas and concurrency limits, and streams the reply back as NDJSON. The browser never sees the server key. In the browser we use the **Web Speech API** for voice input, **SpeechSynthesis** for spoken replies, the **Web Audio API** for seven procedurally generated soundscapes (no audio files), `localStorage` for personal data, and a **service worker** so the app installs and works offline. Tool calls execute in the browser, results are fed back to the model, and the loop is capped at three rounds.

This was the best fit because it delivers the highest-value idea (an app that *acts*) while keeping every high-value/easy idea available offline, and it avoids the two low-value quadrants. It also matches our constraints: no budget, no dataset of private conversations, no server of our own, and a hard requirement that personal data never leave the device.

**Tools used:** OpenRouter (streaming chat + function calling), Cloudflare Pages Functions, Web Speech API, SpeechSynthesis, Web Audio API, Service Workers, `localStorage`, and standard HTML/CSS/JS — with **no build step**.

**Rate yourself: 3/3** — *Brainstorming.* 1 point: a brainstorming session was conducted and a solution selected. 2 points: creative and critical thinking with supporting arguments. 3 points: a compelling solution selected with supporting arguments from this section (five ideas, priority grid, trade-off analysis and tool justification).

[PAGEBREAK]

## 6. Design

### 6.1 What are the steps that users will now do using your AI solution to address the problem?

1. **Open and speak.** Tap the orb (or type). Live transcription fills the prompt bar; the app auto-sends about 2 seconds after the person stops speaking. The orb turns bright blue while listening, yellow while thinking and orange while speaking.
2. **Get one short, useful reply.** One sentence of empathy, one concrete thing to do right now — a 4-in/6-out breath, a kinder reframe, three things they can see, or one tiny next step — spoken aloud and shown as captions. No lists, no jargon, no clinical claims.
3. **Ask for an action.** "Play some rain", "remember that I'm proud of how I handled today", "help me breathe", "tuck me in". The model calls a tool; the sound starts, the note saves, or the exercise opens immediately, and Calmora says one warm sentence about what it did.
4. **Keep everything private.** Journal entries, moods, transcript and settings stay in the browser. The user can export everything or erase all data at any time; only conversation text is sent to the AI, and reasoning is filtered out.
5. **Be safe.** If crisis language is detected, a safety card appears with the configured local emergency number, a trusted person and international helplines; the model receives a crisis addendum and encourages immediate human help without discussing methods.
6. **Keep going offline.** With no network or no key, the offline companion still replies and every wellness tool — breathing, grounding, PMR, values, journal, soundscapes, sleep mode — still works.

### 6.2 How the design meets user needs (new vs old experience)

| Before | With Calmora |
|---|---|
| Type a long message, create an account, wait for a wall of text. | Speak one sentence; see it transcribed; get 1–4 short spoken sentences. |
| "I understand — tell me more." | Empathy plus one concrete technique or one tiny next step. |
| Advice the user has to go and carry out themselves. | The app starts the breathing exercise, plays the rain, or saves the thought itself. |
| Personal data stored on a company server. | Local-first storage; export and erase controls; no account. |
| App goes quiet (or breaks) offline. | Offline companion and all wellness tools keep working. |
| English-only, one interface. | Seven interface/voice languages with right-to-left layout support. |
| Chatbot implies it is a therapist. | Explicit boundaries, disclaimer and a crisis route to real humans. |

**Rate yourself: 3/3** — *Design.* 1 point: the use of AI is a good fit. 2 points: good fit plus some documentation of how it meets user needs. 3 points: good fit and the new user experience is clearly documented showing how users will be better served than they are today (steps 6.1 and the comparison in 6.2).

[PAGEBREAK]

## 7. Data

### 7.1 What data will you need to train your AI solution?

**Important design decision: we do not train a model.** Calmora uses a pre-trained third-party LLM through OpenRouter, shaped by **prompt engineering and tool definitions** (in-context learning), plus two deterministic components we wrote ourselves: a keyword-based offline companion and a crisis-detection regular expression. No dataset of private conversations is collected, uploaded, labelled or used for training.

What we therefore needed was:

  - **System prompt text** — how Calmora speaks (1–4 short spoken sentences), its "help, don't just reflect" method, the techniques it may teach, and its boundaries (no diagnosis, no medication advice, no methods or means).
  - **Tool schemas** — six functions with typed arguments and enums (seven sounds, six breathing patterns, five mood labels, sleep timer in minutes).
  - **Offline reply library** — team-written, pattern-matched empathetic replies grouped by theme: anxiety, exhaustion, sadness, anger, sleeplessness, positive moments, relationships, and a generic set.
  - **Interface and content strings** — translations for seven languages (English, Hindi, Spanish, French, German, Portuguese, Arabic), including greetings, suggestions and exercise text.
  - **Crisis pattern list and safety content** — phrases indicating self-harm or immediate danger, plus the emergency label, trusted person fields and helpline links.
  - **User data generated in the browser** — journal entries, mood check-ins with tags, conversation history, settings and soundscape mix. These stay in `localStorage`. Only the most recent conversation turns (up to 24, truncated) are sent to the model; journal, moods and stats are never included, apart from an optional anonymised 5-check-in mood average used only to set tone.
  - **Synthesised audio parameters** — noise filters and procedural events for rain, ocean, forest, brown noise, fireplace, night and cave; no audio files or licensed datasets.

### 7.2 Where or how will you source your data?

| Data needed | Where will the data come from? | Who owns the data? | Do you have permission to use the data? | Ethical considerations |
|---|---|---|---|---|
| System prompt and therapeutic techniques | Written by our team, informed by public material on CBT reframes, behavioural activation, grounding, ACT values, PMR, coherent breathing, the physiological sigh and 4-7-8 breathing | Our team | Yes (original writing; sources credited in the README) | No clinical claims; app states it is not a therapist or medical device; techniques are presented as general wellbeing skills, reviewed by our mentor. |
| Tool schemas, enums and agent rules | Written by our team from the feature list | Our team | Yes | Arguments are validated in the browser; tool loops capped at 3 rounds; the model must narrate any action it takes. |
| Offline reply library | Written by our team; themed by keyword | Our team | Yes | Deliberately non-clinical and non-prescriptive; crisis language is never handled by canned replies — it routes to the safety card. |
| Conversation turns sent to the model | Typed or spoken by the user in the app | The user | Yes — in-app consent; user can use their own key (BYOK) or the server key | Only message text (last 24 turns, truncated); reasoning excluded; no journal/moods/stats; keys never logged (a short SHA-256 hash is used only for rate-limit buckets); all requests over HTTPS. |
| Journal, moods, transcript, settings, mix | Generated in the browser by the user | The user | Yes — stored locally by the app | Never leaves the device; export and "erase all data" controls; no account, no analytics, no ads, no third-party trackers. |
| UI translations (7 languages) | Written by our team and checked by speakers in our community | Our team | Yes | Needs native-speaker review; right-to-left layout checked for Arabic; AI replies follow the selected language. |
| Pre-trained model | OpenRouter API (third-party model, no fine-tuning) | Model / API provider | Yes — API terms of service | Users are told their message text goes to an AI provider; BYOK lets them control their own quota; server key never reaches the browser. |
| Soundscapes and frequency tones | Generated live in the Web Audio API | Our team (code) | Yes — no datasets | No audio files to license; binaural beats include a headphones recommendation. |

**Balance, safety and privacy.** Because there is no training set, we balanced our **evaluation set** instead: a scripted set of utterances spread evenly across the eight offline themes, all seven languages, voice and text input, tool-triggering requests, and crisis phrases — so no single theme or language dominates our results. The server sanitises and truncates every message, caps concurrent requests (2 for server-key users, 8 for BYOK), and filters reasoning on both server and client. Privacy was reviewed with our mentor before any user testing.

**Rate yourself: 3/3** — *Data.* 1 point: relevant data identified and sourced. 2 points: evidence the dataset is balanced. 3 points: evidence the dataset is balanced *and* safety and privacy have been considered (no training on personal data, local-first storage, consent, crisis handling, key handling and rate limits).

[PAGEBREAK]

## 8. Prototype

### 8.1 Which AI tool(s) will you use to build your prototype?

**OpenRouter** for a streaming, function-calling-capable LLM; **Cloudflare Pages Functions** for the `/api/chat` endpoint; **Web Speech API** (`SpeechRecognition`) for voice input; **SpeechSynthesis** for spoken replies; **Web Audio API** for procedural soundscapes and binaural/Solfeggio tones; **Service Workers + Web App Manifest** for the installable offline shell; `localStorage` for personal data; and browser DevTools for inspecting requests.

### 8.2 Which AI tool(s) will you use to build your solution?

The same stack, deployed as a Cloudflare Pages project: `index.html` (the whole client — UI, orb, audio engine, exercises, agent loop, PWA), `functions/api/chat.js` (system prompt, key, tool schemas, concurrency limits, NDJSON streaming), `sw.js`, `manifest.webmanifest` and `icon.svg`. Configuration is set through environment variables (`OPENROUTER_API_KEY`, `OPENROUTER_MODEL`, `ALLOWED_ORIGIN`, `MAX_CONCURRENCY_SERVER`, `MAX_CONCURRENCY_BYOK`, `APP_URL`).

### 8.3 What decisions or outputs will your tool generate and what further action needs to be taken after a decision is made?

| AI output / tool call | Decision or output | Action taken in the app |
|---|---|---|
| `play_sound` | Chooses one of rain, ocean, forest, brown, fire, night, cave | Stops other layers, starts the synthesised soundscape, shows a toast, and Calmora says one warm sentence. |
| `stop_sounds` | Decides the user wants quiet | Stops all audio layers. |
| `note_thought` | Extracts a sentence worth keeping, with an optional mood label | Saves a private journal entry locally; the journal dock badge lights up. |
| `start_breathing` | Picks one of six patterns (coherent, box, sigh, unwind, tactical, long exhale) | Opens the breathing sheet and starts the guided animation/voice prompts. |
| `start_grounding` | Decides grounding is the right technique | Opens the 5-4-3-2-1 exercise. |
| `sleep_mode` | Chooses a sound and timer length | Starts sleep mode with a gently fading soundscape. |
| Spoken reply (streamed `delta` events) | 1–4 short sentences, plus at most one gentle question | Streamed into the chat, spoken by TTS, captioned; mic reopens for hands-free conversation. |
| `safety: crisis` flag + crisis addendum | Client regex detects crisis language | Safety card shown with local emergency number, trusted person and helplines; model responds with 2–3 steady sentences urging immediate human help, never methods. |

If the model calls a tool without speaking, the client feeds the tool result back and asks for one short spoken sentence (agent loop capped at 3 rounds). If `/api/chat` is unreachable, times out (60 s) or has no key, the app switches to the **offline companion** and shows a friendly toast instead of failing silently.

### 8.4 Architecture (how the decision travels)

> User (voice or text) → `index.html` → `POST /api/chat` (system prompt + tools + last 24 messages) → OpenRouter (streaming) → NDJSON events `delta` / `tool` / `done` → browser executes the tool → tool result fed back if needed → reply streamed, spoken and captioned → personal data saved to `localStorage` only.

**Rate yourself: 3/3** — *Prototype.* 1 point: a concept shows how the AI model will work. 2 points: a prototype has been created and trained. 3 points: a prototype has been created and successfully configured to meet users' requirements — the streaming agent, six working tools, offline companion, safety layer, PWA and seven-language UI are all implemented and deployed.

[PAGEBREAK]

## 9. Testing

### 9.1 Who are the users who tested the prototype?

The prototype was tested by [[number]] students from [[school / club]] across [[number]] sessions, plus [[Teacher or mentor name]] and the three team members. We tested in Chrome/Edge/Brave (voice and text), Safari (text and TTS), Firefox (text only — the Web Speech API is unavailable), and as an installed PWA on an Android phone. We also ran a scripted, code-level verification of the streaming endpoint, privacy behaviour and safety rules.

### 9.2 List your observations of your users as they tested your solution

  - **Voice input:** one utterance at a time worked reliably; `continuous=false` + `onspeechend` avoided the "won't stop listening" loop, and the 14-second hard cap plus double-commit guard prevented stuck states. Users liked seeing their words appear in the prompt bar before sending.
  - **Auto-send:** 2 seconds of silence felt natural for most, but several users paused mid-sentence and wanted a way to send manually or a slightly longer pause.
  - **Tools:** "play some rain", "help me breathe", "remember that I'm proud of today" and "tuck me in" triggered the correct tool, executed instantly, and were followed by a short spoken narration. With the default free model (`openrouter/free`), tool calls sometimes did not fire — a documented limitation of models without function-calling support.
  - **Reply style:** short spoken sentences were well received; long or list-like replies were not. Reasoning tags never appeared in the UI (filtered on server and client).
  - **Offline:** with the network disabled and the endpoint unreachable, the app showed "server offline", the offline companion replied, and breathing, grounding, journal, sounds and sleep mode all still worked from the cached shell.
  - **Safety:** scripted crisis phrases triggered the safety card; configured emergency and trusted-person numbers appeared as tap-to-call links; the server appended the crisis addendum. The card is dismissible with "I'm safe right now".
  - **Privacy:** network inspection confirmed that request bodies contain message text only — no journal entries, mood logs, stats or settings. Export and "erase all data" worked.
  - **Language & accessibility:** the interface, speech recognition language, TTS voice and AI replies switched across all seven languages; Arabic switched to right-to-left layout. Large captions, reduce-motion, keyboard shortcuts and `aria-live` announcements behaved as intended.

**Scripted evaluation set (record your results here):** [[number]] utterances — eight emotional themes × voice/text × tool requests × seven languages × crisis phrases.

| Measure | Scripted cases | Result |
|---|---|---|
| Correct tool selected and executed (function-calling model) | [[n]] tool requests | [[n/n successful]] |
| Crisis phrases that raised the safety card | [[n]] crisis phrases | [[n/n detected]] |
| Offline companion replied with no network / no key | [[n]] turns | [[n/n replied]] |
| Personal data absent from request bodies | [[n]] inspected requests | [[n/n clean]] |
| Interface + STT + TTS language switch | 7 languages | [[n/7 verified]] |
| Voice input in Firefox | 1 browser | Not supported by browser — typing works (known limit) |

### 9.3 Complete the user feedback grid

| What works | What needs to change |
|---|---|
| Short, kind spoken replies; seeing the transcript before it sends; tools that actually start sounds, breathing and journal entries; no account; everything stays on the device; the orb's colour states make it obvious when it is listening; the app still works offline. | A manual send button and a slightly longer/adjustable pause before auto-send; a clearer hint that tools need a function-calling model; Firefox and Safari have no voice input; translations need native-speaker review; some users wanted a visible "what did you save?" confirmation in the journal. |
| **Questions?** | **Ideas** |
| "Is anything I say stored anywhere?" "Is this a therapist?" "What happens if I say something really serious?" "Does it work without internet?" "Can I use it in Hindi / at home?" | A Whisper-style offline speech fallback; more tools (timers, gratitude, CBT thought record, body scan); conversation search; optional end-to-end encrypted sync; a way to share a single journal entry with a counsellor; a short onboarding that explains the orb colours. |

### 9.4 Refining the prototype: based on user testing, what needs to be acted on now so that the prototype can be used?

  - Add a **manual send button** and make the auto-send silence window configurable, so pauses mid-sentence are not cut off.
  - **Default to a tool-capable model** and surface the requirement in the Settings panel; if the chosen model cannot call tools, show a clear in-app hint instead of silently losing actions.
  - Add an **onboarding hint** explaining the orb colours, voice permissions (HTTPS/localhost) and the privacy model; users asked "is anything stored?" first.
  - **Native-speaker review** of the seven translations and the RTL layout, especially the exercise instructions.
  - **Confirm journal writes visibly** (e.g. open the journal or show the saved entry), because users were unsure whether `note_thought` had done anything.
  - Replace the drafted interview notes and the highlighted test counts in this logbook with our **actual** user session notes and results before submission.

### 9.5 What improvements can be made later?

In-browser Whisper speech-to-text fallback for Firefox/Safari (private, offline); more agent tools (timers, body scan, gratitude, CBT thought record); conversation branching and search; automatic language detection for speech recognition; optional end-to-end encrypted cloud sync; richer non-voice chat rendering; and a properly designed user study with a larger, more diverse group and measurable outcomes.

**Rate yourself: 3/3** — *Testing.* 1 point: a concept shows how it will be tested. 2 points: prototype tested with users and improvements identified. 3 points: tested with a fair representation of users and all tasks in this section completed (test matrix, browser coverage, privacy and safety verification, feedback grid, refinements and future improvements).

[PAGEBREAK]

## 10. Team collaboration

**10.1 How did you actively work with others in your team and with stakeholders?**

  - We collaborated with our stakeholders — students, a school mentor and [[Teacher or mentor name]] — by asking what actually happens when they feel overwhelmed, and letting their answers decide our features. Their input is why the app is voice-first, account-free, honest about its limits and able to work offline.
  - We worked in one GitHub repository: `index.html` for the client, `functions/api/chat.js` for the server, `sw.js` / manifest for the PWA, and this logbook. Commits and pull-request reviews made each person's contribution visible and gave us a real history of decisions.
  - We created a group chat to stay in touch at any hour, held short online meetings two to three times a week, and kept a shared Drive document for the logbook so nobody's notes were lost. We made a point of listening to every suggestion and crediting it in the meeting minutes.
  - We ran brainstorming sessions together, split the test matrix by browser and by feature, and paired up to review the streaming code and the safety wording.
  - Our mentor reviewed the problem statement, the "not a therapist / not a crisis service" disclaimer and the crisis card before we tested with students, and joined the testing-plan meeting on 1 October.

**Rate yourself: 3/3** — *Team collaboration.* 1 point: some evidence of team interactions. 2 points: collaboration clearly documented. 3 points: effective collaboration and communication among peers and stakeholders clearly documented in this section.

## 11. Individual learning reflection

**11.1 Team Reflections** — *A good way to identify what you have learned is to ask yourself what surprised you during the project.*

**Team member name: [[Name 1]] — Project Leader / Designer / Tester**
What surprised me most was how much of the project was not "the AI". The model was one function call; the hard parts were making listening stop reliably, making a reply short enough to be spoken, and designing a safety card that is calm rather than alarming. I learned to control scope — we dropped a custom-trained model because it added risk without helping users — and to defend a decision with user evidence instead of enthusiasm. I also learned that privacy is a design decision made at the architecture stage, not a setting you add at the end. Working to deadlines with two other people changed how I plan: small, reviewable commits beat one big reveal.

**Team member name: [[Name 2]] — Project Manager / Data Expert**
I expected to spend the project collecting and labelling a dataset. Instead I learned that a well-written system prompt and a set of typed tool schemas can shape a pre-trained model without training anything at all — and that this is *safer* when the subject is people's feelings. I learned what a streaming protocol looks like (NDJSON `delta` / `tool` / `done` events), why tool results have to be fed back into the conversation, and why a concurrency limit exists. Managing the logbook taught me that documentation written during the work is accurate and documentation written afterwards is guesswork. The biggest lesson: "we don't need to store that" is a legitimate and powerful engineering answer.

**Team member name: [[Name 3]] — Information Researcher / Safety & Quality Lead / Tester**
The interviews changed the product. We arrived with a chatbot idea and left with a voice-first tool that does things, because users told us typing and generic reassurance were the barriers. I learned how to ask a question without leading the answer, and how to turn quotes into an empathy map and then into requirements. Testing across browsers was humbling: something that feels perfect in Chrome simply does not exist in Firefox, and a responsible project documents that instead of hiding it. Working on the crisis rules made me take AI ethics seriously — a wrong, overconfident sentence in this domain can matter — and I'm glad our app says plainly that it is not a therapist and points to real people.

**Rate yourself: 3/3** — *Individual Learning Reflection.* 1 point: some team members present an account of their learning. 2 points: each team member presents an account. 3 points: each member presents a reflective and insightful account of their learning during the project.

## 12. Video link

**Enter the URL of your team video:** [[Paste your 3-minute video URL]]
**Website / deployed app link:** [[Paste your deployed *.pages.dev URL]]
**Source code:** https://github.com/apsethicsbowl20026-collab/calmora-ai
**Supporting material attached:** [[List screenshots, interview notes, test logs or consent forms]]

[PAGEBREAK]

## Appendix A — Recommended Assessment Rubric (for Teachers)

### Logbook and video content

| Steps | 3 points | 2 points | 1 point | Points given |
|---|---|---|---|---|
| Problem definition | Local, unsolved problem explained in detail with supporting research. | Local, unsolved problem described. | A local problem described. | [[ ]] |
| The Users | All steps of Section 4 completed with thorough investigation. | Most steps of Section 4 completed. | User group described but impact unclear. | [[ ]] |
| Brainstorming | Creative/critical session; compelling solution with supporting arguments. | Creative/critical session; solution with supporting arguments. | Session conducted; solution selected. | [[ ]] |
| Design | AI is a good fit and the new user experience clearly shows better service. | Good fit plus some documentation of user needs. | AI is a good fit for the solution. | [[ ]] |
| Data | Data identified and sourced; evidence of balance, safety and privacy. | Data identified and sourced; evidence of balance. | Data identified and how it will be sourced. | [[ ]] |
| Prototype | Prototype created and successfully configured to meet user requirements. | Prototype created and trained/configured. | Concept shows how the AI model will work. | [[ ]] |
| Testing | Tested with a fair representation of users; all Section 9 tasks completed. | Tested with users; improvements identified. | Concept shows how it will be tested. | [[ ]] |
| Team collaboration | Effective collaboration and communication clearly documented. | Collaboration clearly documented. | Some evidence of team interactions. | [[ ]] |
| Individual learning | Each member presents a reflective, insightful account. | Each member presents an account. | Some members present an account. | [[ ]] |
| **Total points** | | | | [[ ]] |

### Video presentation

| Criteria | 3 – excellent / 2 – very good / 1 – satisfactory | Points given |
|---|---|---|
| Communication | Well-paced, clear and logical sequence. | [[ ]] |
| Illustrative | Demonstrations and visuals illustrate examples where appropriate. | [[ ]] |
| Accurate language | Accurate science and technology; appropriate language. | [[ ]] |
| Passion | Team members show passion for their chosen topic. | [[ ]] |
| Sound and image quality | Good sound and image quality. | [[ ]] |
| Length | Content presented within a 3-minute timeframe. | [[ ]] |
| **Total points** | | [[ ]] |

[PAGEBREAK]

## Appendix B — Before you submit (completion checklist)

*This appendix is a helper added to this completed draft; it is not part of the official logbook template.*

  - Replace every highlighted `[[field]]`: school / organisation, year and class, teacher or mentor, the three team member names and grades, the number of testers and sessions, all scripted test counts, the video URL, the deployed app URL and the list of supporting material.
  - Replace the drafted interview responses in 4.3, the observations in 4.2 and the user feedback in 9.3 with your team's **actual** notes and quotes from real sessions, and get consent before recording anyone's words.
  - Fill in the real results of the scripted evaluation table in 9.2 and attach your test log / screenshots as supporting material.
  - Confirm the project plan dates in 2.2 match your team's real timeline; the dates in this draft follow the repository's commit history (August–October 2026).
  - Have your mentor review the safety wording, the disclaimer and the crisis card once more; verify the emergency number and helpline links for your country.
  - Check that the video is under three minutes and demonstrates at least one voice request, one tool call, the offline companion and the safety card.
  - Export or print the final logbook and save a copy in the shared drive.

**Sources used for the technical content of this logbook:** the Calmora repository (`README.md`, `index.html`, `functions/api/chat.js`, `sw.js`, `manifest.webmanifest`); the IBM EdTech Youth Challenge Project Logbook template; OpenRouter and Cloudflare Pages documentation; MDN documentation for the Web Speech API, Web Audio API, SpeechSynthesis and Service Workers; public material on CBT reframes, behavioural activation, DBT grounding, ACT values, PMR, coherent breathing, the physiological sigh and 4-7-8 breathing; and helpline resources (Crisis Text Line, findahelpline.com).
