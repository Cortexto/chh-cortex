---
name: CHH Cortex Lite — Sanitization Manifest
description: Allowlist and strip rules for exporting HERA Cortex → Cortexto/chh-cortex
type: export-manifest
updated: 2026-07-09
upstream: Cortexto/hera-cortex
downstream: Cortexto/chh-cortex
---

# CHH Cortex Lite — Sanitization Manifest

Build command:

```bash
python3 scripts/build_chh_lite.py \
  --source /path/to/hera-cortex/cortex \
  --output /path/to/chh-cortex
```

## Strip (never export)

| Pattern | Reason |
|---------|--------|
| `wiki/observations/**` | Person negotiation intel; Paul flagged on demo |
| `_system/state/**` | HERA automation secrets |
| `_system/HOT_CACHE.md` | HERA internal priorities |
| `_system/live/**` | Berktuğ personal automations |
| `raw/email/**` (full archive) | Sensitive |
| `raw/fireflies/**` (full archive) | HERA internal meetings |
| HERA-only proposals (IRUSA, AWS, DIV, UNHCR, etc.) | Not JHU joint |
| `raw/proposals/jhu-lsri-individual-2026/submission/**` | Live PDFs/DOCX |
| `raw/proposals/jhu-lsri-individual-2026/BRAINSTORM-LEDGER.md` | Internal hypothesis forks |
| `raw/proposals/jhu-lsri-individual-2026/AGENT-HANDOFF.md` | Internal agent audit |
| `raw/proposals/jhu-lsri-individual-2026/REVISION-LOG.md` | Berktuğ internal feedback |
| `rowboat_source` frontmatter keys | Legacy traceability — strip on copy |
| Berktuğ PhD / RWJF / internal gate sections on Shatha card | CHH-facing only |

## Keep (allowlist)

### Skills

- `skills/grant-writer/SKILL.md` (CHH-adapted header in output)
- `skills/grant-red-team-reviewer/SKILL.md`
- `skills/transcript-triage/SKILL.md`
- `skills/knowledge-curator/SKILL.md`
- `skills/context-navigator/SKILL.md`
- `skills/chh-onboarding/SKILL.md` (generated)

### Wiki — partnerships & workflow

- `wiki/partnerships/jhu-chh-cortex-pilot.md` → `wiki/partnerships/chh.md`
- `wiki/concepts/workflow/grant-proposal-workbench.md` (if exists, else stub)
- `wiki/opportunities/jhu-life-sciences-research-initiative-2026.md` (public criteria)
- `wiki/projects/connect2care-google-org.md` (from starter bundle)

### Wiki — people (see PEOPLE-ROSTER.md)

Export with strip rules applied.

### Raw — proposals

| Path | Notes |
|------|-------|
| `raw/proposals/jhu-lsri-individual-2026/README.md` | Adapt station note |
| `raw/proposals/jhu-lsri-individual-2026/DECISION-CHART.md` | Full |
| `raw/proposals/jhu-lsri-individual-2026/DONOR-DOSSIER.md` | Sections 2 only → replace with sanitized lens |
| `raw/proposals/jhu-lsri-individual-2026/lsri-narrative-skeleton.md` | Full |
| `raw/proposals/jhu-lsri-individual-2026/lsri-hypothesis-brief.md` | Strip Aral trainee internal notes |
| `raw/proposals/_template-chh-rfp/**` | Generated empty scaffold |

### Raw — meetings

- `raw/meetings/_template/README.md` — paste instructions only

### System

- `_system/CHH-INSTALL.md` (generated)
- `_system/SANITIZATION-MANIFEST.md` (this file copy)
- `_system/adapters/claude-code.md` (adapt from HERA)
- `_system/AGENTS-AND-SKILLS.md` (CHH subset)

## Post-copy transforms

1. Remove lines matching `^rowboat_source:`
2. Replace `HERA Cortex` → `CHH Cortex` in ENTRY/README where audience-facing
3. Grep output for forbidden tokens: `wiki/observations`, `negotiation style`, `berktug-signals`, `aral-signals`
4. Replace LSRI `DONOR-DOSSIER.md` body with sanitized reviewer lens from manifest template

## QA checklist (before GitHub invite)

- [ ] No `wiki/observations/` paths in repo
- [ ] No live submission PDFs/DOCX
- [ ] No HERA email raw files
- [ ] Shatha card has no PhD committee section
- [ ] Plugin loads without HERA vault path
- [ ] `skills/chh-onboarding/SKILL.md` runs end-to-end read test

## Source(s)

- Plan: CHH Cortex Lite (2026-07-09)
- Template: `raw/drafts/jhu-chh-notebooklm-upload-sanitized-dossier.md`
