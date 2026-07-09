---
name: CHH Cortex — Team Install
description: Half-day onboarding for JHU CHH — Claude Code primary, Google Drive sync, honest IT limits.
type: system
updated: 2026-07-09
---

# CHH Cortex — Install guide

**Audience:** Manny Kim, Paul Spiegel, William Weiss, CHH staff  
**Time:** ~4 hours first setup; ~30 min per additional user  
**Primary tool:** Claude Code + `chh-cortex-code` plugin

## 1 — Prerequisites

- Mac (Paul's preferred: one dedicated center laptop)
- GitHub access to `Cortexto/chh-cortex` (private)
- Claude Code or Claude desktop with code workspace
- Optional: Cursor for IDE parity
- Optional: Google Drive desktop sync for proposal corpus

## 2 — Clone repo

```bash
git clone git@github.com:Cortexto/chh-cortex.git
cd chh-cortex
```

Open `chh-cortex/` as workspace root (not parent folder).

## 3 — Claude Code + plugin

1. Open Claude Code from `chh-cortex/` folder
2. Install local plugin: `.claude-plugin/plugin.json` (`chh-cortex-code`)
3. Verify: ask *"Read ENTRY.md and list available skills"*

Or run onboarding skill:

```
Use skills/chh-onboarding/SKILL.md and complete setup checklist.
```

## 4 — Google Drive sync (recommended)

Paul/William discussed syncing consolidated proposals:

1. Create CHH Google Drive folder (center account)
2. Sync to local path, e.g. `~/CHH-Cortex-data/proposals/`
3. Symlink or copy into `raw/proposals/` — **curator approves** what enters vault
4. Do not auto-sync entire SharePoint without PII review

## 5 — First workflows

### Paste a meeting transcript

1. Save to `raw/meetings/YYYY-MM-DD_topic.md` (see `_template/`)
2. Prompt: `Use skills/transcript-triage/SKILL.md and triage this meeting`

### Open example grant workbench

```
I am working on jhu-lsri-individual-2026 — boot the workbench and decode the donor dossier.
```

### Start new CHH RFP

```bash
cp -r raw/proposals/_template-chh-rfp raw/proposals/my-grant-slug-2026
```

## 6 — Honest limits (Hopkins IT)

| Capability | v1 |
|------------|-----|
| Manual transcript/email paste | Yes |
| Grant workbench + red-team | Yes |
| Google Drive folder sync | Yes (manual curator gate) |
| Outlook calendar auto-ingest | No — IT blocks AI OAuth |
| Dropbox auto-access | No |
| Hopkins GPT memory persistence | No — use file-first vault instead |

**Calendar workaround (optional):** invite Gmail to Outlook events — hassle; Manny/Paul to decide.

## 7 — Cost notes (for Manny call)

| Item | Estimate |
|------|----------|
| Claude business/team seats | Center procurement — Paul mentioned paying through CHH |
| Cursor Pro (optional) | Per-seat if IDE parity wanted |
| GitHub private repo | Org already has Cortexto |
| Local inference (Ollama) | Optional; not required for pilot |

## 8 — Curator rules

- One curator-owner per pilot workflow
- No PII/PHI in git repo
- Human approval before paste-ready funder text
- Red-team footer on external outputs

## 9 — Support

HERA Digital Health (tech lead): Berktuğ Kubuk — b.kubuk@medak.org.tr  
Pattern updates: periodic re-sync from HERA Cortex via `scripts/build_chh_lite.py`

## Source(s)

- `wiki/partnerships/chh.md`
- `raw/meetings/2026-07-08_jhu-chh-cortex-demo-transcript.md`
