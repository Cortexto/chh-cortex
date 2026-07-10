---
name: LSRI application narrative
type: submission-draft
status: canonical narrative (aims-first + team-source tailoring); Shatha PI confirmation + Aral review + budget confirmation + PDF layout gate before submission
updated: 2026-07-10
deadline: 2026-07-15 11:59 PM InfoReady
submit_owner: Shatha Elnakib (PI)
format: 4 pages max PDF (12pt, ½" margins; refs beyond)
---

# AI-Supported Digital Health Navigation and Conversational Analytics for Refugee Health Service Utilization

**Lead PI:** Shatha Elnakib, Center for Humanitarian Health, Johns Hopkins Bloomberg School of Public Health

---

## Hypothesis and Specific Aims

**Hypothesis.** Routinely generated, de-identified conversational data from an operating digital health service can identify modifiable barriers to health service utilization among refugee and returnee populations, and a navigation intervention designed around one validated barrier can measurably improve navigation feasibility and service uptake.

**Aim 1. Establish and validate a governed conversational-and-utilization evidence pipeline.** We will audit and characterize the de-identified operational corpus (population, languages, volume, linkage to utilization indicators), implement governance and de-identification under JHU IRB, develop a barrier taxonomy using NLP and thematic coding, and evaluate lay-language health terminology in low-resource refugee-community languages where the corpus permits, validated against structured survey and utilization measures with prespecified convergence and divergence analyses. *Outputs: governed analytic dataset; validated coding framework; terminology/accessibility brief where applicable; methods manuscript.*

**Aim 2. Identify and prioritize modifiable barriers to public health service utilization.** Applying the Aim 1 pipeline, we will estimate barrier prevalence and associations with utilization patterns, triangulate conversational signals with structured measures, and select one priority barrier against prespecified criteria (prevalence, modifiability, equity relevance). *Outputs: barrier evidence profile; cycle 1 learning memo; selected design target.*

**Aim 3. Design and feasibility-test one AI-supported navigation intervention targeting the priority barrier.** We will translate Aim 2 findings into design requirements and, through a proposed CBID work package, produce one bounded navigation prototype integrated with the existing platform, then assess feasibility, acceptability, usability, and change in utilization indicators using rapid-cycle implementation evaluation. *Outputs: prototype and design documentation; implementation findings; effect estimates to power follow-on studies.*

---

## 1. Transformative Potential and Impact

**Significance.** Syrian refugee women in Türkiye retain formal access to public health services, including Ministry of Health migrant health centers, yet documented barriers to use persist, including language, navigation complexity, fragmented records, and mobility; clinical findings are not uniform across settings, and persistent maternal and newborn health inequalities remain across the evidence base.[1–6] Displacement compounds these barriers because health systems assume geographically stable users, while refugee and returnee families move across cities, providers, and documentation systems.[7] Prior digital maternal-health interventions in this and comparable populations, including the partner platform's earlier smartphone application for Syrian refugees, support the feasibility and acceptability of reminder and navigation support, though effects are not uniform across studies or components.[8–11] This study addresses a translational gap: humanitarian programs now generate large volumes of routine service conversations, but rigorous methods to link those data to validated barrier taxonomies and utilization outcomes in displacement contexts remain thin.[12,13]

**Innovation.** We will close a 24-month loop from ethically governed operational conversations to a validated barrier taxonomy to one deployed navigation intervention tested for feasibility and utilization change. The high-risk element is responsible use of sensitive, multilingual conversational data in populations for whom errors, privacy failures, and language or cultural bias carry disproportionate consequences.[14–17] Mainstream health-AI work rarely links consumer chatbot intent classification to subsequent care-seeking in humanitarian maternal and reproductive health populations.[12] We will test whether conversational signals add complementary barrier evidence beyond structured measures, whether lay-language terminology in underrepresented refugee-community languages (including dialectal Arabic where present in the corpus) aligns with clinical navigation constructs, and whether one barrier-informed navigation feature is feasible and associated with service use.

**Impact.** CHH will lead research design, ethics, analysis, and evaluation. HERA Digital Health will provide bounded de-identified data access and platform integration within the 10% external-subaward cap. This award funds catalytic science and implementation learning, not large-scale field implementation. Successful completion yields IRB-ready methods, an independent faculty-led research line in AI and humanitarian health evidence at CHH, a funded DrPH dissertation thread, supervised translational design experience for an anticipated CBID student team, peer-reviewable design and methods outputs, and a defensible evidence base for DIV, NIH, and foundation follow-on.

---

## 2. Strategic Alignment

This proposal meets the Life Sciences Research Initiative mandate for bold, high-risk, high-reward science integrating data science and AI with population-health translation. AI is central to analytic methods and the navigation intervention; life-science relevance runs through maternal and reproductive health access among displaced populations; student investment is explicit through DrPH trainee support and a proposed CBID design team. The project advances CHH's capacity to generate rigorous evidence on emerging technology in humanitarian response.

---

## 3. Strength of Approach and Feasibility

### Aim 1. Governed conversational-and-utilization evidence pipeline

**Rationale.** Aim 1 converts the operational corpus from a feasibility unknown into a validated analytic substrate. Without prespecified audit, governance, and validation against structured measures, later barrier prioritization and intervention design lack defensible inputs.

**Design.** Mixed-methods corpus characterization and validation study over Months 1–12, nested within the 24-month award.

**Data and measures.** De-identified conversational health data from HERA humanitarian operations; structured survey and utilization records where linkage is permitted. Prespecified audit documents population, languages, date range, usable volume, completeness, de-identification pathway, utilization linkage, permissions, and fitness for analysis. Geography and any extension beyond the population represented in the corpus follow audit and partner/IRB feasibility review, with prespecified transfer rationale and subgroup validation if required.

| Outcome domain | Candidate measures | Role |
|----------------|-------------------|------|
| Utilization (primary candidates) | Antenatal visit counts; migrant health center registration and visit frequency; referral completion; sustained service engagement | Primary where linkage permits; hierarchy finalized post-audit |
| Conversational analytics | Barrier taxonomy codes; thematic clusters; lay-language terminology fidelity in low-resource languages | Aim 1 validation outputs |
| Implementation (Aim 3) | Feasibility; acceptability (AIM/IAM/FIM-class); usability (SUS); reach; fidelity | Secondary in Aim 3 |

**Analysis.** NLP and thematic coding of health-seeking narratives; pattern detection for entitlement confusion, facility access, and trust barriers; prespecified convergence and divergence analyses comparing conversational and structured signals; lay-language terminology review against clinician-reviewed navigation constructs where Arabic or other low-resource refugee-community languages are present in the corpus. JHU-hosted compute supports secure storage and analysis.

**Pitfalls and alternatives.** Conversational data may add no useful information beyond structured measures or may encode platform-selection and documentation biases; we treat these as testable null hypotheses in Aim 1 rather than assumptions. Privacy or linkage failure triggers a narrowed analytic sample and revised power expectations documented in the audit report.

### Aim 2. Barrier identification and prioritization

**Rationale.** Utilization improvement requires targeting modifiable barriers with equity relevance, not generic access narratives.

**Design.** Cross-sectional and longitudinal association analyses using the Aim 1 dataset, followed by structured barrier prioritization against prespecified criteria (prevalence, modifiability, equity relevance).

**Analysis.** Estimate barrier prevalence and associations with utilization patterns; triangulate conversational and structured evidence; produce cycle 1 learning memo and one CHH-approved design target for Aim 3.

**Pitfalls and alternatives.** If conversational and structured signals diverge materially, we retain both in the evidence profile and select the barrier with strongest convergent support and clearest modifiability for intervention design.

### Aim 3. Navigation intervention design and feasibility testing

**Rationale.** The translational test is whether research-derived barrier evidence can become a usable, safe navigation response on an operating platform within the award period.

**Design.** Rapid-cycle implementation evaluation over Months 13–24: design requirements, bounded prototype, supervised usability and feasibility testing, linkage to utilization indicators where feasible. We do not propose a large RCT; the program does not require one. Analysis uses pre-post comparison with benchmarks or interrupted time series where linkage allows, plus convergent mixed-methods integration of implementation and utilization findings.

**CBID translational work package.** The proposed CBID collaboration applies CBID's established partner-anchored student design model, recently demonstrated in the 2024 Ayu AI collaboration with the NGO telemedicine platform Intelehealth, and follows CBID's published needs-finding methodology for healthcare service innovation in low- and middle-income countries.[18] CHH retains scientific ownership of NLP, statistical analysis, IRB, and humanitarian evaluation; CBID leads one needs-driven design-and-prototype cycle producing a deployable feature on a live platform, publishable as translational design science.

We will complete one 24-month design cycle:

1. Synthesize Aim 2 findings into user, accessibility, and system requirements (multilingual usability, low-bandwidth use, bias-aware UX, and defer-versus-answer boundaries for clinically, culturally, and religiously sensitive questions).
2. Map the patient and navigation journey around the priority barrier.
3. Generate and assess intervention concepts with CHH, HERA, and the DrPH trainee.
4. Prototype one bounded HERA-compatible navigation feature or workflow on the existing WhatsApp-based platform.
5. Conduct supervised usability and feasibility testing under the approved ethics and partner protocol.
6. Deliver design documentation, implementation recommendations, and handoff for follow-on funding.

The specific navigation feature is not predetermined; disciplined needs-driven design selects among plausible forms (e.g., service-matching workflow, referral interface, proactive guidance) after Aim 2. Faculty design-methodology oversight and student participation remain subject to Yazdi's availability and CBID calendar confirmation; Aims 1–2 proceed on CHH capacity if CBID timing requires phasing.

**Ethics.** All conversational data will be handled under JHU IRB with explicit de-identification, no PII or PHI in shared analytic or design artifacts, and protection-aware protocols for vulnerable populations, including prespecified escalation pathways for gender-based violence disclosures and acute medical risk. Safety monitoring during feasibility testing includes structured review of flagged conversations.

**Timeline.**

| Phase | Activity | Output |
|-------|----------|--------|
| Year 1, Q1–Q2 | IRB; de-identification; corpus audit; baseline utilization metrics | Approved protocol; analytic dataset |
| Year 1, Q3–Q4 | Aim 1 validation; Aim 2 barrier prioritization; design brief | Coding framework; cycle 1 learning memo |
| Year 2, Q1–Q2 | Aim 3 concept generation and bounded prototype | Prototype; design documentation |
| Year 2, Q3–Q4 | Supervised usability/feasibility; utilization linkage | Implementation findings; effect estimates for power calculations |

**Feasibility.** JHU hosts analysis, faculty effort, trainee support, and compute. HERA provides data access and technical partnership within the 10% subaward cap. Prior quasi-experimental work on antenatal visit attendance in Istanbul migrant health centers demonstrates adjacent evaluation capacity, though that study used smartphone reminders rather than conversational AI and supports plausibility only.[10]

---

## 4. Team Capability and Environment

**Lead PI.** Shatha Elnakib's scholarship spans the scientific bridge this proposal requires. Her mixed-methods work examines how refugees are integrated into national health systems and why policy commitments do or do not translate into sustained access.[19] Her humanitarian sexual, reproductive, maternal, and newborn health research includes evaluation of service delivery during conflict.[20] She has also contributed to validation of a mobile-health mortality-risk model using national survey data.[21] Together, this record supports the proposed combination of health-systems interpretation, humanitarian reproductive-health relevance, and explicit validation of a new analytic method. Elnakib will be accountable for study design, IRB and ethics, the qualitative codebook and validation framework, mixed-methods integration, selection of the Aim 3 design target, and publication. A CHH-based analyst supported under the award will execute the NLP and statistical pipelines under her scientific oversight.

**Trainee.** Aral Surmeli is a DrPH candidate advised by William (Bill) Weiss and the physician-founder of HERA Digital Health. He is first author of the current JMIR preprint and registered principal investigator for NCT05094518, which evaluated antenatal-care reminders among Syrian refugee women at two Istanbul migrant health centers.[10] The study's planned randomized design could not be analyzed as intended because allocation and identifiers were incompletely captured in routine operations. That experience is directly relevant to this proposal's central feasibility risk: whether conversational and utilization records can be governed, linked, and interpreted without overstating what the data support. Under Elnakib's supervision, Surmeli will lead operational data-provenance mapping, linkage-feasibility documentation, implementation protocol and fidelity assessment, and rapid-cycle learning. His earlier publications on HERA's refugee-health model and end-user acceptability provide additional population and implementation context.[8,9]

**Complementarity and development.** The sequence of ownership is deliberate. Elnakib defines the scientific and ethical standard and determines which finding is sufficiently validated to translate. Surmeli makes the operational data and implementation pathway auditable. Subject to confirmation, Yazdi will provide design-methodology oversight and student supervision while a CBID team converts one approved finding into a testable navigation workflow. HERA supplies bounded data and integration support within the 10% external-partner cap. This structure avoids duplicated ownership while building a faculty-led research line, a DrPH dissertation, and supervised translational design experience for CBID students.

**Environment.** JHU CHH provides humanitarian health evaluation rigor and scientific ownership. The proposed CBID collaboration adds bioengineering design methods. HERA provides the operational platform and de-identified data interface within the 10% cap without new field operations. The roster remains small by design.

---

## 5. Future Funding Potential

This Individual Award is designed as a springboard. Follow-on pathways include DIV Fund stages, NIH and foundation implementation grants, and CHH–HERA co-authored methods and design papers. HERA field implementation at scale would be funded externally after this award establishes the evidence base.

---

## 6. Appropriate Use of Institutional Funds and Budget Justification

**Requested amount:** $300,000 over 2 years (range $200k–$500k allowed; confirm with Shatha/JHURA).

| Line item | Amount (placeholder) | Justification |
|-----------|---------------------|---------------|
| PI effort (Shatha) | $45,000 | 15% effort Years 1–2; study design, oversight, publication |
| CBID faculty and student participation | TBD | Faculty effort, student mechanism, and facilities per Yazdi/Shatha/JHURA scoping |
| Trainee support (Aral) | $30,000 | Dissertation-related research activities |
| Postdoc / research analyst (CHH) | $90,000 | Thematic analysis, implementation learning cycles |
| Compute / AI infrastructure | $50,000 | NLP pipelines, secure storage, JHU-hosted compute |
| Prototyping, usability, travel, dissemination | TBD | Prototype materials, supervised usability, partner coordination |
| HERA partnership (subaward) | $30,000 | 10% cap at $300k: de-identification support, API access, technical deliverables; or in-kind |
| **Working request envelope** | **$300,000** | Rebalance after CBID and JHURA scoping |

No large external subawards; JHU-hosted research, trainee, design, and compute costs dominate; HERA remains at or below 10%.

---

## 7. Demonstrated Need for Support

This project is not yet competitive for traditional external mechanisms at full implementation scale. The Individual Award provides catalytic investment to establish IRB-ready conversational analytics methods in humanitarian settings, generate utilization-focused implementation evidence, and position the faculty team for external follow-on.

---

## References (beyond 4-page limit)

1. Davidson N, Hammarberg K, Romero L, Fisher J. Access to preventive sexual and reproductive health care for women from refugee-like backgrounds: a systematic review. *BMC Public Health*. 2022;22:403. https://doi.org/10.1186/s12889-022-12576-4
2. Ozel S, Yaman S, Kansu-Celik H, Hancerliogullari N, Balci N, Engin-Ustun Y. Obstetric outcomes among Syrian refugees: a comparative study at a tertiary care maternity hospital in Turkey. *Revista Brasileira de Ginecologia e Obstetrícia*. 2018;40(11):673–679. https://doi.org/10.1055/s-0038-1673427
3. Sayili U, Ozgur C, Bulut Gazanfer O, Solmaz A. Comparison of clinical characteristics and pregnancy and neonatal outcomes between Turkish citizens and Syrian refugees with high-risk pregnancies. *Journal of Immigrant and Minority Health*. 2022;24(5):1177–1185. https://doi.org/10.1007/s10903-021-01288-3
4. Hakimi S, et al. Maternal and newborn health inequality among Syrian refugees in Turkey: a systematic review and meta-analysis. *International Journal for Equity in Health*. 2025;24:160. https://doi.org/10.1186/s12939-025-02506-2
5. Republic of Türkiye Ministry of Interior, Presidency of Migration Management. Rights and obligations under temporary protection. Accessed July 10, 2026. https://www.goc.gov.tr/hak-ve-yukumlulukler
6. Republic of Türkiye Ministry of Health, General Directorate of Public Health. Migrant health centers. Accessed July 10, 2026. https://hsgm.saglik.gov.tr/tr/gsm.html
7. Abubakar I, Aldridge RW, Devakumar D, et al. The UCL–Lancet Commission on Migration and Health: the health of a world on the move. *The Lancet*. 2018;392(10164):2606–2654. https://doi.org/10.1016/S0140-6736(18)32114-7
8. Sürmeli A, Narla NP, Shields AJ, Atun R. Leveraging mobile applications in humanitarian crisis to improve health: a case of Syrian women and children refugees in Turkey. *Journal of Global Health Reports*. 2020;4:e2020099. https://doi.org/10.29392/001c.17892
9. Meyer CL, Sürmeli A, Hoeflin Hana C, Narla NP. Perceptions on a mobile health intervention to improve maternal child health for Syrian refugees in Turkey: opportunities and challenges for end-user acceptability. *Frontiers in Public Health*. 2022;10:1025675. https://doi.org/10.3389/fpubh.2022.1025675
10. Sürmeli A, Yasin Y, Narla NP, et al. Digital reminders for antenatal care in a refugee population. *JMIR Preprints*. 2026;97767. Under peer review; NCT05094518. https://preprints.jmir.org/preprint/97767
11. Saleh S, El Arnaout N, Sabra N, et al. The effectiveness of an artificial intelligence-based gamified intervention for improving maternal health outcomes among refugees and underserved women in Lebanon: community interventional trial. *JMIR mHealth and uHealth*. 2025;13:e65599. https://doi.org/10.2196/65599
12. Costa-Gomes B, Tolmachev P, Taysom E, et al. Public use of a generalist LLM chatbot for health queries. *Nature Health*. 2026;1:689–696. https://doi.org/10.1038/s44360-026-00117-x
13. Norton A, Tappis H. Sexual and reproductive health implementation research in humanitarian contexts: a scoping review. *Reproductive Health*. 2024;21:64. https://doi.org/10.1186/s12978-024-01793-2
14. World Health Organization. *The role of artificial intelligence in sexual and reproductive health and rights: technical brief*. Geneva: WHO; 2024. https://iris.who.int/handle/10665/376294
15. Cirillo D, et al. Sex and gender differences and biases in artificial intelligence for biomedicine and healthcare. *npj Digital Medicine*. 2020;3:81. https://doi.org/10.1038/s41746-020-0288-5
16. Zhu L, Mou W, Lai Y, Lin J, Luo P. Language and cultural bias in AI: comparing the performance of large language models developed in different countries on Traditional Chinese Medicine highlights the need for localized models. *Journal of Translational Medicine*. 2024;22:319. https://doi.org/10.1186/s12967-024-05128-4
17. Huo B, Boyle A, Marfo N, et al. Large language models for chatbot health advice studies: a systematic review. *JAMA Network Open*. 2025;8(2):e2457879. https://doi.org/10.1001/jamanetworkopen.2024.57879
18. Shafieian M, Abolfathi N, Yazdi Y. Caredesign: a needs-finding framework for enhancing healthcare service innovation in low- and middle-income countries. *Annals of Biomedical Engineering*. 2026;54(2):613–620. https://doi.org/10.1007/s10439-025-03912-x
19. Elnakib S, Jackson C, Lalani U, Shawar YR, Bennett S. How integration of refugees into national health systems became a global priority: a qualitative policy analysis. *Conflict and Health*. 2024;18(Suppl 1):31. https://doi.org/10.1186/s13031-024-00587-4
20. Tappis H, Elaraby S, Elnakib S, et al. Reproductive, maternal, newborn and child health service delivery during conflict in Yemen: a case study. *Conflict and Health*. 2020;14:30. https://doi.org/10.1186/s13031-020-00269-x
21. Elnakib S, Vecino-Ortiz AI, Gibson DG, et al. A novel score for mHealth apps to predict and prevent mortality: further validation and adaptation to the US population using the National Health and Nutrition Examination Survey data set. *Journal of Medical Internet Research*. 2022;24(6):e36787. https://doi.org/10.2196/36787
