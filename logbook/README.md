## New evidence supplement — 4 November 2026

- [Test logs and interview notes — PDF](PRIMOSHU-Test-Logs-and-Interview-Notes.pdf)
- [Editable Word copy](PRIMOSHU-Test-Logs-and-Interview-Notes.docx)
- [Markdown source](PRIMOSHU-Test-Logs-and-Interview-Notes.md)
- [Captured automated test output](evidence/automated-tests-2026-11-04.txt)
- [Run metadata and file checksums](evidence/run-metadata-2026-11-04.json)

This supplement records a fresh **12/12 automated test pass**, one requester's
written feedback, unexecuted manual-test plans, and an unfilled interview sheet.
It is **not evidence of newly conducted participant interviews**. The original
logbook's drafted interview dialogue and unverified human-testing statements must
not be treated as measured results. See the supplement's submission guidance.

To rebuild just the supplement (leaving the original exports unchanged):

```bash
python -m venv .venv
.venv/bin/pip install python-docx reportlab
.venv/bin/python logbook/build_evidence.py
```

The PDF export uses the system DejaVu fonts, as does the existing builder.

---

# Calmora — AI Project Logbook

A completed **AI Project Logbook** for this repository, following the structure of the
IBM EdTech Youth Challenge logbook template (the "PLASTIX" example PDF): the same
12 numbered sections, team roles, project plan, communications plan, meeting
minutes, empathy map, priority grid, data table, prototype, testing, reflections,
video links and the teacher assessment rubric — but filled in for **Calmora**.

## Deliverables

| File | What it is for |
|---|---|
| [`CALMORA-AI-Project-Logbook.pdf`](../CALMORA-AI-Project-Logbook.pdf) | Submission-ready, 22 pages, print/export exactly as it looks. |
| [`CALMORA-AI-Project-Logbook.docx`](../CALMORA-AI-Project-Logbook.docx) | Editable Word copy — the one to put in the shared drive and work on as a team. |
| [`CALMORA-AI-Project-Logbook.md`](CALMORA-AI-Project-Logbook.md) | Plain-text source of truth, easy to review in Git and diff. |
| `build.py` | Regenerates the `.docx` and `.pdf` from the Markdown source. |

## Regenerate after editing

```bash
pip install python-docx reportlab     # one time
python3 logbook/build.py
```

The Markdown syntax is intentionally small: `#`–`####` headings, `-` bullets
(indent by two spaces for sub-bullets), `1.` numbered items, `| pipe | tables |`
(first row = header, second row = `|---|`), `> callouts`, and `[PAGEBREAK]`.
Inline: `**bold**`, `*italic*`, `` `code` ``, `[label](url)` and `[[fields]]`.

## Highlighted `[[fields]]`

Anything the team has to supply personally is highlighted in **yellow** in both
the Word and PDF versions: school / class / year, teacher or mentor name, the
three team member names and grades, tester counts, scripted test results, the
video URL, the deployed app URL and the list of supporting material.

`Appendix B — Before you submit` is a checklist of those fields. It also asks you
to replace the *drafted* interview quotes (4.3), observations (4.2) and user
feedback (9.3) with your team's real notes, and to fill in the real numbers in
the evaluation table (9.2). Those parts were drafted from this repository's
README and code because they cannot be known from the source files — please do
not submit them as if they were measured results.

The project plan dates in section 2.2 follow this repository's real commit
history (created 11 August 2026, last updated 13 October 2026); change them if
your team's timeline differs.

## Where the technical content came from

`README.md`, `index.html`, `functions/api/chat.js`, `sw.js` and
`manifest.webmanifest` in this repository. Nothing about Calmora's architecture,
features, privacy model, safety behaviour or tools was invented — those entries
are descriptions of the code as it stands.
