---
name: CHH Cortex — Roadmap & guide
description: Start here — pain points, contextual awareness, email population, learning loop, tailored grant tool, phases
type: guide
updated: 2026-07-15
---

# CHH Cortex — Roadmap & guide

**Read this first** on GitHub — Paul, William, Manny, CHH staff.  
Install: `_system/CHH-INSTALL.md` · **Deployment:** `CHH-DEPLOYMENT-OPTIONS.md` · **Phase 1:** `_system/CHH-PHASE1-PLAYBOOK.md` · Demo: `raw/proposals/demo-lsri-workbench-2026/DEMO-READ-ME-FIRST.md`

> **Note:** Content from the old CHH-CONTEXT doc (removed in v0.3) is **here** at repo root.

---

## What this is

CHH Cortex is a **shared folder of markdown files** — grant workbenches, meeting notes, selected emails, people context — that your team and an approved AI assistant read together every session.

It is **not** a chatbot with hidden memory.

**Contextual awareness** means: when someone works on an RFP or prepares for a meeting, the system already knows CHH pilot scope, relevant people, prior decisions, and what was already drafted — because that knowledge lives in the vault, not in one person’s chat history.

**Example boot:**

```
I am working on demo-lsri-workbench-2026 — incorporate context from any landed email about this grant.
```

The assistant reads workbench files + `raw/email/` + people cards together — not chat memory.

---

## Raw vs wiki — the two layers

| | **`raw/`** | **`wiki/`** |
|---|-----------|-------------|
| **Plain English** | **Inbox & working files** — everything as it arrived | **Approved facts** — what the center trusts as current truth |
| **Examples** | Email paste, meeting transcript, RFP notes, drafts | People cards, partnership rules, **reviewer lessons** |
| **Who writes** | Anyone can land; curator selects what enters | **Curator approves** promotions from raw |
| **Rule** | Append-only — do not silently edit sources | Every fact needs **Source(s)** pointing to raw |
| **Stale info** | Kept for audit trail | Curator **updates or supersedes** when facts change |

**Flow:** land in `raw/` → triage → curator approves → promote to `wiki/` → next grant boot reads both.

Workflows: `wiki/concepts/workflow/chh-workflows-guide.md`

---

## What hurts today → what Cortex does

| What you feel | Why it is hard | **Now** (pilot) | **Later** (IT / MoU) |
|---------------|----------------|-----------------|----------------------|
| **Calendar prep** — exporting Outlook for AI | Hopkins blocks AI OAuth to Outlook | Paste day/week (iCal or agenda) → `raw/meetings/` | Meeting brief template from **pasted** calendar only |
| **Email context** — who did we email? | Same IT block on mailbox | **Curator-selected** threads → `raw/email/` → triage → workbench link | Forward/export folder → markdown (human step) |
| **Forgotten meeting decisions** | No shared memory | Searchable vault + **boot by grant slug** | Meetings ↔ grants ↔ people linked in wiki |
| **Too much time on proposals** | Fragmented drafts | Workbench per RFP + red-team + revision log | Reviewer lessons library + canonical blocks |
| **Many departments — who is involved?** | Siloed inboxes | People cards + triage from email/meetings | “Who touched this funder?” from wiki |
| **Claude + ChatGPT — no shared memory** | Multiple tools | **One git or Drive folder** | Cross-tool ledger in workbench |
| **SharePoint / Dropbox not AI-readable** | File walls | Curator copies into `raw/` | Approved folder sync only |
| **Hopkins GPT forgets after 30 days** | Session-bound cloud | **File-first memory** | Same |

**Pilot priority:** grant packaging first. Email and meeting layers **support grants**.

**We will not promise** live Outlook OAuth until Hopkins IT signs off.

---

## Six layers (how the pieces fit)

### Layer 1 — Meeting & calendar context

**Paul’s need:** Daily prep without OAuth to Outlook.

1. Export day/week from Outlook (iCal or copy agenda text)
2. Paste → `raw/meetings/YYYY-MM-DD_<topic>.md`
3. Run `wiki/concepts/workflow/chh-sop-meeting-prep.md` or `skills/chh-meeting-prep/SKILL.md`
4. Run `skills/transcript-triage/SKILL.md` (optional weekly)
5. Curator promotes durable facts to `wiki/`

### Layer 2 — Email population (Paul priority)

**Paul’s need:** Email threads in the same brain as meetings and proposals.

**Principles:** curator-selected only · no PII/PHI in shared git · context over volume

**Now:**

1. Curator forwards/copies **selected** grant-related threads
2. Save → `raw/email/` (see `raw/email/README.md` frontmatter)
3. Run `wiki/concepts/workflow/chh-sop-email-population.md` → `skills/chh-email-triage/SKILL.md`
4. Link to workbench `REVISION-LOG.md` or `DECISION-CHART.md`

**Contextual awareness example:**

> Boot `my-grant-2026` — use the coordination email thread landed last week.

**Phase 2:** CHH capture address or folder staff forward into; periodic export to markdown.  
**Phase 3:** Hopkins-reviewed read-only export path — still curator-gated.

### Layer 3 — Tailored grant packaging tool

**Vision:** A **CHH-specific grant environment** — not generic AI prose.

| Component | Purpose |
|-----------|---------|
| **Workbench** (`raw/proposals/<slug>/`) | Decision chart, donor dossier, skeleton, revision log |
| **Boot phrase** | `I am working on [slug]` pulls locks + dossier + linked raw context |
| **Red-team gate** | Reviewer stress-test before paste |
| **Reviewer lessons library** | Promoted rules from past cycles (see below) |
| **Canonical blocks** (future) | Approved IRB, methods, center boilerplate |

**Demo:** `raw/proposals/demo-lsri-workbench-2026/` — full LSRI-shaped package (ledgers, portal pack, submission/).

### Layer 4 — People & “who’s already involved”

- Landed meetings and **selected emails** in `raw/`
- People cards in `wiki/entities/people/`
- Active workbenches in `raw/proposals/`
- Curated wiki with `Source(s)` — not the whole SharePoint tree

Triage proposes people updates; curator approves. **No** automated person-profiling or negotiation-intel mining.

### Layer 5 — Institutional learning (plain language)

| Internal (HERA — not CHH-facing) | **CHH name** |
|-----------------------------------|--------------|
| Pattern cards / activation index | **Reviewer lessons library** |
| Collective brain / capture from corrections | **Institutional learning loop** |
| Self-improvement automation | **Quality feedback cycle** |
| Grant-writer + dossier + red-team | **CHH grant packaging tool** |

**Pattern recognition — how it works:**

1. **Donor / committee lens** — each workbench keeps `DONOR-DOSSIER.md` (must-prove, kill list, tone)
2. **Revision memory** — feedback in `REVISION-LOG.md` with field + **reason**, not just rewritten text
3. **Promoted lessons** — curator moves reusable rules to `wiki/` (e.g. “life-sciences committee wants AI mechanism in paragraph two, not slide-deck hype”)
4. **Activation on draft** — grant workflow reads those files before generating prose

**Quality feedback cycle:**

```
Draft → review → committee/donor feedback
        ↓
REVISION-LOG (what + why)
        ↓
Curator: one-off fix OR promote to wiki / dossier template
        ↓
Next grant boot reads updated context
```

**Pilot:** manual promotion via `skills/knowledge-curator/SKILL.md`  
**Phase 2–3:** curated reviewer lessons index page in wiki (stub when pilot starts)  
**Phase 4:** optional “this matches a failed pattern on grant X — suggest rewrite?” — **curator always approves**

### Layer 6 — Files, Drive, institutional ownership

| Source | Pilot path |
|--------|------------|
| SharePoint / proposal folders | Manny syncs subset to Drive → curator copies to `raw/proposals/` |
| Dropbox | Export/copy into landed folder |
| Hopkins GPT | Optional for IT-approved tasks; **Cortex files persist** when GPT sessions reset |

---

## Tailored grant tool — product arc

| Layer | Now (lite) | Building toward |
|-------|------------|-----------------|
| Workbench | Folder per RFP | Live CHH packages with curator boot |
| Voice & committee | `chh-grant-voice.md` + dossier kill lists | JHU committee variants as approved blocks |
| Review gates | Red-team before paste | Optional internal “PI read” checklist |
| Evidence honesty | `verify` / `needs source` | CHH-approved stats in wiki |
| Reuse | `_template-chh-rfp/` | Fact-locked IRB / methods blocks |
| Contextual boot | `I am working on [slug]` | + meetings, emails, reviewer lessons |

**Not in scope:** replacing Hopkins GPT, auto-reading Outlook, unsupervised auto-submit.

---

## Included in this repo (use today)

| Capability | Where |
|------------|--------|
| Grant workbench | `raw/proposals/` |
| **Full LSRI demo** | `raw/proposals/demo-lsri-workbench-2026/` |
| Red-team | `skills/grant-red-team-reviewer/SKILL.md` |
| Email population | `raw/email/README.md`, `skills/chh-email-triage/SKILL.md` |
| Meeting triage | `skills/transcript-triage/SKILL.md` |
| Workflows (portal gate, donor lens, cross-tool) | `wiki/concepts/workflow/chh-workflows-guide.md` |
| Wiki promotion | `skills/knowledge-curator/SKILL.md` |
| People & pilot rules | `wiki/entities/people/`, `wiki/partnerships/chh.md` |

## Not in this repo

- Background automation bots, full HERA donor pipeline
- Heavy usage-mining across HERA’s full vault
- Maintainer build tools — **CHH only needs `Cortexto/chh-cortex`**

Updates arrive when HERA re-syncs this repo after curator approval.

---

## Try the demo (5 minutes)

1. `raw/proposals/demo-lsri-workbench-2026/DEMO-READ-ME-FIRST.md`
2. Browse the demo package — open questions board, cross-agent notes, portal fill pack, `submission/`
3. **`I am working on demo-lsri-workbench-2026`**

Some wiki links inside demo files will not resolve in CHH lite — expected.

---

## Roadmap phases (merged)

### Phase 1 — Now

- File-first workbench + manual lesson promotion
- Manual meeting + **email population**
- Grant tool = structured folders + skills (not a separate app)
- LSRI demo at full complexity

### Phase 2 — Pilot operations

- Dedicated CHH Mac or Drive workflow
- First **live** grant workbenches
- Email capture SOP; seed **reviewer lessons** from revision logs
- Optional reviewer lessons index in wiki (Phase 2)

### Phase 3 — MoU + IT

- CHH canonical blocks; proposal corpus sync
- Hopkins-reviewed email export (if available)
- Quality feedback cycle as documented SOP

### Phase 4 — Tailored product (aspirational)

- Boot → decode question → draft from blocks + dossier → red-team against lessons index → revision log → portal export
- Cross-grant search; richer email ↔ meeting ↔ grant links (**curator facts only**)

---

## One paragraph for sponsors (Paul / William)

> CHH Cortex gives the center a **durable markdown brain**: grant workbenches, **curator-selected email and meeting capture**, and review gates before paste. Drafts inherit **reviewer lessons from past cycles** (not generic AI advice), and a **quality feedback loop** turns PI and committee corrections into reusable rules. It addresses core pains — **proposal load, forgotten context, email awareness, and no memory between AI tools** — with file-first storage Hopkins IT can tolerate. Full Outlook automation stays out of scope until IT approves; the lite repo is step one — structured memory and gates.

---

## Roles

| Party | Role |
|-------|------|
| **CHH** | Data ownership, curator, IT compliance, email/meeting selection |
| **HERA Digital Health** | Pattern maintenance, sanitized repo updates, training |
| **Approved AI tool** | Reads vault; never replaces curator or paste approval |

**Support:** Berktuğ Kubuk — berktug@heradigitalhealth.org
