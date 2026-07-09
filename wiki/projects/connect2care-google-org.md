---
name: Connect2Care (Google.org AI for Government — Somalia MNCH)
description: Connect2Care — Somalia MNCH WhatsApp + MoH-side platform (Google.org AI for Government). Canonical project wiki; consortium, reach, tech, partner roles. CMU-only notes — [[cmu-google-ai-somalia]].
type: project
status: submitted
donor: Google.org AI for Government
ask: $1–3M
duration: 30 months
geography: Somalia (Mogadishu, Dhusamareb, Kismayo)
lead: HERA (tech)
partners: SORDI, CMU, JHU, Somalia MoH
voice: technical-ops
migrated_from: memory/projects/sahan-google.md
renamed_from_wiki_slug: sahan-google-org-ai
tags:
  - project
  - project/ai
  - connect2care
updated: 2026-05-14
---

# Connect2Care (Google.org AI for Government)

**Canonical project page:** [[connect2care-google-org]] — do not maintain a second programme home under `wiki/partnerships/`; use [[cmu-google-ai-somalia]] for CMU-only rows.

## Project Overview
Two-sided digital health platform for Somalia maternal, newborn, and child health (MNCH).

**Side A**: Women & families (WhatsApp-native, Somali + Arabic, no download)
**Side B**: Healthcare personnel & MoH dashboard (web-based, role-based access)

## Core Innovation Claim
HERA captures **demand-side data** that national health information systems (DHIS2) structurally cannot see:
- Who isn't reaching facilities (pre-facility demand)
- Why women miss appointments
- Geographic gaps in coverage
- Unmet need patterns by district

This complements (not replaces) DHIS2 supply-side data.

## Partner Responsibilities
| Partner | Role |
|---------|------|
| HERA | WhatsApp adaptation, Side B dashboard, closed-loop system, Langfuse, Gemini integration |
| SORDI | Facility enumeration, MoH relationship, healthcare provider onboarding, co-design, ethnographic data |
| CMU ([[mona-dieb]]) | Advisory — prompt engineering review, red flag taxonomy, ethnographic study design. NO fine-tuning, NO RAG, NO custom model. |
| JHU | Independent evaluation, grant management, Google.org relationship |
| Somalia MoH | Facility registry, EPI schedule, ANC protocol, content |

## Key Design Decisions
- **Literacy barrier response**: Structured menu navigation (select from options, no typing) for all user flows + facility-based assisted onboarding
- **Voice interaction**: NOT promised — Somali ASR not commercially viable without custom model; CMU advisory only
- **DHIS2 integration**: One-directional push of anonymized aggregate data via API
- **Data sovereignty**: WhatsApp/Gemini layers do NOT have HIPAA BAA (backend/AWS only)

## Technical architecture (submission-canon vs. March meeting)

- **Submission-canon (portal / partner comms):** Gemini on Vertex; Twilio; Django/Postgres; Langfuse; DHIS2-linked workflows; CMU = safety, alignment, prompt/ethnographic design — **not** CMU-executed fine-tuning or a CMU-built RAG layer on HERA infra (see Partner table above).
- **March 2026 meeting capture** still useful for **history** (RAG framing, SMS fallback, partner table wording): [[2026-03-24-google-ai-somalia-architecture]]. If portal copy and that decision diverge, **treat this project page + landed portal notes as canonical** for external consistency.

## Reach numbers (two tracks — reconcile before comms)

**Internal / Trello conservative scaffold (early-phase planning):**

- Direct: 5,000–8,000 women on Side A across 2–3 cities
- Healthcare personnel at mapped MNCH facilities
- Somalia MoH and SORDI staff trained on Side B

**Application narrative (landed 2026-05-14 — verify against field + ethics):**

- Pilot framing toward **~50,000** pregnant women / mothers across **three federal member states** and **~40** primary health centres on DHIS2 (see portal notes in Source(s)).

## Full Documentation
Legacy reference: `memory/projects/sahan-google.md` (not present in this repo).

If you still have the source document, add it to `raw/proposals/` (or `raw/drafts/`) and link it here.

## Status
- **Product / programme name:** Connect2Care
- **Current**: Portal submitted April 2026; extended form fields + ethics/M&E blocks landed in `raw/capture-logs/2026-05-14-connect2care-google-org-ai-for-government-application-notes.md` (**verify** before reuse)
- **Next**: Q24 (ethical risks) — use tech-decisions/004 as base
- **Pending confirmations**: Structured menus feasibility, DHIS2 API integration scope, reach numbers (pick one track above), facility staff cadres for onboarding
- **Funder timing (2026-05-05 call):** team expects **no Google.org decision for a few more months**; informal mention of evaluation activity through **late Aug–Sep** — **reconcile with official Google materials** before relying on dates externally (`TASKS.md` Shared This Week / DIV–Google bundle). Source: `raw/meetings/2026-05-05_shatha-elnakib-aral-berktug-granola-export.md`.

## DIV Reuse Note — May 2026

The 2026-05-05 Shatha/JHU call made clear that a Somalia DIV pitch should **not** simply shrink this Google.org concept. For DIV Stage 1 / pilot framing, reuse the Somalia partner logic and demand-side theory of change, but strip the scope down to a small women-focused proof of concept:

- demand-side only;
- no full provider dashboard / supply-side build in the first pass;
- one bounded geography or region;
- realistic reach, partner stack, and MoH involvement that fit a **USD 200k** pilot ceiling.

Source: `raw/meetings/2026-05-05_shatha-aral-div-rwjf-transcript.md` · `raw/meetings/2026-05-05_shatha-elnakib-aral-berktug-granola-export.md`

Later same-day internal note: the Somalia DIV lane remains useful as a possible Stage 1/pilot concept, but the evidence-heavy second lane is now leaning toward Syria with SAMS + JHU rather than staying equally split between Syria and Turkey. Keep the Somalia pitch small enough that it does not look like a second full Google.org-style system build.

Source: `raw/meetings/2026-05-05_aral-berktug-weekly-grants-followup-transcript.md`

## Trello planning snapshot — Connect2Care / Google.org Somalia chatbot

Trello card reviewed 2026-04-30: `Google.org: Somalia Chatbot`

Status caveat:

- Trello label: `Grant Status Unknown`
- Dates shown: Sep 1, 2026-Sep 1, 2027
- Treat this as roadmap planning context, not confirmed project delivery.

Tech implementation items listed in Trello:

- Configure Somali chatbot.
- Configure expected WhatsApp API setup.
- Configure known languages: Somali + Arabic.
- Configure provider-side dashboard for local partners and on-the-ground entry interface.
- Configure chatbot knowledge base.
- Configure Langfuse pipeline.
- Integrate SORDI facility database.

This aligns with the proposal architecture: Side A WhatsApp-native user flow, Side B provider/MoH dashboard, SORDI facility data, and Langfuse monitoring.

Source: `raw/capture-logs/2026-04-30-trello-product-roadmap-review.md`

## Links

→ Donor: [[institutional]] · [[ai-technical]]
→ People: [[aral]] · [[berktug]]
→ Partners: [[cmu-google-ai-somalia]] · [[academic]]
→ Tech: [[amti-capabilities]] · [[architecture]] · [[langfuse-observability]]
→ Tech decisions: [[003-cmu-somalia-architecture]] · [[004-data-privacy-phi-response]]
→ Evidence: [[key-statistics]] · [[proof-points]] · [[pilot-results]]
→ Patterns: [[010-anti-parallel-line]] · [[005-field-realism-over-tech-idealism]] · [[006-crisis-affected-women-and-girls]] · [[021-google-org-government-deployment-framing]] · [[023-never-mention-fallback-rate-externally]] · [[022-consortium-budget-not-org-budget]]
→ Principles: [[voice-dna]] · [[principles-full]]

## Application draft (Google.org portal)

Landed portal copy and extended form fields (sections II–III, ethics, M&E, scaling) — **internal; verify before reuse:**

- `raw/capture-logs/2026-05-14-connect2care-google-org-ai-for-government-application-notes.md`

## Source(s)

- `raw/capture-logs/2026-05-14-connect2care-google-org-ai-for-government-application-notes.md`
- `raw/capture-logs/2026-04-30-trello-product-roadmap-review.md`
- `raw/meetings/2026-05-05_shatha-aral-div-rwjf-transcript.md`
- `raw/meetings/2026-05-05_aral-berktug-weekly-grants-followup-transcript.md`
