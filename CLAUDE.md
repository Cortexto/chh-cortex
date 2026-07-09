# CHH Cortex — Claude Instructions

This is the CHH Cortex lite vault for Johns Hopkins Center for Humanitarian Health.

## Works in

- **Claude desktop (Cowork)** — plug and play: add this folder to a Cowork session, then say *Read CLAUDE.md and get me started*. No terminal or git needed.
- **Claude Code** — open this folder as the workspace root; this file loads automatically.
- **Cursor** (optional) — same folder, same rules.

First session with a new user: offer `skills/chh-onboarding/SKILL.md` before anything else.

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

`chh-cortex-code` metadata lives at `.claude-plugin/plugin.json`. If local plugin install is unavailable, use the skill paths above directly.
