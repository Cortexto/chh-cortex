---
name: CHH Cortex — Entry Point
type: system
updated: 2026-07-09
---

# CHH Cortex — Start Here

Knowledge vault for Johns Hopkins Center for Humanitarian Health (CHH) grant and research packaging.

## Step 1 — Read these first

1. **`CHH-ROADMAP.md`** — pain points, raw vs wiki, what is included, demo, phases
2. `CORTEX.md` — folder contract (short)
3. `wiki/partnerships/chh.md` — pilot scope and curator rules
4. `_system/CHH-INSTALL.md` — install (Track A = no terminal)
5. `_system/AGENTS-AND-SKILLS.md` — skill index

## Raw vs wiki (30 seconds)

- **`raw/`** = inbox (emails, meetings, drafts) — land first, don’t silently rewrite sources
- **`wiki/`** = approved facts — curator promotes from raw with sources

Details in `CHH-ROADMAP.md`.

## Step 2 — Folder structure

```
chh-cortex/
├── CHH-ROADMAP.md     pain points, demo, phases (read first)
├── ENTRY.md           this file
├── CLAUDE.md          AI workspace guide
├── raw/               source material (append-only)
├── wiki/              curated CHH knowledge
├── skills/            runnable workflows
└── _system/           install guide
```

## Step 3 — Invoke a skill

| Task | Skill |
|------|-------|
| First-time setup | `skills/chh-onboarding/SKILL.md` |
| Grant drafting | `skills/grant-writer/SKILL.md` |
| Grant review | `skills/grant-red-team-reviewer/SKILL.md` |
| Email triage | `skills/chh-email-triage/SKILL.md` |
| Meeting triage | `skills/transcript-triage/SKILL.md` |
| Wiki promotion | `skills/knowledge-curator/SKILL.md` |
| Ambiguous routing | `skills/context-navigator/SKILL.md` |

Workflows (portal gate, donor lens, cross-tool ledger): `wiki/concepts/workflow/chh-workflows-guide.md`

## Demo workbench (learn the routes)

`raw/proposals/demo-lsri-workbench-2026/` — **sanitized walkthrough** of a JHU-style grant package (not a live submission).

Say: **`I am working on demo-lsri-workbench-2026`**

Read `HOW-TO-USE.md` inside that folder first.

## Guardrails

- No PII/PHI in shared vault
- Human approval before paste-ready donor text
- Curator-owner for each pilot workflow
