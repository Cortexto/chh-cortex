---
name: chh-onboarding
description: Half-day setup wizard for Johns Hopkins CHH Cortex lite — Claude Code, plugin, Google Drive sync, first workflows. Run when Manny or CHH staff first open the repo.
---

# CHH Onboarding

Use when a CHH user (Manny, Paul, William, or delegate) first sets up CHH Cortex lite.

## Required reads

1. `_system/CHH-INSTALL.md`
2. `wiki/partnerships/chh.md`
3. `ENTRY.md`

## Onboarding checklist (run in order)

### Phase A — Environment (30 min)

- [ ] Clone `Cortexto/chh-cortex` to local machine
- [ ] Open repo root as Claude Code workspace
- [ ] Confirm `CLAUDE.md` loads (ask: summarize routing rules in 3 bullets)
- [ ] Install `chh-cortex-code` plugin from `.claude-plugin/plugin.json`

### Phase B — Vault orientation (20 min)

- [ ] Read `wiki/partnerships/chh.md` — IT matrix and pilot ask
- [ ] Browse `raw/proposals/jhu-lsri-individual-2026/` — example workbench
- [ ] Browse `wiki/entities/people/` — CHH roster

### Phase C — First actions (60 min)

- [ ] Paste a sample meeting note into `raw/meetings/` using `_template/`
- [ ] Run transcript-triage on the sample
- [ ] Boot LSRI workbench: *I am working on jhu-lsri-individual-2026*
- [ ] Copy `_template-chh-rfp` to a test slug; fill DECISION-CHART stub

### Phase D — Data sync (optional, 60 min)

- [ ] Identify CHH proposal folder (SharePoint/OneDrive — Sanny tracker)
- [ ] Set up Google Drive sync path per CHH-INSTALL §4
- [ ] Curator reviews one proposal file before adding to `raw/proposals/`

### Phase E — Honest limits acknowledgment

Confirm user understands v1 **does not**:

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
