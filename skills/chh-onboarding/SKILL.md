---
name: chh-onboarding
description: Setup wizard for Johns Hopkins CHH Cortex lite — Cowork plug-and-play track (~30 min) or Claude Code technical track (half day). Run when Paul, Manny, or CHH staff first open the repo, say "get me started", or ask how to set this up.
---

# CHH Onboarding

Use when a CHH user (Manny, Paul, William, or delegate) first sets up CHH Cortex lite.

## Required reads

1. `_system/CHH-INSTALL.md`
2. `wiki/partnerships/chh.md`
3. `ENTRY.md`

## Step 0 — Pick the track

Ask one question: **"Are you in the Claude desktop app (Cowork) or Claude Code?"**

- **Cowork** → Track A below. The user is likely non-technical (Paul): no terminal, no git, plain language, one step at a time. If the folder is already mounted, environment setup is done — skip straight to orientation.
- **Claude Code** → Track B (full checklist, Phases A–E). This is the technical-owner path (Manny).

## Track A — Cowork wizard (~30 min, Paul-friendly)

Run conversationally, one step per message, confirming each before moving on:

1. **Confirm the vault is loaded** — summarize `ENTRY.md` in 3 plain-language bullets and name the 6 available skills
2. **Orientation** — walk through `wiki/partnerships/chh.md` (what this pilot does and doesn't do) and `raw/proposals/example-chh-rfp-2026/` (the fictional example workbench)
3. **First win** — ask the user to paste any recent meeting note or transcript into chat; run `skills/transcript-triage/SKILL.md` on it and save the result to `raw/meetings/` using `raw/meetings/_template/README.md`
4. **Grant demo** — say back: try *"I am working on example-chh-rfp-2026"* and boot the workbench
5. **Honest limits** — state Phase E limits below in plain language (no Outlook auto-ingest, no Hopkins email access)
6. **Close** — emit the Output section below; flag anything needing Manny or the HERA tech lead

Never send a Cowork user to the terminal. If a step needs git or file plumbing, log it as a blocker for Manny instead.

## Track B — Claude Code checklist (run in order)

### Phase A — Environment (30 min)

- [ ] Clone `Cortexto/chh-cortex` per `_system/CHH-INSTALL.md` §2b (HTTPS)
- [ ] Open repo root as Claude Code workspace
- [ ] Confirm `CLAUDE.md` loads (ask: summarize routing rules in 3 bullets)
- [ ] Review `.claude-plugin/plugin.json` (metadata stub v0.2 — skills load from repo paths)

### Phase B — Vault orientation (20 min)

- [ ] Read `wiki/partnerships/chh.md` — IT matrix and pilot ask
- [ ] Browse `raw/proposals/example-chh-rfp-2026/` — fictional example workbench
- [ ] Browse `wiki/entities/people/` — CHH roster

### Phase C — First actions (60 min)

- [ ] Paste a sample meeting note into `raw/meetings/` using `_template/`
- [ ] Run transcript-triage on the sample
- [ ] Boot example workbench: *I am working on example-chh-rfp-2026*
- [ ] Copy `_template-chh-rfp` to a test slug; fill DECISION-CHART stub

### Phase D — Data sync (optional, 60 min)

- [ ] Identify CHH proposal folder (SharePoint/OneDrive — Sanny tracker)
- [ ] Set up Google Drive sync path per CHH-INSTALL §4
- [ ] Curator reviews one proposal file before adding to `raw/proposals/`

### Phase E — Honest limits acknowledgment

Confirm user understands v0.2 **does not**:

- Auto-connect Outlook calendar or Hopkins email
- Replace Hopkins GPT for all tasks
- Export person-observation or negotiation mining

## Output

After checklist, emit:

1. **Setup status** — which phases complete
2. **Blockers** — IT, procurement, curator assignment
3. **Recommended pilot workflow** — RFP packaging default unless Paul chooses IRB/reporting
4. **Next call topics** for HERA tech lead if blocked

## Handoff

- Grant drafting → `skills/grant-writer/SKILL.md`
- Ambiguous tasks → `skills/context-navigator/SKILL.md`

## Source(s)

- `_system/CHH-INSTALL.md`
- `wiki/partnerships/chh.md`
- Jul 8 demo transcript — Manny: "key thing is streamlining knowledge into MD"
