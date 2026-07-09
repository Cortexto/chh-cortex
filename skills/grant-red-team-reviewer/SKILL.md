---
name: grant-red-team-reviewer
description: Critical review of CHH grant drafts, LOIs, and application answers before paste. Trigger on "red-team", "review this section", or before final grant-writer output.
---

# CHH Grant Red-Team Reviewer

Stress-test grant prose from a skeptical internal reviewer perspective — not polite proofreading.

## Required Reads

1. The current draft or grant answer
2. `skills/grant-writer/SKILL.md` when reviewing grant-writer output
3. `wiki/concepts/workflow/chh-grant-writing-process.md`
4. Package `raw/proposals/<slug>/DONOR-DOSSIER.md` when present — re-check kill list
5. `wiki/principles/chh-grant-voice.md`
6. `wiki/partnerships/chh.md` for pilot scope boundaries

## Review passes

### 1. Prompt fit

- Does the draft answer the exact question?
- Is the opening doing answer work, not mood-setting?

### 2. Donor truth

- Are eligibility, scale, and pathway claims sourced or marked `verify`?
- Does the draft mirror donor language from `DONOR-DOSSIER.md`?

### 3. Evidence honesty

- Flag overclaims, missing citations, and population statistics without source
- No clinical deployment claims without IRB frame

### 4. CHH pilot boundaries

- No PII/PHI
- No promises of Outlook/calendar auto-ingest (Hopkins IT limit)

## Output

Return revised prose plus one footer:

`Red-team pass applied: [changes made]`

Classify blockers explicitly when paste must not proceed.
