# JHU LSRI Individual Award Agent Handoff

## Use

Cross-agent audit comments for Codex, Cursor, Claude. **Not** Berktuğ revision style — use `REVISION-LOG.md` for that.

## Ledger

| ID | Date | Agent | Phase | Target file/section | Comment | Severity | Status | Owner | Source |
|----|------|-------|-------|---------------------|---------|----------|--------|-------|--------|
| LSRI-HANDOFF-001 | 2026-07-07 | cursor-fleet | Setup | package | Workbench bootstrapped for CHH demo × LSRI fleet | note | resolved | Berktuğ | go ultracode |
| LSRI-HANDOFF-002 | 2026-07-07 | cursor-fleet | Intake | `lsri-hypothesis-brief.md` | Fork B demo lean; **verify with Aral** before claiming locked | high | open | Aral | fleet merge |
| LSRI-HANDOFF-003 | 2026-07-07 | cursor-fleet | Hygiene | demo runbook | Show LSRI package + public opportunity facts only; never negotiation intel | blocker | resolved | Berktuğ | plan § demo hygiene |
| LSRI-HANDOFF-004 | 2026-07-07 | cursor-fleet | Intake | budget | ≤10% subaward — HERA cannot fund field implementation at scale | high | open | Shatha | InfoReady RFP |
| LSRI-HANDOFF-007 | 2026-07-08 | Cursor | Contact | Yazdi email thread | Landed 2026-07-07 reply: soft yes; roles TBD; do not paste as committed co-PI | medium | open | Aral | `raw/capture-logs/2026-07-07-yazdi-lsri-individual-award-email-thread.md` |
| LSRI-HANDOFF-008 | 2026-07-08 | cursor-fleet | Intake DEMO | Package | Post-Aral Fork C merge: 3-lens intake; hypothesis still open; runbook step 3 stale (A/B only); demo-safe CHH one-liner ready | high | open | Berktuğ | go ultracode DEMO MODE |
| LSRI-HANDOFF-009 | 2026-07-08 | cursor-fleet | Full package | `lsri-portal-fill-pack-2026-07-08.md` | Portal checklist + 4-page narrative + budget/biosketch/support templates; InfoReady 2019088 fields captured; Shatha must submit | high | open | Shatha | go ultracode |
| LSRI-HANDOFF-010 | 2026-07-08 | cursor-subagent | Submission | `submission/` | Red-team narrative + 5 submission artifacts; InfoReady draft saved under Berktuğ (Co-PI #1 Yazdi proposed); Shatha must re-login as PI, overwrite applicant, upload PDFs | high | open | Shatha | complete submission task |

## INNO-FLEET-PILOT (demo-driven)

| Run | Recipe | vs solo | Notes |
|-----|--------|---------|-------|
| LSRI-FLEET-001 | intake + co-applicant hybrid | TBD | Boot package + demo artifacts in one session; hypothesis still open |
| LSRI-FLEET-002 | demo + NotebookLM source-pack hybrid | likely positive | Three read-only lenses: CHH audience/story, LSRI claim-risk, NotebookLM source-pack. Output kept internal and claim-safe; no donor prose authored by subagents. |
| LSRI-FLEET-003 | grant-intake-fleet DEMO | positive vs solo | 3 parallel read-only lenses post-Aral Jul 8 notes; unified decision-pick; no donor prose; caught runbook Fork C gap |
| LSRI-FLEET-004 | section + full-review hybrid | positive vs solo | 3 lenses + parent draft; live InfoReady fields; hybrid B+C narrative; portal fill pack landed |

## Fleet orchestration log (2026-07-07)

```text
Recipe: intake + co-applicant hybrid
Scout: demo Jul 8 09:00 EDT; LSRI package missing; hypothesis open; Aral bullets pending
Fleet: 4 lenses — RFP intelligence, pitch-fork (internal), CHH audience, demo hygiene
Merge: raw/proposals/jhu-lsri-individual-2026/ + hypothesis brief + narrative skeleton + runbook + deck
Red-team: demo hygiene pass — LSRI package safe; negotiation intel / signals / TASKS blocked
Open: Aral hypothesis lock; Yazdi outreach; Shatha 4-page PDF by Jul 15
```

## Red-team hygiene verdict (2026-07-07)

| Check | Result |
|-------|--------|
| Sensitive paths excluded from runbook tabs | **pass** |
| Corpus / literature claims marked verify | **pass** |
| Aral co-PI trap avoided in skeleton | **pass** |
| ≤10% subaward stated consistently | **pass** |
| Fork B demo lean flagged verify-with-Aral | **pass** |
| Negotiation intel not in show list | **pass** |

**Claims verified against vault:**

- Deadline 15 Jul 11:59 PM — `raw/capture-logs/2026-07-02-jhu-infoready-rfp-resilience-and-lsri-individual.md`
- ≤10% subaward — same source
- Shatha PI / Aral trainee — `wiki/concepts/decisions/2026-07-02-jhu-lsri-individual-award-strategy.md`
- 165 messages / 34 corrections — `raw/drafts/jhu-cortex-presentation-outline-2026-07-07.md` (HERA pilot; no independent audit)

**Blockers remaining:** hypothesis lock; Yazdi role scoping (soft yes 2026-07-07); Shatha narrative ownership.

## Fleet orchestration log (2026-07-08 — DEMO MODE)

```text
Recipe: grant-intake-fleet (DEMO MODE)
Scout: CHH demo day; Aral Fork C landed; hypothesis open; dossier draft; runbook step 3 still A/B only
Fleet: 3 lenses — donor dossier (Weeraratna), evidence gaps (corpus/utilization/Syria), route/demo hygiene
Merge: all three → decision-pick; no donor prose; demo-safe one-liner from Aral capture; roster conflicts flagged
Red-team: skipped (internal memos only per intake recipe)
Open: Shatha reconcile Fork C; update runbook step 3; Aral on-call confirm; Yazdi not committed co-PI
```

## Source(s)

- `_system/handoffs/go-fleet-grant.md`
