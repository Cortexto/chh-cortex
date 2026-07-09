---
name: CMU + Google AI Partnership — Somalia Maternal Health
description: Consortium (HERA + CMU LTI + Johns Hopkins + SORDI) for Google AI for Government proposal. Ethnographic study design, LLM fine-tuning, government dashboard. $1–3M, 30 months.
type: partnership
status: active
formation_date: 2026-03-24
project: connect2care-google-org
partners:
  - HERA Digital Health
  - Carnegie Mellon University (LTI)
  - Johns Hopkins Center for Humanitarian Health
  - SORDI (Somalia)
  - Somalia Ministry of Health
archive: memory/partnerships/cmu-google-ai-somalia-2026.md
tags:
  - partnership
  - partnership/academic
---

# CMU + Google AI Partnership — Somalia

## Partnership Structure
**Consortium forming** for Google AI for Government Innovation proposal (deadline: April 3, 2026).

## Roles

| Organization | Role | Key People |
|---|---|---|
| **HERA** | Product/platform lead, WhatsApp deployment, dashboard | Berktuğ, Sara |
| **CMU LTI** | Ethnographic study design, cultural alignment, LLM fine-tuning | Mai Alkhamissi (anthropologist), Vasudha Varadarajan (CS), Mona Dieb (PI) |
| **Johns Hopkins** | Field liaison, project management, publications | Shatha Elnakib, Sheri Morgan |
| **SORDI** | Somalia field partner, data collection, local context, gov relations | TBD |
| **Somalia MoH** | Official facility registry, EPI schedule, ANC protocol | TBD |

## Project Scope
Maternal and child health support via:
- **WhatsApp (Side A)**: pregnancy tracking, ANC reminders, vaccination calculator, facility locator, personal health record
- **Government dashboard (Side B)**: demand-side analytics, gap identification, service utilization metrics

## CMU Contributions

**Mai Alkhamissi (Anthropologist)**:
- Ethnographic study design for Somali maternal health context
- Train local field researchers (virtual + pilot)
- Qualitative data: symptom descriptions, cultural barriers, healthcare trust
- Deliver machine-readable dataset for RAG/fine-tuning

**Vasudha Varadarajan (CS)**:
- LLM fine-tuning technical work
- Social intelligence improvements for chatbot
- Mental health red-flag detection frameworks
- Convert qualitative data → machine-readable format

## Critical Blockers (as of March 24)

1. **SORDI data urgently needed**:
   - WhatsApp penetration rates by region
   - Internet/smartphone distribution
   - Geographic scope (accessible vs. hard-to-reach)
   - Government relationship + MoH integration feasibility

2. **CMU resource confirmation**:
   - GPU computing capacity for fine-tuning
   - Postdoc availability
   - IRB/ethics approval timeline

3. **Budget allocation**:
   - Google requires 80% to implementing partner (SORDI)
   - CMU + HERA + JHU share 20%
   - Vertex credits available for Google Cloud

## Timeline
- **March 25**: Sara + Mai + Vasudha meet with Mona Dieb to scope CMU contribution
- **~March 29**: SORDI to provide field context data
- **April 3**: Proposal deadline

## Technical Stack
- **LLM**: Google Gemini (funder requirement)
- **RAG**: Retrieval Augmented Generation for cultural context
- **Fine-tuning**: Based on ethnographic field data
- **Safety monitoring**: Langfuse for red-flag detection (mental health, domestic violence, medical urgency)

## Key Framing
- **Cultural differentiator**: Not just translated, but culturally aware
- **Recruitment strategy**: Need to include both users and non-users of the system
- **Implementation**: Virtual training + local researchers preferred over external researchers

## Status
- **Current**: Partnership forming, proposal drafting
- **Outcome**: Pending (proposal due April 3, 2026)

## Full Documentation
[[memory/partnerships/cmu-google-ai-somalia-2026.md]]

## Links

→ Project: [[connect2care-google-org]]
→ Full partnership file: [[academic]]
→ Tech decisions: [[003-cmu-somalia-architecture]] · [[004-data-privacy-phi-response]]
→ Tech: [[amti-capabilities]] · [[langfuse-observability]] · [[architecture]]
→ People: [[berktug]] · [[aral]]
→ Evidence: [[key-statistics]] · [[proof-points]]
→ Donor context: [[ai-technical]] · [[institutional]]
