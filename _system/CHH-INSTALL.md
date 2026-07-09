---
name: CHH Cortex — Team Install
description: Onboarding for JHU CHH — folder sync or git clone of Cortexto/chh-cortex only
type: system
updated: 2026-07-09
---

# CHH Cortex — Install guide

**Start with `CHH-ROADMAP.md`** (root) for what this is and raw vs wiki.

**Audience:** Manny Kim, Paul Spiegel, William Weiss, CHH staff

## Tracks

- **Track A** (~30 min, no terminal) — faculty / program leads  
- **Track B** (~half day) — technical owner (Manny)

## 1 — Prerequisites

- Mac (center-dedicated laptop preferred)
- Access to **`Cortexto/chh-cortex`** (private GitHub) — Track B, or ZIP download for Track A
- Organization-approved AI tool with **folder access**
- Optional: Google Drive desktop sync

## 2 — Track A: Folder + AI assistant

1. Get the folder — Drive sync **or** GitHub → Download ZIP
2. Mount `chh-cortex` in your AI tool
3. Say: *Read CHH-ROADMAP.md and ENTRY.md*

Updates: Manny pulls from GitHub or replaces Drive copy when HERA publishes a release.

## 2b — Track B: Clone repo

```bash
git clone https://github.com/Cortexto/chh-cortex.git
cd chh-cortex
```

Open `chh-cortex/` as workspace root.

## 3 — Google Drive sync (optional)

1. CHH Google Drive folder (center account)
2. Curator copies approved files into `raw/proposals/` or `raw/email/`
3. No auto-sync of full SharePoint without PII review

## 4 — First workflows

| Action | Command / path |
|--------|----------------|
| Learn routes | `I am working on demo-lsri-workbench-2026` |
| New real RFP | Copy `raw/proposals/_template-chh-rfp/` |
| Email | `raw/email/README.md` + `chh-email-triage` skill |
| Meeting | `raw/meetings/_template/` + transcript-triage |

## 5 — Honest limits (Hopkins IT)

| Capability | Pilot |
|------------|-------|
| Manual paste (email, calendar text) | Yes |
| Grant workbench + red-team | Yes |
| Outlook auto-ingest | No |
| Background automation bots | No — not in this repo |

## 6 — Support

Berktuğ Kubuk — berktug@heradigitalhealth.org  

HERA publishes updates to **`Cortexto/chh-cortex`** only. No second repo access required for CHH staff.

## Source(s)

- `wiki/partnerships/chh.md`
