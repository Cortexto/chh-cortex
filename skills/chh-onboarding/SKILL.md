---
name: chh-onboarding
description: Setup wizard for Johns Hopkins CHH Cortex — faculty track (~30 min) or technical-owner track (half day). Run when CHH staff first open the repo or say "get me started".
---

# CHH Onboarding

Use when a CHH user (Manny, Paul, William, or delegate) first sets up CHH Cortex.

## Required reads

1. `_system/CHH-INSTALL.md`
2. `_system/CHH-CAPABILITIES.md`
3. `wiki/partnerships/chh.md`
4. `ENTRY.md`

## Step 0 — Pick the track

Ask: **"Will you use git and a full workspace setup, or folder sync only?"**

- **Folder only** → Track A (faculty / Paul). No terminal, no git.
- **Git + workspace** → Track B (technical owner / Manny).

## Track A — Folder wizard (~30 min)

Run conversationally, one step per message:

1. **Confirm vault loaded** — summarize `ENTRY.md` in 3 plain bullets; name the six skills
2. **Orientation** — `wiki/partnerships/chh.md` + `raw/proposals/example-chh-rfp-2026/`
3. **Capabilities** — summarize `_system/CHH-CAPABILITIES.md` (what is included vs HERA-maintained)
4. **First win** — user pastes a meeting note; run `skills/transcript-triage/SKILL.md`; save to `raw/meetings/`
5. **Grant demo** — *I am working on example-chh-rfp-2026*
6. **Honest limits** — no Outlook auto-ingest; no background automation in lite repo
7. **Close** — emit Output section; flag blockers for Manny or HERA tech lead

Never send Track A users to the terminal.

## Track B — Technical checklist

### Phase A — Environment (30 min)

- [ ] Clone per `_system/CHH-INSTALL.md` §2b
- [ ] Open repo root as workspace
- [ ] Confirm `ENTRY.md` + skills index load

### Phase B — Orientation (20 min)

- [ ] Read `wiki/partnerships/chh.md` and `CHH-CAPABILITIES.md`
- [ ] Browse `example-chh-rfp-2026/` and `wiki/entities/people/`

### Phase C — First actions (60 min)

- [ ] Paste sample meeting → transcript-triage
- [ ] Boot example workbench
- [ ] Copy `_template-chh-rfp` to test slug
- [ ] Run knowledge-curator on one approved promotion

### Phase D — Data sync (optional)

- [ ] Google Drive path per CHH-INSTALL §4

### Phase E — Limits

Confirm v0.2 does not include: Outlook auto-ingest, HERA background automation, person-observation mining.

## Output

1. Setup status  
2. Blockers  
3. Recommended pilot workflow (RFP default)  
4. Next topics for HERA tech lead if blocked  

## Handoff

- Grant drafting → `skills/grant-writer/SKILL.md`  
- Wiki promotion → `skills/knowledge-curator/SKILL.md`  
- Routing → `skills/context-navigator/SKILL.md`
