---
name: CHH Cortex pilot
description: Partner dossier for Center for Humanitarian Health Cortex lite deployment.
type: partnership
organization: Johns Hopkins University — Center for Humanitarian Health
status: active-pilot-prep
updated: 2026-07-09
---

# JHU CHH — Cortex pilot dossier

**Status:** Post-demo → lite repo + operationalization call  
**Tech lead:** External pattern maintainer (HERA Digital Health) — MoU pending  
**CHH role:** Data ownership, curator approval, IT compliance, hosting choice

## Why CHH cares

| CHH problem | Cortex answer |
|-------------|---------------|
| Fragmented proposals and meeting notes | File-first vault in git / Google Drive |
| No memory between AI sessions | Shared markdown brain + workbench per grant |
| Hopkins GPT session expiry | Institution owns files; swap model without losing memory |
| High proposal volume | Grant workbench + red-team gates |
| IT blocks AI on Outlook/calendar | Manual paste + curated **email population** → `raw/email/`; see `CHH-ROADMAP.md` |

Person context: [[paul-spiegel]]

## Pilot ask

**One CHH workflow** with curator-owner, approval gates, **no PII/PHI**:

| Priority | Workflow |
|----------|----------|
| **A (default)** | Internal RFP packaging |
| B | Donor/reporting reuse |
| C | IRB/protocol boilerplate |

## Deployment options

| Option | Notes |
|--------|-------|
| **Dedicated CHH Mac + Google Drive** | Preferred in demo discussion |
| Hopkins GPT + synced folder | IT-approved; session limits |
| Manual paste vault | Works today; no OAuth |

## Lite repo

| Item | Detail |
|------|--------|
| Repo | `Cortexto/chh-cortex` (private) |
| Onboarding | `skills/chh-onboarding/SKILL.md` + `_system/CHH-INSTALL.md` |
| Demo workbench | `raw/proposals/demo-lsri-workbench-2026/` (sanitized LSRI-shape walkthrough) |

## IT limits (v1)

- No automatic Outlook/calendar ingest
- No Dropbox auto-access for AI tools
- Curator gate on all `raw/` promotions

## Source(s)

- Jul 2026 CHH Cortex demo (sanitized summary)
