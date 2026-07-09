---
name: CHH Cortex — Team Install
description: Onboarding for JHU CHH — Cowork plug-and-play track for Paul, Claude Code track for technical setup, Google Drive sync, honest IT limits.
type: system
updated: 2026-07-09
---

# CHH Cortex — Install guide

**Audience:** Manny Kim, Paul Spiegel, William Weiss, CHH staff  
**Two tracks:** Track A (Cowork, ~30 min, no terminal — Paul and non-technical staff) · Track B (Claude Code, ~half day — Manny / technical owner)  
**Skills load from repo paths in both tracks;** `.claude-plugin/plugin.json` is a metadata stub (v0.2), not something you install.

## 1 — Prerequisites

- Mac (Paul's preferred: one dedicated center laptop)
- GitHub access to `Cortexto/chh-cortex` (private) — accept the emailed collaborator invite first
- Claude desktop app (Cowork) for Track A; Claude Code for Track B
- Optional: Cursor for IDE parity
- Optional: Google Drive desktop sync for proposal corpus

## 2 — Track A: Cowork, no terminal (Paul)

1. Get the folder once — either of:
   - Ask Manny/HERA to put the `chh-cortex` folder in the center Google Drive and sync it locally, or
   - On github.com open Cortexto/chh-cortex → green **Code** button → **Download ZIP** → unzip somewhere easy to find (Documents works)
2. Open the Claude desktop app → start a **Cowork** session → add the `chh-cortex` folder
3. Say: *Read CLAUDE.md and get me started* — Claude runs the onboarding wizard from there

That's the whole install. Updates arrive by replacing the folder (Manny re-syncs from GitHub); Paul never touches git.

## 2b — Track B: Clone repo (Manny / technical owner)

```bash
git clone https://github.com/Cortexto/chh-cortex.git
cd chh-cortex
```

(SSH `git@github.com:Cortexto/chh-cortex.git` also works if you already use SSH keys.)

Open `chh-cortex/` as workspace root (not parent folder).

## 3 — Claude Code + plugin (Track B)

1. Open Claude Code from `chh-cortex/` folder
2. Review plugin stub: `.claude-plugin/plugin.json` (`chh-cortex-code` v0.2 — skills load from repo)
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

1. Save to `raw/meetings/` using the paste template in `raw/meetings/_template/README.md`
2. Prompt: `Use skills/transcript-triage/SKILL.md and triage this meeting`

### Open example grant workbench

```
I am working on example-chh-rfp-2026 — boot the workbench and decode the donor dossier.
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
Pattern updates: HERA maintainer re-syncs from canonical Cortexto/hera-cortex vault (build script lives there — not in this repo).

## Source(s)

- `wiki/partnerships/chh.md`
