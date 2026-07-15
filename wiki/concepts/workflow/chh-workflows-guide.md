# CHH workflows guide

Step-by-step workflows for CHH Cortex. Skills implement these; this file is the map.

---

## 1 — Triage matrix (what to promote)

When triaging email or meetings, classify each unit:

| Label | Meaning | Usual destination |
|-------|---------|-------------------|
| `task` | Someone needs to act | Propose `TASKS.md` (curator approves) |
| `decision` | Choice was made | Workbench or `wiki/` |
| `project-fact` | Durable grant/partner fact | `wiki/` with source |
| `contact-intel` | Who is involved | People card update |
| `background` | Context only | Stay in `raw/` |
| `noise` | Low value | Stay in `raw/` only — **do not promote** |
| `verify` | Uncertain | Mark verify; do not promote |

**Score before wiki promotion:** Is it actionable, reusable, and source-backed? If not, keep in `raw/`.

**Freshness:** When a newer meeting or email supersedes an old wiki fact, curator **updates** the wiki row or marks old reasoning superseded — do not stack contradictory “current” facts.

---

## 2 — Email population

Full SOP: `wiki/concepts/workflow/chh-sop-email-population.md`

1. Curator selects grant-related threads only
2. Save to `raw/email/` per `raw/email/README.md`
3. Run `skills/chh-email-triage/SKILL.md`
4. Link to active workbench `REVISION-LOG.md` if relevant

---

## 2b — Meeting prep (no Outlook OAuth)

Full SOP: `wiki/concepts/workflow/chh-sop-meeting-prep.md` · Skill: `skills/chh-meeting-prep/SKILL.md`

---

## 2c — Fireflies landing

Full SOP: `wiki/concepts/workflow/chh-sop-fireflies-landing.md`

---

## 3 — Donor lens gate (before drafting)

Before external grant prose on a new RFP:

1. Open or create `raw/proposals/<slug>/DONOR-DOSSIER.md`
2. Fill **must-prove**, **kill list**, **reviewer tone**
3. Boot grant with **I am working on [slug]**
4. Do not paste-ready draft until dossier is at least `partial`

See demo: `raw/proposals/demo-lsri-workbench-2026/DONOR-DOSSIER.md`

---

## 4 — Portal paste gate (before each field)

For each donor portal question:

```
Field job: …
Reviewer check: …
Trap: …
```

Draft answer → red-team → human paste.

---

## 5 — Incoming thread read (before you reply)

When pasting PI feedback, reviewer comments, or partner email **before drafting a response**:

1. Read mechanism vs symptom — what is the real ask?
2. Separate **funder-facing** vs **internal-only**
3. Weight which 2–4 beats deserve space in the reply
4. Hand off to `grant-writer` or `knowledge-curator`

Do not promote negotiation intel or person-psychology profiles to wiki.

---

## 6 — Cross-tool continue (Claude + ChatGPT + folder AI)

When the same grant moves across tools:

1. Read `raw/proposals/<slug>/REVISION-LOG.md` + `DECISION-CHART.md`
2. Optional: `REVIEW-LEDGER.md` for session notes
3. Say **continue [slug]** — assistant reads files before drafting

**Git handles collisions** — ledgers are coordination records only (not locks, not model telemetry). Full guardrails: `CHH-DECISIONS.md` CD-005 · skill: `skills/chh-cross-tool-ledger/SKILL.md`

---

## Source(s)

- CHH Cortex lite export template
- Adapted from HERA triage and grant process patterns (not shipped to CHH)
