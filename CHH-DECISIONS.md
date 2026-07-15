---
name: CHH Cortex — Pilot decisions log
description: What we initially thought vs where we landed — center-level decisions visible to the whole team
type: guide
updated: 2026-07-15
---

# CHH Cortex — Pilot decisions log

**Read with:** `CHH-ROADMAP.md` · `CHH-DEPLOYMENT-OPTIONS.md`

This file is the **center-level decision record** for the CHH pilot — not grant-by-grant routing (that lives in each workbench's `DECISION-CHART.md`).

Each row captures: what we **first assumed**, what we **decided**, and **why it changed** when it did.

**Phase 0 status:** held 2026-07-15 — partial. Open items are in § Open decisions below (not repeated in other docs).

---

## Which file do I use?

**Four center-level docs** + **one folder per grant**. Git handles edit collisions (pull, commit, resolve); ledgers are **coordination records only** — not file locks, not model loggers (see CD-005).

| I need to… | Open |
|------------|------|
| Understand the product, raw vs wiki, pain points | `CHH-ROADMAP.md` |
| Install, clone, Antigravity paste-boot | `_system/CHH-INSTALL.md` |
| Lane A vs B, Mac options, rollout phases | `CHH-DEPLOYMENT-OPTIONS.md` |
| **Pilot decisions, Phase 0 status, bottlenecks** | **This file** |
| Week 0–4 center-Mac checklist | `_system/CHH-PHASE1-PLAYBOOK.md` |
| Step-by-step workflow map | `wiki/concepts/workflow/chh-workflows-guide.md` |
| Email / meeting / Fireflies SOP | `wiki/concepts/workflow/chh-sop-*.md` |
| **One RFP's route, locks, gates** | `raw/proposals/<slug>/DECISION-CHART.md` |
| **Draft feedback and why it changed** | `raw/proposals/<slug>/REVISION-LOG.md` |
| Continue same grant in a new AI session (optional) | `raw/proposals/<slug>/REVIEW-LEDGER.md` |

**Do not confuse similarly named files:**

| Name | Scope |
|------|-------|
| `CHH-DECISIONS.md` | **Center pilot** — IT, hardware, repo policy |
| `DECISION-CHART.md` | **One grant** — hypothesis, budget, section route |
| `REVISION-LOG.md` | **One grant** — draft feedback history |
| `REVIEW-LEDGER.md` | **One grant** — optional cross-tool session notes |

**Curator rule:** append new rows; do not silently delete old reasoning — mark superseded instead.

---

## Questions and bottlenecks (GitHub)

1. **Try the repo first** — open `chh-cortex/` as your AI workspace root and ask your question with context (e.g. *Read CHH-DECISIONS.md and CHH-DEPLOYMENT-OPTIONS.md — then answer: …*).
2. **If still stuck** — open a **GitHub Issue** on `Cortexto/chh-cortex` instead of long email threads. Title: `Bottleneck: <short label>`. Include: what you tried, which tool (Antigravity / Claude / Cursor), and the file path if relevant.

HERA reads issues to evolve docs and unblock Phase 1 — the issue history becomes a public audit trail of how the workflow is shaping.

---

## Decision log

| ID | Date | Initial thought | Decision | Why it evolved | Status |
|----|------|-----------------|----------|----------------|--------|
| **CD-001** | 2026-07-08 | One tool fits everyone | **Folder-first vault** — any approved AI with workspace access | Demo showed Cursor; Paul uses Claude Business; Manny uses Antigravity | **locked** |
| **CD-002** | 2026-07-08 | Auto-ingest Outlook + calendar like a personal assistant | **Manual SOPs** for Lane A; start **center Mac** (Lane B) for grants | Hopkins IT blocks AI OAuth on institutional mail/calendar | **locked** |
| **CD-003** | 2026-07-08 | Deploy on every personal laptop | **One dedicated CHH Mac** + Drive for proposal corpus | Shared center brain; Paul pivoted to proposals-first on demo call | **pending** Mac spec |
| **CD-004** | 2026-07-09 | Public GitHub is enough for everything | **Public repo = patterns + demo**; **live RFP drafts → private repo or Drive** | Manny raised confidentiality on 2026-07-15 call | **open** — Paul debrief |
| **CD-005** | 2026-07-15 | Ledger auto-logs model choice and prevents simultaneous edits | **Git handles collisions**; ledgers are coordination records only | On-call confusion — corrected in install + workflows guide | **locked** |
| **CD-006** | 2026-07-15 | Non-technical staff should use Codex | **Claude Desktop + folder mount** for faculty; Codex is maintainer-only | Demo misspeak; Paul/William are not terminal-first users | **locked** |
| **CD-007** | 2026-07-15 | Hopkins might block AI on laptops entirely | **Blocker is email/calendar OAuth only** — AI on laptop is OK | Manny confirmed on Phase 0 call | **locked** |
| **CD-008** | 2026-07-15 | Antigravity reads repo like Cursor | **Paste-boot required** — open `chh-cortex/` as project root; first prompt = Read CHH-ROADMAP then ENTRY | Calendar export files failed to read — likely wrong workspace root | **locked** — see `CHH-INSTALL.md` |
| **CD-009** | 2026-07-15 | Invite optional for exploration | **GitHub collaborator invite** to JHU email for pull + push when ready | Berktuğ sent invite post-call | **locked** |
| **CD-010** | 2026-07-15 | Paul's ambient email/calendar assistant is v1 | **~60% without IT change** — manual paste + SOPs; full automation = IT track | ~200 emails/day; OAuth blocked | **expectation set** |

---

## Open decisions (Phase 0 partial)

| Item | Owner | Next |
|------|-------|------|
| Dedicated CHH Mac model/spec | Paul + Manny | After Paul debrief |
| Curator name (PII gate) | Paul | Confirm on debrief |
| CHH Google Drive proposal folder | Manny | Path + sync owner |
| Outlook auto-forward to external allowed? | Manny | Test Hopkins settings |
| Private repo vs Drive for live drafts | Paul + Manny | CD-004 |

---

## Support

Berktuğ Kubuk — berktug@heradigitalhealth.org
