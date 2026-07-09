---
name: CHH Cortex — Entry Point
type: system
updated: 2026-07-09
---

# CHH Cortex — Start Here

Knowledge vault for Johns Hopkins Center for Humanitarian Health (CHH) grant and research packaging.

## Step 1 — Read these first

1. `CORTEX.md` — folder contract and guardrails
2. `wiki/partnerships/chh.md` — pilot scope, IT matrix, curator rules
3. `TASKS.md` — CHH team task list (empty template — fill locally)
4. `_system/CHH-CAPABILITIES.md` — feature map (lite vs HERA-maintained)

## Step 2 — Folder structure

```
chh-cortex/
├── ENTRY.md           this file
├── CLAUDE.md          AI workspace guide (for folder-mounted assistants)
├── raw/               source material (append-only)
├── wiki/              curated CHH knowledge
├── skills/            runnable workflows
└── _system/           install guides, adapters
```

## Step 3 — Invoke a skill

| Task | Skill |
|------|-------|
| First-time setup | `skills/chh-onboarding/SKILL.md` |
| Grant drafting | `skills/grant-writer/SKILL.md` |
| Grant review | `skills/grant-red-team-reviewer/SKILL.md` |
| Meeting triage | `skills/transcript-triage/SKILL.md` |
| Wiki promotion | `skills/knowledge-curator/SKILL.md` |
| Ambiguous routing | `skills/context-navigator/SKILL.md` |

## Example workbench

`raw/proposals/example-chh-rfp-2026/` — fictional RFP walkthrough (safe to share).

Say: **I am working on example-chh-rfp-2026** to boot the workbench files.

## Guardrails

- No PII/PHI in shared vault
- Human approval before paste-ready donor text
- Curator-owner for each pilot workflow
