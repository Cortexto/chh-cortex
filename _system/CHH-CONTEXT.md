---
name: CHH Cortex — Context & roadmap
description: What CHH Cortex is, Paul pain-point mapping, contextual awareness, email population, and product arc
type: system
updated: 2026-07-09
---

# CHH Cortex — Context & roadmap

This document explains **what we are building**, **why it matches CHH’s stated pain points** (Jul 2026 demo), and **what comes next**. It complements the tactical guides `CHH-INSTALL.md` and `CHH-CAPABILITIES.md`.

## What this is

**CHH Cortex** is a **shared institutional memory** for grant and research packaging at the Center for Humanitarian Health.

It is not a chatbot with hidden memory. It is a **folder of plain markdown files** — proposals, meeting notes, selected emails, people context, donor criteria — that your team and an approved AI assistant read together, session after session.

**Contextual awareness** means: when someone works on an RFP or prepares for a meeting, the system already knows CHH pilot scope, relevant people, prior decisions, and what was already drafted — because that knowledge lives in the vault, not in one person’s chat history.

---

## Paul & CHH pain points → Cortex layers

Mapped from the Jul 8, 2026 demo (Paul Spiegel, William Weiss). **Honest about IT limits.**

| Pain (their words) | Blocker today | Cortex layer | Pilot (now) | Building toward |
|--------------------|---------------|--------------|-------------|-----------------|
| **“Can’t give AI my Outlook calendar — iCal export is killing me”** | Hopkins blocks AI OAuth to Outlook | **Meeting & calendar context** | Manual iCal or agenda paste → `raw/meetings/`; triage skill | Standing “daily brief” template from pasted calendar; optional Gmail-invite workaround (center decision) |
| **“Want email in the knowledge base — who did we already talk to?”** | Same IT block on mailbox OAuth | **Email population** | Curator selects threads → land in `raw/email/` → triage → wiki | Curated forward/BCC to a CHH capture address or Drive drop; **no full mailbox scrape** without IT |
| **“I forget what we decided in a meeting months ago”** | No shared searchable memory | **Contextual retrieval** | Searchable `raw/` + `wiki/`; boot grant by slug | Cross-link meetings ↔ workbenches ↔ people cards |
| **“Hell of a lot of time on proposals”** | Fragmented drafts, no reuse | **Tailored grant tool** | Workbench per RFP + red-team gate | CHH canonical blocks + reviewer lessons library |
| **“Many departments applying — don’t know who’s involved”** | Siloed inboxes | **People & correlation layer** | `wiki/entities/people/` + meeting/email triage | “Who touched this funder?” view from promoted wiki facts |
| **“Claude + ChatGPT — no shared memory”** | Multiple tools, no ledger | **Single vault** | One git or synced folder for center | Same; institution owns files |
| **“Can’t access Dropbox / SharePoint with AI”** | Institutional file walls | **File landing zone** | Google Drive or local folder → curator copies into `raw/` | Scheduled sync of **approved** proposal folders only |
| **“Hopkins GPT forgets every 30 days”** | Session-bound cloud brain | **File-first memory** | Markdown in repo/Drive outlives any AI product | Same |
| **Proposal-first vs personal calendar automation** | William aligned with Paul | **Pilot priority** | **RFP packaging default** | Email/meeting layers support grants, not replace IT policy |

---

## Layer 1 — Meeting & calendar context

**Paul’s need:** Daily meeting prep and briefs without OAuth to Outlook.

**Now:**

1. Export day or week from Outlook (iCal or copy agenda text).
2. Paste into `raw/meetings/YYYY-MM-DD_prep.md` (see `_template/`).
3. Run `skills/transcript-triage/SKILL.md` — extract people, decisions, grant mentions.
4. Curator promotes durable facts to `wiki/`.

**Contextual awareness:** Next grant boot or “what did we say about X?” reads landed meetings, not chat memory.

**Future (Phase 2–3):** Optional Gmail calendar mirror if center approves the hassle; templated “meeting brief” skill that only uses **pasted** calendar text — still no Hopkins OAuth promise.

---

## Layer 2 — Email population (Paul priority)

**Paul’s need:** Email threads feed the same brain as meetings and proposals — “did you read this email?” level awareness, without exposing the full mailbox to AI.

**Principles:**

- **Curator-selected only** — no automated full inbox ingest in pilot.
- **No PII/PHI** in shared git; redact before landing when needed.
- **Context over volume** — one grant-related thread beats archiving every message.

**Now (manual population):**

1. Curator forwards or copies **selected** threads (grant invites, PI feedback, partner coordination).
2. Save as markdown in `raw/email/` using `raw/email/README.md` naming convention.
3. Run triage → propose tasks, people updates, workbench notes.
4. Link to active workbench: note in `REVISION-LOG.md` or `DECISION-CHART.md` under open items.

**Contextual awareness example:**

> “Boot `my-grant-2026` — incorporate context from the Yazdi email thread landed last week.”

Assistant reads `raw/email/`, people cards, and workbench files together.

**Phase 2 — Curated capture (no OAuth):**

- Dedicated CHH address or shared mailbox **folder** staff forward into.
- Manny exports folder weekly → markdown → `raw/email/` (human step, IT-friendly).
- Or: BCC line on **grant-related** outbound only (policy TBD with William).

**Phase 3 — MoU + IT review:**

- Hopkins-approved path for **read-only** export from Outlook (if any exists for center).
- Still curator-gated promotion to shared vault.
- Email **metadata** (subject, date, parties) in wiki; body in `raw/` with access control.

**We will not promise** live Outlook/Claude OAuth in partner docs until CHH IT signs off.

---

## Layer 3 — Tailored grant packaging tool

**Vision:** A **CHH-specific grant environment** — not generic AI prose.

| Component | Purpose |
|-----------|---------|
| **Workbench** (`raw/proposals/<slug>/`) | One folder per RFP: locks, dossier, skeleton, revision log |
| **Boot phrase** | “I am working on [slug]” pulls decision chart + dossier + linked raw context |
| **Red-team gate** | Reviewer stress-test before paste |
| **Reviewer lessons library** | Promoted rules from past cycles (see Layer 5) |
| **Canonical blocks** (future) | Approved IRB, methods, center boilerplate — fact-locked |

Maps directly to **proposal load** and **reuse** pain points.

---

## Layer 4 — People, proposals, and “who’s already involved”

William’s demo question: *what data does the model actually see?*

**CHH answer in pilot:**

- Landed **meetings** and **selected emails** in `raw/`
- **People cards** in `wiki/entities/people/`
- **Active grant workbenches** in `raw/proposals/`
- **Curated wiki** facts with `Source(s)` — not the whole SharePoint tree

Triage proposes updates when a thread mentions a new partner or an existing funder — curator approves before wiki promotion.

---

## Layer 5 — Institutional learning (patterns without jargon)

Internally HERA uses pattern libraries and quality loops. **CHH-facing names:**

| Internal concept | CHH name |
|------------------|----------|
| Pattern cards | **Reviewer lessons** — repeatable writing rules |
| Correction → wiki | **Quality feedback cycle** |
| Donor dossier kill list | **Must-prove / kill list** per workbench |

**Cycle:**

```
Draft → review → feedback
  → REVISION-LOG (what + why)
  → curator promotes reusable rule to wiki or dossier template
  → next grant boot applies it
```

**Pilot:** Manual promotion via `skills/knowledge-curator/SKILL.md`.

**Future:** `wiki/chh-reviewer-lessons.md` index; optional “this paragraph matched a failed pattern” suggestions — curator always approves.

---

## Layer 6 — Files, Drive, and institutional ownership

**Paul’s preference:** Memory on a **center-owned Mac or folder**, not a proprietary cloud brain.

| Source | Pilot path |
|--------|------------|
| SharePoint / consolidated proposals | Manny syncs subset to Drive → curator copies to `raw/proposals/` |
| Dropbox | Not AI-connected; export/copy into landed folder |
| Hopkins GPT | Optional for IT-approved tasks; **Cortex files persist** when GPT sessions reset |

---

## Roadmap phases

### Phase 1 — Now (lite repo live)

- Grant workbench + example RFP
- Manual meeting + **email population** into `raw/`
- Triage + curator + red-team
- Tool-neutral install (folder or git)

### Phase 2 — Pilot operations (post–Manny call)

- Dedicated CHH Mac or Drive workflow
- First **live** grant workbenches
- Weekly curator rhythm: raw → wiki
- Email capture SOP (forward/export → `raw/email/`)
- Seed **reviewer lessons** from first revision cycles

### Phase 3 — MoU + IT

- Canonical CHH blocks for IRB / methods
- Curated proposal corpus sync
- Hopkins-reviewed email export path (if available)
- Documented quality feedback cycle

### Phase 4 — Aspirational (not dated)

- Cross-grant search (“what did we promise funder X?”)
- Richer email↔meeting↔grant **correlation views** (curator-promoted facts only — **not** automated person-observation or negotiation-intel mining)
- Calendar assist **only if** IT approves a compliant path

**HERA-maintained intelligence (not in CHH lite pilot):** usage-learning loops, inter-person signal extraction, and automated stale-fact archival run in full HERA Cortex (`wiki/principles/cortex-collective-brain.md`). CHH benefits via maintainer re-sync of **reviewer lessons** and workflow patterns — not live person-analytics bots.

**Pilot guardrails (non-negotiable):** no person-observation mining, no negotiation-intel wiki pages, no promoting psychological profiles from meetings — only **decision facts**, **task candidates**, and **grant-linked context** with curator approval (see `skills/transcript-triage/SKILL.md`, `skills/knowledge-curator/SKILL.md`, `skills/chh-onboarding/SKILL.md`).

---

## HERA full vision ↔ CHH lite (honest map)

| Capability | CHH lite (now) | Full HERA Cortex |
|------------|----------------|------------------|
| Contextual awareness at grant boot | ✓ vault + workbench + landed raw | ✓ + automation agents |
| Learn from corrections / usage | Manual REVISION-LOG → reviewer lessons | collective-brain-reflection, grant-tone-miner, capture-check |
| Inter-person dynamics from meetings | Triage → people/decision facts only | incoming-message-reader, person signals (internal) |
| Noise reduction / keep current | Curator + triage classify `noise` | triage matrix scoring, dedup, supersede rows, freshness gates |
| Latest papers / conferences in context | Manual land in `raw/` + wiki | Same + intake automations (HERA-side) |

---

## Roles

| Party | Role |
|-------|------|
| **CHH** | Data ownership, curator, IT compliance, email/meeting selection policy |
| **HERA Digital Health** | Pattern maintenance, sanitized repo updates, training |
| **Approved AI tool** | Reads vault; never replaces curator or paste approval |

**Support:** Berktuğ Kubuk — berktug@heradigitalhealth.org

---

## One paragraph for sponsors (Paul / William)

> CHH Cortex gives the center a **durable markdown brain**: grant workbenches, **curator-selected email and meeting capture**, and review gates before paste. It addresses Paul’s core pains — **proposal load, forgotten meeting context, and no memory between AI tools** — with file-first storage Hopkins IT can tolerate. Full Outlook automation stays **out of scope until IT approves**; we start with manual population and build toward curated email capture and a **tailored CHH grant tool** with reviewer lessons that improve every cycle.

## Source(s)

- Jul 8, 2026 CHH Cortex demo (transcript held in HERA maintainer vault — not shipped to partner repo)
- `wiki/partnerships/chh.md` (export copy)
