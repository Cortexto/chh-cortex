---
name: CHH Cortex — Phase 1 center pilot playbook
description: Weeks 1–4 checklist — dedicated CHH Mac, first live RFP workbench, visible win
type: system
updated: 2026-07-15
---

# CHH Phase 1 playbook — center Mac pilot

**Prerequisite:** Phase 0 Manny call complete — hardware, curator, Drive folder, accounts decided.  
**Reference:** `CHH-DEPLOYMENT-OPTIONS.md` · `_system/CHH-INSTALL.md` · `skills/chh-onboarding/SKILL.md`

**Goal:** One real internal RFP section through workbench + red-team + revision log **without waiting on Outlook OAuth**.

---

## Week 0 — Hardware & access (CHH)

| # | Task | Owner | Done |
|---|------|-------|------|
| 0.1 | Procure / designate **CHH Mac** | CHH admin | [ ] |
| 0.2 | Install macOS updates; center login policy | Manny | [ ] |
| 0.3 | Claude Team/Business or approved AI tool | CHH billing | [ ] |
| 0.4 | Optional: Cursor if IDE parity wanted | Manny | [ ] |
| 0.5 | Name **curator** (PII gate) | Paul | [ ] |
| 0.6 | Create **Google Drive folder** for proposal corpus | Manny | [ ] |
| 0.7 | Clone repo or sync ZIP — see CHH-INSTALL Track B / A | Manny | [ ] |

---

## Week 1 — Vault live (Manny + Berktuğ setup)

| # | Task | Owner | Done |
|---|------|-------|------|
| 1.1 | Open `chh-cortex/` as **workspace root** in AI tool | Manny | [ ] |
| 1.2 | Read `CHH-ROADMAP.md`, `CHH-DEPLOYMENT-OPTIONS.md`, `ENTRY.md` | Team | [ ] |
| 1.3 | Run demo boot: `I am working on demo-lsri-workbench-2026` | Team | [ ] |
| 1.4 | Copy `raw/proposals/_template-chh-rfp/` → `<first-real-slug>/` | Curator | [ ] |
| 1.5 | Copy **one real internal RFP** subset from Drive → new workbench | Curator | [ ] |
| 1.6 | Fill `DECISION-CHART.md` + `DONOR-DOSSIER.md` stubs | Curator + PI | [ ] |
| 1.7 | **HERA half-day setup** (boot phrases, red-team, Drive path) | Berktuğ | [ ] |

---

## Week 2 — First draft cycle

| # | Task | Owner | Done |
|---|------|-------|------|
| 2.1 | Boot: `I am working on <slug>` — confirm locks + blockers | PI / writer | [ ] |
| 2.2 | Draft **one section** via `skills/grant-writer/SKILL.md` | Writer | [ ] |
| 2.3 | Run `skills/grant-red-team-reviewer/SKILL.md` before paste | Writer | [ ] |
| 2.4 | Log feedback in `REVISION-LOG.md` | Curator | [ ] |
| 2.5 | Land **one** grant email via `chh-sop-email-population.md` | Curator | [ ] |

---

## Week 3 — Context layers (parallel, low effort)

| # | Task | Owner | Done |
|---|------|-------|------|
| 3.1 | Run `chh-sop-meeting-prep.md` once (daily agenda paste) | Paul or staff | [ ] |
| 3.2 | Land **one** Fireflies export via `chh-sop-fireflies-landing.md` | Curator | [ ] |
| 3.3 | Promote one durable fact to `wiki/` (curator approves) | Curator | [ ] |

---

## Week 4 — Measure & review

| # | Task | Owner | Done |
|---|------|-------|------|
| 4.1 | Record **baseline vs post-Cortex** time for same section type | CHH | [ ] |
| 4.2 | Confirm **100% external paste** human-approved | Curator | [ ] |
| 4.3 | Joint 30-min review: Paul, Manny, William, Berktuğ | All | [ ] |
| 4.4 | Decide: extend pilot · MoU draft · Phase 3 IT petition | Paul | [ ] |

---

## Success criteria (pilot)

| Metric | Target |
|--------|--------|
| One workflow live | Internal RFP packaging |
| Curator gate | No unapproved external paste |
| Shared memory | Next session reads prior `REVISION-LOG` without re-brief |
| IT incidents | Zero PHI in git |

---

## Honest limits (repeat to sponsors)

| Capability | Phase 1 |
|------------|---------|
| Grant workbench + red-team | Yes |
| Drive / local proposal sync | Yes |
| Manual email / calendar / Fireflies SOPs | Yes |
| Outlook OAuth | No |
| Background automation bots | No |

---

## Handoff after Phase 1

- **Phase 2:** Scale SOPs; second workbench if first succeeds
- **Phase 3:** Manny + William IT track — see `CHH-DEPLOYMENT-OPTIONS.md`
- **Support:** berktug@heradigitalhealth.org

## Source(s)

- `CHH-DEPLOYMENT-OPTIONS.md`
- `wiki/partnerships/chh.md`
- MoU success metrics — HERA internal brief
