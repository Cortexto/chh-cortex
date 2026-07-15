---
name: LSRI hypothesis brief
type: working-draft
status: draft — fusion LSRI-H005 proposed 2026-07-13; verify with Shatha + Aral before locking
updated: 2026-07-13
demo_lean: Fusion LSRI-H005 (Fork C frame + Fork B method)
---

# JHU LSRI — Hypothesis Brief

**Purpose:** Working document for Shatha + Aral alignment and CHH Cortex demo (8 Jul). **Not** the final 4-page PDF — Shatha owns narrative submission.

**Status:** Hypothesis **not locked**. Demo presents both forks; working lean = **Fork B** per Aral emphasis on 2026-07-02 call — **`verify with Aral`** before stating as final on the call.

---

## Shatha gates (must pass either fork)

| Gate | Requirement | How we answer |
|------|-------------|---------------|
| **AI mandatory** | Must include AI / data science | Both forks: AI analytics, NLP, or product AI |
| **Life-science / biomedical** | Lean medical, not pure ops | **Maternal / reproductive health** bridge in displaced populations |
| **Novelty** | Big and new vs current HERA ops | Fork A: weaker unless sharpened; **Fork B: conversational data modality vs Kobo** |
| **Student benefit** | Money to trainees, not only faculty | **Aral DrPH trainee** + dissertation thread |
| **Multidiscipline** | Cross-faculty team | Shatha (CHH) + **Yazdi (CBID)** target |

---

## Fork A — Product / intervention

**One-liner:** Expand AI inside HERA's maternal and newborn health modules for displaced populations — product innovation lane.

| Dimension | Content |
|-----------|---------|
| **Scientific claim** | AI-assisted maternal health support improves engagement or outcomes in crisis settings |
| **Novelty** | Incremental unless tied to new clinical module or population — **needs sharpening** |
| **JHU role** | CHH evaluation design, outcome measurement, publication |
| **HERA role** | Product + ops; likely **in-kind** given ≤10% cap |
| **Risks** | Sounds like "more of what HERA already does"; product delivery burden on narrative |

**Shatha gate fit:** AI ✓ · Biomedical bridge ✓ · Novelty **weak** unless hybrid with data science angle.

---

## Fork B — Conversational intelligence (demo lean)

**One-liner:** Analyze de-identified humanitarian health conversations at scale as a **novel data-collection modality** — versus survey-only tools (e.g. Kobo) — filling a **refugee-specific gap** in chatbot-health literature.

| Dimension | Content |
|-----------|---------|
| **Scientific claim** | Conversational data reveal health-seeking patterns, barriers, and symptom narratives surveys miss — refugee/displacement populations under-studied vs generic Nature chatbot-health papers |
| **Novelty** | **Latent asset** — conversations already exist in HERA ops; science is **usage intelligence + methods**, not greenfield product |
| **JHU role** | CHH leads study design, ethics/IRB, analysis, publication; compute on JHU |
| **HERA role** | De-identified data access partnership; **≤10% subaward** or in-kind technical support |
| **Aral trainee** | DrPH dissertation thread on conversational data in humanitarian crises; comp exams Jul 2026 |
| **Risks** | IRB/privacy framing; corpus size **`verify`**; must link to health outcomes, not tooling-only grant |

**Shatha gate fit:** AI ✓ · Biomedical bridge ✓ · Novelty **strongest** · Lower field-build burden on JHU.

**Aral framing (Jul 2):** *"Conversational data collection and intelligence in a humanitarian crisis setting"* — contrast with Kobo as survey-form incumbent.

---

## Hybrid option (if Aral prefers)

Product outcomes **plus** conversational analytics as **evaluation layer** — maternal module as intervention, conversation logs as implementation-science dataset. Tighter 4-page fit if Fork B alone reads too methods-heavy.

**Owner to decide:** Aral + Berktuğ before narrative v1.

---

## Fusion — LSRI-H005 (proposed 2026-07-13, red-team session)

**Resolves B vs C: Fork C is the frame, Fork B is the method.** Reviewer-simulation scores: invisible-demand science 7/10 · chat-vs-survey benchmark 5/10 (demote to sub-task) · CBID prototype 4/10 standalone, 8/10 as component · follow-on pipeline 3/10 standalone (paragraph only).

> **Hypothesis:** conversational data from an operating digital health service can identify why refugee women miss care, and a PI-designed measurement layer embedded in that service can validly measure self-reported utilization.

| Aim | Content | Depends on |
|-----|---------|------------|
| **1** | Governed pipeline + **PI-designed self-report measurement layer** (wording, timing, flow placement under study protocol) + nested validation sub-study. Corpus with annotation protocols = deliverable (trainee gate, structural). Survey benchmark = sub-task, not aim | Live Türkiye service — no partners needed |
| **2** | Barrier discovery + **pre-clinic drop-off measurement** + explicit **selection-function modeling** (who conversational data sees vs misses — the fatal critique converted into the novel science) | Aim 1 pipeline |
| **3** | Bounded CBID rapid design cycle on top validated barrier; **pre-specify fallback barrier from DIV evidence** so aim isn't hostage to Aim 2 timing | Yazdi role scoping |
| **Exploratory** | CHH-led facility linkage pilot (2–3 sites recruited via CHH networks) — **pending Shatha yes/no**; Istanbul 2023 = prior-collaboration rationale (identifier failure → DIV H3 → this develops the fix) | Shatha network answer |

**Maturity gradient (feasibility spine):** structured in-service self-report (*exists — 3 loops, founder-confirmed 2026-07-13*) → PI-designed instrument + validation (*this grant*) → facility linkage pilot (*exploratory*) → causal trial (*DIV/FID follow-on — criterion-5 paragraph only, overlap disclosed in current/pending support*).

### Product basis (founder-confirmed 2026-07-13 — numbers `verify`)

Three reminder → push → in-chat structured self-report loops live in product: **template 1** vaccination (host-country schedule auto-calc; caregiver confirms attendance + vaccines given) · **template 2** pregnancy check-up attendance · **template 3** health-services access. Source: `raw/capture-logs/2026-07-13-lsri-self-report-loops-product-confirmation.md`. **Verify before quoting figures:** response rate per template · window/denominators · storage format · export/de-ID path.

### Hard constraints (registered 2026-07-13)

1. **No active clinic connection anywhere** — linkage never claimed as capability; exploratory aim or cut
2. **No AMTI name** in this proposal
3. **HERA back-staged** — describe by function (*"WhatsApp-based maternal and child health navigation service operated by a nonprofit platform partner in Türkiye"*); HERA named once, ≤10% lane
4. **No unverified figures** in narrative

### Aim 1 draft language (JHU register)

> **Aim 1.** Establish a governed pipeline for routinely generated conversational and self-reported utilization data from an operating digital health service. The study will draw on a WhatsApp-based maternal and child health navigation service operated by a nonprofit platform partner in Türkiye, which currently serves Arabic-speaking refugee women and embeds structured follow-up cycles into routine care navigation: host-country-specific vaccination schedules with caregiver-confirmed attendance, antenatal check-up reminders with attendance confirmation, and periodic health-service access questions. The research team will (a) design and prospectively deploy a refined outcome-measurement layer within these existing service flows, specifying question wording, timing, and flow placement under the study protocol; (b) establish de-identification and data-governance procedures for secondary analysis of the accumulated service data; and (c) assess the measurement properties of in-service self-report through a nested validation sub-study.

**New Shatha-call agenda item:** *"Can CHH realistically bring 2–3 facility partners for a linkage pilot — yes or no?"* — decides exploratory aim vs cut.

---

## Team stack (locked direction)

| Role | Person | Status |
|------|--------|--------|
| Lead PI | **Shatha Elnakib** | Confirmed Jul 2 |
| Co-PI (target) | **Youseph Yazdi** (CBID) | **Soft yes 2026-07-07** — student/faculty roles TBD; not committed co-PI |
| Trainee | **Aral Surmeli** | Confirmed — **not co-PI** |
| HERA support | **Berktuğ Kubuk** | Drafting + package assembly |

**Roster discipline:** No extra maternal faculty — keep small (Aral + Shatha + Yazdi).

---

## Budget implication (≤10% subaward)

| Award | Max HERA external line |
|-------|------------------------|
| $200k | ≤$20k |
| $300k | ≤$30k |
| $500k | ≤$50k |

**Realistic models:**

1. **In-kind** HERA ops + JHU-funded CHH analysis staff
2. **≤10%** HERA service contract (de-identification pipeline, API access, technical deliverables)
3. **Follow-on** DIV / external grant for implementation scale

**Open:** Service contract vs subaward distinction — **`verify` with Shatha / JHURA**.

---

## Demo talking point (CHH audience)

*"This is a real in-flight JHU internal RFP we're packaging in Cortex — same workflow CHH could use for your RFAs: lock route, map reviewer criteria, draft from facts, capture corrections permanently."*

Name LSRI as **worked example**; do **not** oversell submit certainty or disclose internal negotiation detail.

---

## Next actions

| # | Action | Owner |
|---|--------|-------|
| 1 | Aral sends hypothesis bullets | Aral |
| 2 | Lock A / B / hybrid | Aral + Berktuğ |
| 3 | Yazdi role scoping (soft yes received) | Aral + Shatha |
| 4 | Shatha drafts 4-page PDF from `lsri-narrative-skeleton.md` | Shatha |
| 5 | Budget Excel (InfoReady template) | Shatha / JHURA |

## Source(s)

- `wiki/concepts/decisions/2026-07-02-jhu-lsri-individual-award-strategy.md`
- `raw/meetings/2026-07-02_jhu-research-funding-opportunities-shatha-call-transcript.md`
- `DECISION-CHART.md`
