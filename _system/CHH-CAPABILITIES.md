---
name: CHH Cortex — Capabilities map
description: What CHH lite includes vs what HERA maintains during pilot
type: system
updated: 2026-07-09
---

# CHH Cortex — Capabilities map

This repo is a **pilot workbench**, not a full clone of HERA's internal automation stack. It includes the workflows CHH needs to package grants and grow a curated knowledge base; HERA maintains advanced automation separately.

## Included in CHH Cortex (use today)

| Capability | How | Skill / path |
|------------|-----|--------------|
| **Grant workbench** | Per-RFP folders with decision chart, donor lens, revision log | `raw/proposals/` + `skills/grant-writer/SKILL.md` |
| **Red-team before paste** | Reviewer stress-test on draft sections | `skills/grant-red-team-reviewer/SKILL.md` |
| **Meeting / note triage** | Classify pasted transcripts into tasks and wiki candidates | `skills/transcript-triage/SKILL.md` |
| **Email population** | Curator-selected threads → `raw/email/` → triage → link to workbench | `raw/email/README.md`, triage + curator skills |
| **Knowledge promotion** | Curator-approved moves from `raw/` → `wiki/` with sources | `skills/knowledge-curator/SKILL.md` |
| **People & partnership context** | CHH roster and pilot dossier | `wiki/entities/people/`, `wiki/partnerships/chh.md` |
| **Task list** | Shared CHH priorities | `TASKS.md` |
| **Example walkthrough** | Safe fictional RFP | `raw/proposals/example-chh-rfp-2026/` |

## HERA-maintained (not in this lite repo)

| Capability | Why excluded | How CHH still benefits |
|------------|------------|------------------------|
| **Live automation agents** (`_system/live/`) | HERA ops + credentials | Patterns flow in via maintainer re-sync |
| **Self-improvement loops** | Internal quality system | Export quality gates (`RELEASE-GATE.md`) |
| **Email / Fireflies intake bots** | Sensitive archives | Manual paste + triage skill |
| **Full donor pipeline matrix** | HERA-only funders | CHH uses own workbenches under `raw/proposals/` |
| **Multi-agent grant fleet** | High complexity | Single-workbench grant-writer + red-team for pilot |

## Pilot default workflow

1. Land source material in `raw/` (meetings, RFP PDFs, notes)
2. Triage → propose wiki/tasks (curator approves)
3. Open grant workbench → draft sections → red-team → human paste

## Future expansion (requires MoU + IT review)

See `_system/CHH-CONTEXT.md` for full pain-point mapping and phases.

- **Curated email capture** — forward/export → `raw/email/` (Paul priority; no OAuth in pilot)
- Scheduled knowledge refresh from SharePoint/Drive
- CHH reviewer lessons library (promoted from revision logs)
- CHH-specific automation only where Hopkins approves hosting

## Source(s)

- Jul 2026 CHH demo — proposal packaging first
- `_system/chh-cortex-lite/REVIEW-LEDGER.md` — lite scope decision
