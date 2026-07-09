---
name: transcript-triage
description: Classify pasted meetings, emails, or notes into tasks, decisions, and wiki candidates for CHH vault.
---

# CHH Transcript Triage

Use when landing material in `raw/meetings/` or `raw/email/`.

## Required Reads

1. `CORTEX.md`
2. `wiki/partnerships/chh.md`

## Workflow

1. Normalize names and org terms
2. Classify units: task, decision, project-fact, contact-intel, background, noise, verify
3. Propose `TASKS.md` updates — curator approves before write
4. Propose `wiki/` promotions with `Source(s)` — no PII/PHI

## Guardrails

- Keep raw file intact (append-only)
- Do not promote negotiation intel or person-observation patterns
- Mark uncertainty as `verify`
