---
name: CHH Cortex — Deployment options
description: Two-track plan for Paul's priorities — center Mac first; Outlook/Dropbox OAuth phased honestly
type: guide
updated: 2026-07-15
---

# CHH Cortex — Deployment options

**Read with:** `CHH-ROADMAP.md` · `CHH-DECISIONS.md` (Phase 0 status + file map) · `_system/CHH-INSTALL.md` · `_system/CHH-PHASE1-PLAYBOOK.md`

Paul's two priorities (Jul 2026): personal laptop context (Outlook, meetings) vs **center laptop** grant workflow. Related but **not the same problem** — see CD-002 in `CHH-DECISIONS.md`.

---

## Two lanes

| Lane | What you want | Hopkins reality | v1 answer |
|------|---------------|-----------------|-----------|
| **A — Personal laptop** | Daily meeting prep from Outlook + Fireflies | IT blocks AI OAuth to institutional mail/calendar | **Manual SOPs** — not live mailbox hooks |
| **B — Center laptop** | Shared grant memory on consolidated proposals | File-first vault + Drive works | **Start here** |

**Do not wait for Lane A to start Lane B.**

---

## Lane B — Center grant workflow (recommended v1)

| Option | Summary | Verdict |
|--------|---------|---------|
| **B1** | Dedicated **CHH Mac** + clone this repo + Claude Code / Cursor / **Antigravity** + Google Drive sync for proposals | **Recommended** |
| **B2** | Hopkins GPT + synced Google folder | IT-friendly fallback; sessions expire ~30 days |
| **B3** | Drive/ZIP folder only (Track A, no git) | Faculty adjunct — weaker shared ledger |
| **B4** | Personal Claude on every laptop | Defer — no shared center brain |

### Getting proposal files into the vault

Hopkins IT advice (William Weiss, Jul 8): **pull trusted data into one folder first.**

1. Export or selective-sync from SharePoint/Dropbox → **CHH Google Drive**
2. Curator copies **approved subset** → `raw/proposals/<slug>/`
3. AI reads the vault — not OAuth into Dropbox cloud

See `_system/CHH-PHASE1-PLAYBOOK.md` for week-by-week steps.

**Tools:** Cursor (demo) and **Antigravity** (Manny) both work — see `_system/CHH-INSTALL.md` § Antigravity for paste-boot.

**Live drafts vs this repo:** public `chh-cortex` = patterns + demo; **live RFP drafts → private repo or Drive** (CD-004).

---

## Lane A — Calendar, email, Fireflies (personal pain)

| Source | v1 path | SOP |
|--------|---------|-----|
| **Calendar** | Paste iCal or agenda text → meeting brief | `wiki/concepts/workflow/chh-sop-meeting-prep.md` |
| **Email** | Curator-selected threads only → `raw/email/` | `wiki/concepts/workflow/chh-sop-email-population.md` |
| **Fireflies** | Manual export → triage → link to grant | `wiki/concepts/workflow/chh-sop-fireflies-landing.md` |
| **Dropbox (personal)** | OAuth to AI | **Blocked** — use center Mac local sync instead |

### Optional (CHH decides — not v1 promise)

| Workaround | Effort | Notes |
|------------|--------|-------|
| Gmail shadow invite on every Outlook event | Ongoing | Double-calendar hassle — Paul was skeptical Jul 8 |
| Hopkins IT read-only OAuth exception | High | Manny leads; HERA advises architecture only |
| Fireflies API auto-land | Medium | Phase 3 — security review required |

---

## Phased rollout

### Phase 0 — Manny call (~45 min)

**Held 2026-07-15** — locked decisions and open items: `CHH-DECISIONS.md` (CD-001–CD-010 + § Open decisions).

### Phase 1 — Center pilot (weeks 1–4)

One CHH Mac, one live RFP workbench, one section through red-team + revision log.  
**Success:** visible time savings on proposal packaging without waiting on IT.

### Phase 2 — Manual context layers (weeks 2–8, parallel)

Run the three SOPs above; optional Gmail shadow calendar test.

### Phase 3 — IT track (months 2–6)

Manny + William: read-only export paths, MoU with HERA as tech lead.

### Phase 4 — Aspirational (IT approval only)

Partial auto-ingest, richer email ↔ meeting ↔ grant links — curator always approves.

---

## Cost sketch (CHH-owned, order of magnitude)

| Item | Notes |
|------|-------|
| CHH Mac | One-time procurement |
| Claude Team/Business | Per-seat; center billing preferred |
| Cursor | Optional — IDE parity with HERA demo |
| Google Drive | Likely existing |
| Fireflies | If center already subscribes |
| HERA setup | Half-day per MoU; repo updates via GitHub releases |

---

## One paragraph for sponsors

> The **center laptop path** gives CHH shared grant memory and packaging **now**, with files the center controls. Personal calendar and Outlook access need either **simple manual steps** (documented SOPs in this repo) or **Hopkins IT sign-off** — we map that with Manny and do not over-promise OAuth. Fireflies fits the same file-first pattern immediately via export.

---

## Support

Berktuğ Kubuk — berktug@heradigitalhealth.org
