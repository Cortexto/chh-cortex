---
name: JHU CHH Cortex pilot
description: Partner dossier for Center for Humanitarian Health Cortex lite deployment — pain points, IT matrix, pilot scope, MoU frame, HERA tech-lead role.
type: partnership
organization: Johns Hopkins University — Center for Humanitarian Health
status: active-pilot-prep
updated: 2026-07-09
---

# JHU CHH — Cortex pilot dossier

**Status:** Post-demo (2026-07-08) → lite repo + Manny operationalization call  
**HERA role:** Tech lead (patterns, training, sanitized repo maintenance) — MoU pending  
**CHH role:** Data ownership, curator approval, IT compliance, hosting choice

## Why CHH cares

| CHH problem | Cortex answer |
|-------------|---------------|
| Fragmented proposals, meetings, partner notes across inboxes | File-first vault in git / Google Drive |
| No memory between AI sessions | Shared markdown brain + workbench per grant |
| Hopkins GPT 30-day session expiry | Institution owns files; swap model without losing memory |
| High proposal volume, slow packaging | Grant workbench + red-team gates |
| IT blocks AI on Outlook/calendar | Manual paste + Google Drive sync v1; no OAuth promise |

## Paul Spiegel pain matrix (Jul 8 demo)

| Need | Blocker | Lite v1 path |
|------|---------|--------------|
| Daily meeting prep from calendar | Hopkins blocks AI → Outlook | Manual iCal export → paste transcript/meeting notes into vault |
| Email → knowledge base | Same IT block | Forward/select emails → land in `raw/email/` manually |
| Proposal reuse | Data in SharePoint but no AI layer | Sync proposal folder via Google Drive → `raw/proposals/` |
| Cross-tool memory (Claude ↔ ChatGPT) | No shared ledger | Single vault + Claude Code plugin |
| Dropbox file access | Blocked | Local/Google Drive folder as vault root |

Full person context: [[paul-spiegel]]

## Pilot ask (from demo close)

**One CHH workflow** with curator-owner, approval gates, **no PII/PHI** in shared vault:

| Priority | Workflow | Why first |
|----------|----------|-----------|
| **A (default)** | Internal RFP packaging | LSRI workbench proved live; proposals already consolidated |
| B | Donor/reporting reuse | Verified blocks + fact-locks |
| C | IRB/protocol boilerplate | Low-risk canonical blocks |
| D | Staff onboarding | Queryable memory vs inbox archaeology |

Requirements strip: **curator-owner · explicit approval gates · no PII/PHI**

## Deployment options discussed

| Option | Pros | Cons |
|--------|------|------|
| **Dedicated CHH Mac + Google Drive** | Paul preferred; isolates from personal machines | Procurement + IT approval |
| Hopkins GPT + synced folder | IT-approved models | 30-day sessions; Paul finds quality lower |
| Personal Claude on each laptop | Best model quality | No shared center memory; IT may object |
| Gmail calendar invite workaround | Enables calendar extract | Double-calendar hassle (Paul, Manny) |

**Decision doc:** `wiki/concepts/decisions/2026-07-08-jhu-chh-cortex-lite-deployment.md`

## Lite repo delivery

| Item | Detail |
|------|--------|
| Repo | `Cortexto/chh-cortex` (private) |
| Build | `scripts/build_chh_lite.py` from HERA Cortex canonical |
| Onboarding | `skills/chh-onboarding/SKILL.md` + `_system/CHH-INSTALL.md` |
| Claude plugin | `chh-cortex-code` v0.1.0 |
| Contacts | Manny Kim (`ckim183@jh.edu`) — technical owner |

## Joint funding context (sanitized export)

Include in lite repo as runnable examples:

- **LSRI Individual Award 2026** — workbench structure (sanitized dossier; no negotiation intel)
- **Connect2Care / Google.org Somalia** — evaluation partnership hub

Exclude: HERA-only packages, `wiki/observations/*`, internal Aral/Berktuğ direction captures.

## MoU frame (draft — not signed)

William Weiss raised MoU with HERA (similar to IAPS). Intended scope:

| Party | Responsibility |
|-------|----------------|
| **HERA (tech lead)** | Cortex pattern maintenance; lite repo sync; training (half-day setup); grant-workflow skills; periodic updates |
| **CHH** | Institutional data; curator assignment; IT/hosting decisions; compliance (PII/PHI, Hopkins policies); pilot workflow selection |
| **Shared** | Success metrics for pilot; publication/co-authorship only if separately agreed |

MoU brief (internal): `_system/handoffs/jhu-chh-mou-brief-2026-07-09.md`

## Contacts

| Person | Role on pilot |
|--------|---------------|
| [[paul-spiegel]] | Executive sponsor; pain-point owner |
| [[william-weiss]] | HIS / institutional AI policy |
| [[chaeeun-kim]] | Technical operationalization |
| [[shatha-elnakib]] | Science / LSRI lane (separate from tooling pilot) |

## Source(s)

- `raw/meetings/2026-07-08_jhu-chh-cortex-demo-transcript.md`
- `raw/drafts/jhu-chh-notebooklm-sources/07-chh-transfer-src.md`
- `raw/drafts/jhu-chh-demo-share-notes-for-chh-2026-07-08.md`
- `raw/email/2026-07-09/landed-2026-07-09_jhu-kim-cortex-followup.md`
- `wiki/inbox/triage/2026-07-08-jhu-chh-cortex-demo.md`
