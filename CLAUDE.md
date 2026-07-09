# CHH Cortex — Claude Code Instructions

This is the CHH Cortex lite vault for Johns Hopkins Center for Humanitarian Health.

## Startup reads

1. `ENTRY.md`
2. `wiki/partnerships/chh.md`
3. `_system/CHH-INSTALL.md` (when setting up)

## Mandatory route line

For substantive tasks, begin with:

**Cortex route:** [primary skill] → [vault paths]

## Skills

| Task | Skill |
|------|-------|
| Setup / onboarding | `skills/chh-onboarding/SKILL.md` |
| Grant writing | `skills/grant-writer/SKILL.md` |
| Grant red-team | `skills/grant-red-team-reviewer/SKILL.md` |
| Transcript triage | `skills/transcript-triage/SKILL.md` |
| Knowledge updates | `skills/knowledge-curator/SKILL.md` |
| Routing | `skills/context-navigator/SKILL.md` |

## Active proposal workbench

When user says **I am working on [proposal]** under `raw/proposals/`:

1. Read package `README.md`, `DECISION-CHART.md`, `DONOR-DOSSIER.md`, `REVISION-LOG.md`
2. Run grant-writer + red-team before paste-ready output

## Guardrails

- Do not invent donor criteria, deadlines, or impact claims
- Mark unsupported claims `verify` or `needs source`
- No PII/PHI in vault writes
- Do not write outside this repo

## Plugin

Install `chh-cortex-code` plugin for skill discovery in Claude Code.
