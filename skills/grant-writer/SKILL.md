---
name: grant-writer
description: CHH grant drafting — proposal workbench boot, donor dossier decode, section drafts with red-team gate. Triggers include "write this grant", "grant fit", "application answer", "I am working on [proposal]".
---

# CHH Grant Writer

Use for Johns Hopkins CHH grant packaging, RFP responses, and internal proposal drafts.

## Activation

Before drafting, identify:

- donor / program and deadline
- active workbench under `raw/proposals/<slug>/`
- voice register (faculty PI vs center admin)
- files you will read (list paths that exist in this repo)

Do not start with a generic draft.

## Required Reads

Read only what is relevant:

1. `CORTEX.md`
2. `wiki/partnerships/chh.md`
3. `wiki/concepts/workflow/chh-grant-writing-process.md`
4. `wiki/concepts/workflow/grant-proposal-workbench.md`
5. `wiki/concepts/workflow/chh-workflows-guide.md`
6. `wiki/principles/chh-grant-voice.md`
7. Package `raw/proposals/<slug>/DONOR-DOSSIER.md` when workbench active
8. Package `raw/proposals/<slug>/DECISION-CHART.md` when workbench active
9. Package `raw/proposals/<slug>/REVISION-LOG.md` when revising from human feedback
10. `TASKS.md` when checking CHH pipeline deadlines

## Workbench boot

When user says **I am working on [slug]**:

1. Open `raw/proposals/<slug>/README.md`
2. Read `DECISION-CHART.md`, `DONOR-DOSSIER.md`, `REVISION-LOG.md`
3. Emit boot summary: route locks, must-prove list, open blockers
4. Draft one section at a time unless user asks for full draft

## Workflow

1. Decode the donor question (field job, reviewer check, trap)
2. Draft section prose grounded in workbench files
3. Run `skills/grant-red-team-reviewer/SKILL.md` before paste-ready output
4. Log human feedback in `REVISION-LOG.md` — do not overwrite silently

## Guardrails

- No PII/PHI in shared vault
- No unsupported impact claims — mark `verify` or `needs source`
- Curator approval before paste-ready funder text
- Do not invent eligibility, deadlines, or budget numbers

## Output footer

External-facing grant outputs end with:

`Red-team pass applied: [brief note on changes]`
