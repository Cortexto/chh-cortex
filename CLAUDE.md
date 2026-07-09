# CHH Cortex — AI workspace guide

Instructions for any AI assistant working inside this vault (folder-mounted chat, coding workspace, or equivalent).

**First session with a new user:** offer `skills/chh-onboarding/SKILL.md` before anything else.

## How to open this vault

1. **Non-technical users** — sync or download the folder (see `_system/CHH-INSTALL.md` Track A), mount it in your organization's approved AI tool, then read `ENTRY.md`.
2. **Technical owner** — clone from GitHub, open the repo root as the workspace, then read `ENTRY.md`.

Do not require a specific vendor product name in user-facing setup docs.

## Startup reads

1. `ENTRY.md`
2. `wiki/partnerships/chh.md`
3. `_system/CHH-INSTALL.md` (when setting up)
4. `_system/CHH-CAPABILITIES.md` (what is in scope for CHH vs HERA-maintained)

## Route line (for assistants)

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
