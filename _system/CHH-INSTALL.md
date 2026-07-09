---
name: CHH Cortex — Team Install
description: Onboarding for JHU CHH — folder sync track for faculty, git track for technical owner, Google Drive sync, honest IT limits.
type: system
updated: 2026-07-09
---

# CHH Cortex — Install guide

**Audience:** Manny Kim, Paul Spiegel, William Weiss, CHH staff  

**Two tracks:**  
- **Track A** (~30 min, no terminal) — faculty and program leads  
- **Track B** (~half day) — technical owner (Manny)

See `_system/CHH-CAPABILITIES.md` for what this repo includes vs HERA-maintained automation.

## 1 — Prerequisites

- Mac (center-dedicated laptop preferred for pilot)
- GitHub access to `Cortexto/chh-cortex` (private) — for Track B, or ZIP download for Track A
- Organization-approved AI tool with **folder access** (mount local folder or synced Drive copy)
- Optional: Google Drive desktop sync for proposal corpus

## 2 — Track A: Folder + AI assistant (no terminal)

1. Get the folder once — either:
   - Center Google Drive copy synced locally (Manny/HERA publishes updates), or
   - GitHub → **Code** → **Download ZIP** → unzip (e.g. Documents)
2. Open your approved AI tool → attach or mount the `chh-cortex` folder
3. Say: *Read ENTRY.md and get me started*

Updates arrive when Manny replaces the folder from GitHub or Drive. No git required on this track.

## 2b — Track B: Clone repo (technical owner)

```bash
git clone https://github.com/Cortexto/chh-cortex.git
cd chh-cortex
```

Open `chh-cortex/` as the workspace root (not the parent folder).

Verify: *Read ENTRY.md and list available skills.*

Or run: `Use skills/chh-onboarding/SKILL.md and complete setup checklist.`

## 4 — Google Drive sync (recommended)

1. Create CHH Google Drive folder (center account)
2. Sync locally, e.g. `~/CHH-Cortex-data/proposals/`
3. Copy curator-approved files into `raw/proposals/`
4. Do not auto-sync entire SharePoint without PII review

## 5 — First workflows

### Paste a meeting transcript

1. Save using `raw/meetings/_template/README.md`
2. Run: `Use skills/transcript-triage/SKILL.md and triage this meeting`

### Promote knowledge to wiki

1. After triage, curator approves promotion
2. Run: `Use skills/knowledge-curator/SKILL.md and propose wiki updates`

### Open example grant workbench

```
I am working on example-chh-rfp-2026 — boot the workbench and decode the donor dossier.
```

### Start new CHH RFP

Copy `raw/proposals/_template-chh-rfp/` to a new folder under `raw/proposals/` and fill stubs.

## 6 — Honest limits (Hopkins IT)

| Capability | Pilot |
|------------|-------|
| Manual transcript/email paste | Yes |
| Grant workbench + red-team | Yes |
| Wiki promotion (curator-gated) | Yes |
| Google Drive folder sync | Yes (manual curator gate) |
| Outlook calendar auto-ingest | No |
| Dropbox auto-access for AI | No |
| Hopkins GPT persistent memory | No — file-first vault instead |
| HERA background automation | No — see CHH-CAPABILITIES.md |

## 7 — Cost notes (for center procurement)

| Item | Estimate |
|------|----------|
| Team AI seats (folder-capable) | Center procurement |
| GitHub private repo | Cortexto org |
| Local inference (optional) | Not required for pilot |

## 8 — Curator rules

- One curator-owner per pilot workflow
- No PII/PHI in git repo
- Human approval before paste-ready funder text
- Red-team footer on external outputs

## 9 — Support

HERA Digital Health (tech lead): Berktuğ Kubuk — berktug@heradigitalhealth.org  

Pattern updates: HERA maintainer re-syncs from canonical Cortexto/hera-cortex vault (build tooling lives there, not in this repo).

## Source(s)

- `wiki/partnerships/chh.md`
