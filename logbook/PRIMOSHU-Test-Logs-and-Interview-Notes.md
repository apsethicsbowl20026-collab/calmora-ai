# PROJECT LOGBOOK EVIDENCE PACK
## PRIMØSHU by Calmora

**Test logs • stakeholder feedback notes • future interview protocol**

**Prepared:** 4 November 2026 • **Version:** 1.0

### Evidence statement

This supplement contains one freshly executed automated test run and notes extracted from the project requester's feedback in this conversation. It does not contain newly conducted interviews, clinical findings, or measured user-satisfaction results.

The feedback source is one project requester. Their age, school, occupation, clinical status and relationship to the intended end-user population are unknown. No broader sample or representativeness is claimed.

| Evidence type | What is available | How to use it |
|---|---|---|
| Executed technical tests | 12 automated tests passed on 4 November 2026 | Evidence for selected implementation behavior under mocks |
| Stakeholder review | Recorded requests about voice interaction, appearance, API constraints and naming | Evidence of this requester's priorities, not population-level needs |
| Human usability sessions | No newly conducted sessions in this task | Use the blank protocol to collect real observations |
| Historical browser checks | Earlier conversation reports checks at five viewport widths | Historical context only; not rerun or counted in this test log |

### Evidence index

- E-01: `logbook/evidence/automated-tests-2026-11-04.txt` — complete captured test-run output.
- E-02: `logbook/evidence/run-metadata-2026-11-04.json` — timestamps, branch, revision, environment and exit code.
- E-03: `tests/workspace.test.js` — executable test procedures and assertions.
- E-04: This conversation — the source of the stakeholder quotations in Section 4; no independent interview recording is attached.

**Submission rule:** keep the distinction between executed results, recorded feedback, interpretation and planned work. Do not replace missing human evidence with invented responses.

[PAGEBREAK]

## 1. Executed test log

**Run ID:** TL-2026-11-04-01

| Field | Recorded value |
|---|---|
| Test date | 4 November 2026 |
| Start | 08:20:24 UTC / 13:50:24 IST |
| End | 08:20:30 UTC / 13:50:30 IST |
| Branch | arena/21394eaf-calmora-ai |
| Revision tested | e7ed404594173f266fd72c0ad5a2ba54db94e902 |
| Runner | Agent-executed Node.js test runner; no human participant |
| Environment | Linux x86_64; Node v22.22.3; npm 10.9.8; jsdom |
| Preparation | npm ci |
| Execution command | npm test |
| Recorded suite duration | 6804.048796 ms, as reported by Node; not conversational latency |
| Result | 12 passed; 0 failed; 0 cancelled; 0 skipped; 0 todo |
| Process exit code | 0 |

### Setup issue and resolution

**SETUP-01 — dependency missing.** The initial attempt to run `npm test` failed before feature tests could execute because `jsdom` was not installed in this checkout. The runner reported `ERR_MODULE_NOT_FOUND`. This was a local setup failure, not an observed voice or UI defect.

**Action:** ran `npm ci` using the committed lockfile. Installation completed successfully. The subsequent fresh run passed all 12 tests. E-01 records the successful run; the earlier failure is summarized here from the tool output, not supplied as a separate raw log.

### Method and interpretation

Tests load the application into jsdom and simulate speech-recognition events, speech-synthesis callbacks, browser preferences and network responses. A pass means the asserted behavior occurred in that environment. It does not prove audible voice quality, real microphone release at OS level, actual provider response time, cross-browser compatibility, full accessibility conformance or wellbeing improvement.

No real OpenRouter key was supplied or live model call made for this run. The suite uses synthetic test inputs and a dummy key for its simulated direct-request case.

[PAGEBREAK]

## 2. Detailed test results

**Shared conditions:** TL-2026-11-04-01; E-01 output; E-03 procedures. All results below are automated, not human observations. Source line numbers refer to the tested revision.

| ID / source line | Procedure and expected result | Recorded result |
|---|---|---|
| T-01 / 39 | Boot workspace; toggle hands-free; select Good mood; open Settings and Breathing. Expect five navigation items, saved controls, mood level 4 and visible dialogs without runtime errors. | PASS |
| T-02 / 58 | Omit speech recognition and start a call. Expect the text input to receive focus and an actionable unsupported-voice message. | PASS |
| T-03 / 68 | Start, end and restart listening; deliver old-recognizer events. Expect idle after end and no stale transcript in the new session. | PASS |
| T-04 / 89 | Simulate recognizer ending during silence, then mute, unmute and hang up. Expect reconnection, changed recognizer on unmute and hidden call UI after hang-up. | PASS |
| T-05 / 112 | Emit a microphone-permission-denied event. Expect the call to end and permission-recovery guidance to appear. | PASS |
| T-06 / 122 | Inspect application source for the removed speech endpoint, provider controller and extra key setting. Expect those specific integration markers to be absent. | PASS |
| T-07 / 128 | Simulate a spoken turn and streamed reply; inject matching echo, then a distinct phrase. Expect echo rejection, interruption, a second request and the same ongoing call. | PASS |
| T-08 / 160 | Supply a dummy browser OpenRouter key and mock streamed output. Expect a direct OpenRouter completion URL, a system message, six tool definitions and queued speech. | PASS |
| T-09 / 177 | Boot with no saved theme and a light OS preference. Expect dark theme state, dark color-scheme, matching theme-color metadata and Dark selected. | PASS |
| T-10 / 188 | Change header appearance to Light, then settings to Dark. Expect both selectors and storage to agree; OS changes must not override an explicit choice. | PASS |
| T-11 / 204 | Restore System preference and simulate OS changes; also restore a saved Light choice. Expect resolved themes to follow the selected policy and reject an invalid preference. | PASS |
| T-12 / 216 | Calculate contrast for seven predefined foreground/background pairs. Expect each ratio to meet the 4.5:1 normal-text threshold. | PASS |

**Limits of individual passes:** T-06 is a targeted source check, not a full network/security audit. T-08 checks request construction with mocked output, not real tool selection or execution by OpenRouter. T-09 checks early DOM theme state, not physical-screen flash. T-12 covers specified color pairs only, not every rendered control or a complete WCAG audit.

[PAGEBREAK]

## 3. Follow-up tests and acceptance criteria

All cases in this section are **NOT RUN** in this task. Assign an owner and record actual results before marking them complete.

| ID | Planned procedure | Proposed acceptance criterion |
|---|---|---|
| M-01 | On Chrome/Edge over HTTPS, grant permission and hold a three-turn conversation with headphones. | Each utterance is captured once; replies are audible; listening resumes without a new start tap. |
| M-02 | During playback, try a distinct phrase and then the explicit interrupt button. Repeat with speakers and headphones. | The button stops playback reliably. Record spoken-interruption successes and echo failures separately; do not claim perfect barge-in. |
| M-03 | Inspect browser and OS microphone indicators while muting, unmuting, hanging up and backgrounding. | Mic access stops when intended; no late playback or transcript after call termination. |
| M-04 | Use a real authorized OpenRouter configuration and a tool-capable model for rain, journaling and breathing requests. | The intended tool runs and the assistant describes the actual action. Record model ID, failures and request evidence with secrets redacted. |
| M-05 | Measure end-of-user-speech to first audible reply across at least ten turns on a named device/network. | Report individual timings, median and range. Set a target before the study; no latency measurement is available yet. |
| M-06 | Reload in Dark, Light and System on real mobile and desktop browsers; exercise controls at 200% zoom. | No unintended light flash in Dark; visible focus; no clipped essential controls. Record devices and screenshots. |
| M-07 | Test keyboard-only navigation, a screen reader and reduced-motion mode, including dialogs and call controls. | Controls are named, focus is usable, state changes are understandable, and decorative motion can be disabled. |
| M-08 | Test offline shell, journal export/deletion, network payloads and safety prompts in a safe scripted session. | Document what is sent or stored, tool availability, and actual safety behavior; do not infer these from automated passes above. |

### Manual session record

**Session ID:** [[ID]] • **Date/time/time zone:** [[record]] • **Tester code:** [[code, not full name]]

**Owner:** [[name]] • **Device/OS/browser:** [[record]] • **Network/audio setup:** [[record]]

**Build/model:** [[revision and model ID]] • **Case IDs:** [[IDs]]

**Steps performed:** [[record]] • **Expected result:** [[record before execution]]

**Actual result and evidence:** [[observations, redacted screenshot/log reference]]

**Outcome:** [[pass / fail / blocked / not run]] • **Severity and follow-up:** [[record]]

[PAGEBREAK]

## 4. Stakeholder feedback notes

**Record ID:** SF-01 • **Compiled:** 4 November 2026

**Method:** retrospective extraction from asynchronous written project feedback. This is not a newly conducted structured interview or a usability session.

**Source:** one project requester in this conversation. Review dates for individual messages were not independently recorded. No participant demographics, recruitment process, consent-to-research record or session recording are available. Do not relabel these notes as student, patient or school-community interviews.

### Recorded feedback and interpretation

| Ref | Recorded requester wording / decision | Interpretation, not a measured finding |
|---|---|---|
| F-01 | “Currently we are using oppenrouter, and Calmora still doesnt feels like a Voiuce agent does” | The requester saw a gap between voice-agent expectations and the earlier experience. This does not identify the exact cause or quantify usability. |
| F-02 | “no external api keys, only openrouter support” | Additional keyed speech-provider integrations are unacceptable to this requester. |
| F-03 | “make this a Full interactive voice agent as if i am talking to a person on phone” | A persistent, turn-taking call is the desired interaction model rather than repeated push-to-talk. |
| F-04 | “my eyes are FLASHED, please make a dark mode” | The requester reported brightness discomfort and explicitly requested dark mode. No illuminance, eye-health assessment or accessibility diagnosis was measured. |
| F-05 | “make the UI ABSOLUTELY MESMERISING” | Stronger visual refinement and atmosphere are priorities. The phrase is subjective, not an acceptance-test result. |
| F-06 | The requester selected “PRIMØSHU by Calmora” in the naming clarification. | Use PRIMØSHU as the product name with Calmora attribution; preserve existing internal keys for compatibility. |

**Quotation policy:** brief quotations retain the original wording, spelling and capitalization. They come from the project conversation, not invented interview answers. Use them within the team's logbook; seek permission before publishing identifiable conversation material outside that context.

### Feedback-to-action trace

- F-01/F-03 → persistent call controls, automatic listening, interruption and visible session status; simulated coverage in T-03, T-04 and T-07. Real conversation quality remains unverified here.
- F-02 → retain OpenRouter as the only keyed AI service; targeted tests T-06 and T-08. Browser recognition may still use browser-vendor infrastructure without an application API key.
- F-04 → dark-first appearance and a saved theme choice; coverage in T-09 to T-11. Reduced discomfort has not been measured.
- F-05 → Nightfall surfaces, typography, voice-orb treatment and restrained motion; T-12 checks key colors, not whether people find the interface beautiful.
- F-06 → product naming decision recorded. The current automated suite does not contain a dedicated branding test.

[PAGEBREAK]

## 5. Interview protocol for future evidence

**Status:** proposed; no responses have been collected using this protocol.

**Research question:** can intended users understand the call flow, control the microphone and comfortably use the interface without additional speech-service keys?

### Ethical setup

- Recruit voluntarily and record only a pseudonymous participant code. Obtain appropriate consent and, for minors, school/guardian permission as required by the organizer.
- Explain that PRIMØSHU is an AI wellbeing companion, not a person, therapist, medical service or crisis service. Do not ask for diagnoses or sensitive personal experiences.
- Use neutral, fictional prompts. Allow skipping any task and stopping at any time. Record audio or screenshots only with separate permission; do not include API keys.
- If a participant becomes distressed, stop the session and follow the institution's safeguarding process. Do not run crisis scenarios on a distressed participant.

### Suggested neutral tasks

1. Ask the participant to locate the voice-call control without help.
2. Use a fictional request such as planning a busy afternoon. Ask them to take two conversational turns.
3. Ask them to stop an answer, mute, unmute and end the call. Observe whether they can tell when the mic is active.
4. Ask them to choose a comfortable appearance setting and reload the app.
5. Ask them to find breathing or journaling using non-sensitive sample content.

### Interview questions — leave responses blank until collected

| Question | Response to record after the session |
|---|---|
| Before starting, what did you expect the call button to do? | [[verbatim response]] |
| At what points were you sure or unsure that the microphone was listening? | [[verbatim response]] |
| What happened when you tried to interrupt? | [[verbatim response]] |
| What, if anything, made the conversation feel awkward or natural? | [[verbatim response]] |
| How did the screen feel at your usual brightness? What would you change? | [[verbatim response]] |
| Which appearance setting would you keep, and why? | [[verbatim response]] |
| What do you think the app sends or stores? What remains unclear? | [[verbatim response]] |
| What is the one change that would most improve the experience for you? | [[verbatim response]] |

[PAGEBREAK]

## Interview session sheet — unfilled template

**Status:** not conducted. Complete only during an actual, consented session.

### Session notes

**Participant code / consent reference:** [[record]] • **Session date and facilitator:** [[record]]

**Relevant context:** [[device, environment, prior voice-app experience; avoid unnecessary personal data]]

**Observed behavior:** [[what happened; separate from your interpretation]]

**Direct quote:** [[exact words, with permission]] • **Interpretation:** [[tentative explanation]]

**Task completions / assistance / errors:** [[counts and details]]

**Suggested change:** [[record]] • **Evidence reference / owner / review date:** [[record]]

[PAGEBREAK]

## 6. How to add this evidence to the existing logbook

The existing main logbook contains drafted interview answers and prototype observations. This supplement does not validate those passages. Its purpose is to provide traceable evidence without presenting assumptions as research.

### Section 4 — The Users

Use Section 4 of this supplement as **stakeholder feedback from one project requester**, not as interviews with several students. Keep the future protocol separate until real sessions occur. Existing drafted dialogue in main-logbook Section 4.3 should be labeled illustrative or replaced with genuinely collected notes before submission.

### Section 9 — Testing

Attach E-01 and E-02. Use Sections 1 and 2 for the automated testing record and Section 3 for planned manual work. Do not state that 12 human participants were tested: the number 12 refers to automated tests. Student counts, school names and teacher participation remain unverified and must not be filled from this run.

### Suggested paste-ready technical result

“On 4 November 2026, we executed the project's Node.js/jsdom test suite. All 12 automated tests passed. Coverage included selected workspace controls, simulated voice-call transitions, microphone-error handling, direct OpenRouter request construction, appearance preferences and seven predefined text-contrast pairs. Speech and network responses were simulated; real-device conversation quality, live provider latency and broad accessibility conformance were not established by this run. The captured output and environment metadata are attached.”

### Suggested paste-ready feedback summary

“The project requester asked for a phone-like voice interaction, OpenRouter-only keyed integration, less screen brightness, a more refined interface and the name PRIMØSHU by Calmora. We used this recorded written feedback to prioritize call controls and dark-first appearance. These notes represent one stakeholder's preferences and are not evidence of clinical benefit or general user satisfaction.”

### Before submission

- Identify the team member who reviewed and takes responsibility for these records; do not invent an interviewer or evaluator name.
- Keep the original test output and metadata alongside any edited summaries.
- Replace the [[blank fields]] only after collecting the missing evidence.
- Label old drafted quotes and unverified device/privacy/safety claims accurately; this supplement is not a blanket confirmation of the original logbook.
- Re-run tests after code changes and store a new dated record rather than silently overwriting this result.
- Complete real-device sessions and document limitations and unsuccessful cases as well as successes.
