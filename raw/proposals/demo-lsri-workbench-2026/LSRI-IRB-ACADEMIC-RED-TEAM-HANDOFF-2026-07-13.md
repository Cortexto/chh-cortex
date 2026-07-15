---
name: LSRI current-narrative IRB and academic red-team handoff
description: Sentence-level skeptical review of the 2026-07-13 LSRI narrative for Claude and Shatha.
type: handoff
status: blocker-review
date: 2026-07-13
reviewer: Codex
target: submission/lsri-narrative-word-paste-2026-07-10.md
scope: current-version-only
---

# LSRI current narrative: IRB-defense and academic-jury review

## Scope lock

This review treats `submission/lsri-narrative-word-paste-2026-07-10.md` as the only scientific object. It does not ask Claude to preserve the prior drafting path.

Berktuğ clarified on 2026-07-13 that **Youseph Yazdi will not participate in the study**. Remove Yazdi, CBID, the proposed CBID student team, the CBID work package, CBID costs, and CBID-dependent claims throughout. Do not treat this as a role still awaiting confirmation.

## Jury verdict

**BLOCK before PI or IRB defense.** The premise is scientifically interesting, but the current narrative makes stronger claims than its data architecture can support. The largest problem is not tone. It is construct validity.

The text currently blends three different data objects into one proposed measurement instrument:

1. **Structured follow-up responses** can be candidate self-reported utilization measures.
2. **User-initiated free-text conversations** can describe perceived barriers, questions, and navigation needs.
3. **No response after a referral or reminder** is missing data. It is not evidence that care was missed.

The proposal becomes defensible only when those objects are separated in the hypothesis, aims, endpoints, missing-data plan, and ethics protocol.

### What is worth preserving

- The operating service creates a rare opportunity to study a time-varying, pre-facility part of care-seeking.
- The proposal correctly back-stages the platform and puts JHU faculty science first.
- The prior Istanbul implementation failure is a credible reason to invest in prospective data definitions and linkage discipline.
- Explicit examination of who the digital data omit could be a real methods contribution if a comparison frame and estimand are specified.
- A null result can be valuable, but only within a prespecified population, instrument, and comparator.

### The committee-repeatable scientific object

Use this as the governing interpretation, not necessarily as final prose:

> The study will test whether prospectively specified follow-up questions embedded in an operating WhatsApp service can measure selected self-reported utilization events among participating refugee women, and whether separately coded conversational content adds reproducible information about perceived navigation barriers. Nonresponse and population selection will be analyzed as sources of uncertainty, not interpreted as missed care.

This is narrower than “conversational data measure the pre-clinic journey,” but it is understandable, falsifiable, and closer to what the platform can physically observe.

## Blockers that must change the study description

### B1. The opening creates a false two-source world

Lines 9 and 23 say health systems know care-seeking only when women reach facilities and that everything before arrival is invisible to facility records and surveys. That is too absolute. Referral systems, longitudinal cohorts, claims, community follow-up, appointment systems, qualitative work, and repeated surveys can observe parts of the pathway.

**Repair:** claim an incremental and bounded gap. Facility data are strongest on realized encounters; many routine data systems do not capture time-varying questions and perceived barriers between intention and attendance. Do not say “only,” “everything,” or “invisible.” Berktuğ's note later on we gotta find academic papers that backs this. So idk we can ask cursor to do the review or sth if you clearly indicate what needs to be done and how. 

### B2. Novelty is asserted without a novelty review

Line 9 states, “No study has yet...” and line 29 says three things are new. One Nature Health paper and one humanitarian implementation-research review cannot establish field-wide novelty.

**Repair:** either complete a documented scoping search or use a source-safe formulation such as “Few studies have evaluated...” with exact inclusion boundaries. A novelty claim should name databases, search dates, core terms, population, data modality, and what prior work did not do.

### B3. “Validly measure utilization” has no reference standard

Aim 1 promises to test whether in-service self-report “actually measures utilization,” while line 43 says primary outcomes occur entirely within the operating service and do not depend on external facility records. The draft does not name a gold standard, independent comparator, or validation construct.

**Repair:** choose one of two honest routes.

- **Criterion-validation route:** obtain independent attendance verification for a consented subset, such as facility records or another credible event-level source. Define match windows, linkage method, sensitivity, specificity, predictive values, agreement, and handling of unmatched records.
- **No-record route:** stop calling this criterion validation of actual utilization. Evaluate response process, content validity, test-retest reliability where appropriate, convergent/known-groups validity, completion, and measurement error. The outcome remains **self-reported utilization**.

### B4. Nonresponse is not nonattendance

Lines 15 and 51 define referral information followed by no attendance confirmation as a candidate signal of unrealized care-seeking. That is the most dangerous inferential step in the proposal. A woman may have attended, ignored the message, changed phones, lost connectivity, left Türkiye, misunderstood the prompt, or stopped using the service.

**Repair:** use a three-state outcome at minimum: confirmed attendance, confirmed nonattendance, and unknown/no response. Model response propensity. Predefine sensitivity bounds or multiple assumptions for missing-not-at-random data. Never collapse silence into missed care.

### B5. The “selection function” is not identifiable as written

The proposal promises to establish whom platform data can and cannot represent using “available population benchmarks,” but names no target population, geography, sampling frame, benchmark dataset, overlap variables, or transportability estimand.

**Repair:** define:

- target population and time window;
- service-user analytic population;
- benchmark source with matching geography and dates;
- variables available in both sources;
- estimand, for example utilization-reporting behavior among service users rather than all refugee women;
- weighting or standardization method;
- residual differences that cannot be corrected.

If no suitable benchmark exists, promise a descriptive sample profile and transportability limits, not a formal selection function or representativeness analysis.

### B6. Retrospective service analysis and prospective research are blurred

The narrative moves from existing routine data to prospectively changing question wording, timing, and flows, then to usability testing and an intervention. Those are different activities with different consent, recruitment, risk, and IRB implications.

**Repair:** split the protocol into clearly labeled components:

1. retrospective secondary analysis of existing data;
2. prospective instrument-development study;
3. optional prospective navigation feasibility pilot.

State participant populations, consent or waiver route, recruitment, contact, compensation, inclusion/exclusion, and data flow separately for each component.

### B7. Aim 3 has lost its owner and remains causally overstated

With Youseph and CBID out, Aim 3 no longer has an implementation owner. Even before that correction, a pre-post comparison of a single feature could not support “improvement” without a comparator and adequate control of secular change, regression to the mean, and exposure.

**Recommended repair:** make this a two-aim methods proposal unless Shatha can name a real JHU implementation lead, HERA can deliver the bounded technical work within the external cap, and a lawful participant-testing route exists. A two-aim proposal can still be high-risk/high-reward if the scientific contribution is a valid, governed measurement method.

**If Aim 3 remains:** call it exploratory feasibility testing. Do not hypothesize improved utilization. Name the implementation owner, recruitment route, unit of analysis, minimum sample, exposure definition, comparator, decision thresholds, and remote or partner-supported user-testing protocol.

### B8. “No field program” contradicts the proposed work

Line 74 says Aims 1–3 require no new facility infrastructure or field program. A validation sub-study, prospective question refinement, usability testing, and intervention evaluation all involve new research activity and potentially new participant contact. HERA also has no field team.

**Repair:** say HERA will not run field activities. Then name who will recruit, consent, verify outcomes, conduct usability work, and handle referrals. If all participant work is remote and opt-in through the service, say so and defend its equity and safety limits.

### B9. “Reusable dataset hosted at JHU” is not ethically earned

Free-text health conversations can retain indirect identifiers after direct identifiers are removed. The dataset also includes sensitive health, reproductive, family, ethnicity/nationality, religion, location, and safety information. Reuse, hosting in the United States, and sharing require a lawful data-transfer route, consent/waiver analysis, data-use agreement, retention plan, access model, and re-identification assessment.

**Repair:** promise a governed **analysis dataset in a controlled JHU environment**, subject to IRB and applicable data-transfer approvals. Do not promise reuse or wider sharing until an honest-broker de-identification determination and consent/governance conditions permit it.

### B10. Ethics is one sentence where the proposal needs an architecture

Line 63 lists IRB, de-identification, GBV escalation, acute-risk escalation, and review of flagged conversations without explaining whether review is retrospective or real time. This can create a duty-to-intervene promise that the team may not be able to meet.

**Repair:** the ethics paragraph must identify:

- data controller(s), processor(s), and data owner;
- retrospective versus prospective activities;
- consent, waiver, or determination route for each activity;
- Türkiye-to-U.S. transfer mechanism and data-use agreement;
- exact de-identification or pseudonymization pipeline and who holds linkage keys;
- whether any researcher sees raw text;
- secure environment, roles, access logging, retention, destruction, and breach response;
- whether children’s health data enter via caregiver vaccination reports;
- languages and literacy accommodations for consent;
- service/research separation and refusal without service penalty;
- real-time versus retrospective safety review;
- survivor-centered GBV response, confidentiality and reporting limits, and locally available referral pathways;
- conflict-of-interest management for a trainee who founded the platform and may help define, extract, and analyze its data.

## Sentence-level claim defense matrix

Verdicts: **KEEP** = defensible as written or with routine verification; **NARROW** = scientifically plausible but overstated; **SOURCE** = requires an exact-fit source or documented data audit; **BLOCK** = changes inference or ethics; **REMOVE** = obsolete under the current team decision.

| ID | Line(s) | Claim fragment | Verdict | Jury objection / required repair |
|---|---:|---|---|---|
| C01 | 1 | “Conversational Data as a Scientific Instrument” | NARROW | The candidate utilization instrument is the structured follow-up layer, not all conversation data. Retitle after the data objects are separated. |
| C02 | 3 | Shatha as lead PI | KEEP | Verify current full-time faculty eligibility and exact appointment title in the submission system. |
| C03 | 5 | Shatha decision marker | BLOCK | Remove all bracketed markers before PI circulation or PDF export. |
| C04 | 9 | Health systems measure only at clinic arrival | BLOCK | False absolute; narrow to limits of routine facility data. |
| C05 | 9 | Everything before arrival is invisible to records/surveys | BLOCK | False dichotomy; longitudinal and referral data can observe parts of the journey. |
| C06 | 9 | Pre-clinic journey is where care is “most often” lost | SOURCE | Requires a population- and setting-specific care-cascade source. |
| C07 | 9 | Service records questions, referrals, barriers, and attendance | SOURCE | Founder confirmation covers three follow-up loops, not the full wording, storage, response structure, referral field, or data completeness. Audit first. |
| C08 | 9 | No study has used this record as an instrument | BLOCK | Requires systematic novelty search; remove absolute now. |
| C09 | 11 | Conversation data validly measure the full journey | BLOCK | Conflates free text, structured self-report, referral events, and missingness. Define separate constructs and validation tests. |
| C10 | 11 | Intervention associated with improved indicators | BLOCK | Aim 3 design is not specified to support this hypothesis; Youseph/CBID route is removed. |
| C11 | 13 | Three structured follow-up cycles exist | SOURCE | Plausible and founder-confirmed, but exact questions, denominators, dates, storage, and export path remain unverified. |
| C12 | 13 | JHU IRB will establish governance/de-identification | NARROW | IRB reviews a specified plan; it does not itself create the legal basis, transfer mechanism, or de-identification pipeline. |
| C13 | 13 | Configurable flows will be prospectively refined | BLOCK | This is prospective human-subjects research, not simply secondary analysis. Define consent and recruitment. |
| C14 | 13 | Nested sub-study tests actual utilization | BLOCK | Name the reference standard; otherwise retain “self-reported utilization.” |
| C15 | 13 | Dialectal Arabic aligns with clinical constructs | NARROW | Define construct, sampling, translation/adjudication, annotators, and agreement metric. Arabic only “where corpus permits” is too vague. |
| C16 | 13 | Governed dataset and validated layer as outputs | NARROW | Make outputs conditional on data audit, lawful access, and prespecified validation thresholds. |
| C17 | 15 | Identify and rank modifiable barriers | NARROW | Observational text can identify reported barriers; “modifiable” needs a rule or evidence beyond prevalence. |
| C18 | 15 | No confirmation signals unrealized care-seeking | BLOCK | No response is missing, not nonattendance. Use three-state outcomes and sensitivity analysis. |
| C19 | 15 | Model representation relative to broader refugees | BLOCK | Target population and benchmark are unnamed; formal representativeness may be impossible. |
| C20 | 15 | Select barrier by prevalence/modifiability/equity | NARROW | Operationalize each criterion, weighting, decision authority, and how uncertain estimates affect selection. |
| C21 | 17 | CBID student team delivers Aim 3 | REMOVE | Youseph and CBID are not participating. Remove every dependent claim. |
| C22 | 17 | Fallback barrier makes Aim 3 independent | NARROW | A literature-derived barrier may not be locally relevant. If retained, define transferability criteria and why bypassing Aim 2 remains scientifically coherent. |
| C23 | 17 | Effect estimates will power follow-on | SOURCE | Requires sample size, event rate, exposure, attrition, variance, and estimand. |
| C24 | 23 | Knowledge comes almost entirely from facilities/surveys | BLOCK | Source-safe problem is incomplete routine measurement, not only two data sources. |
| C25 | 23 | Neither source sees desired but unrealized care | NARROW | Some designs can; say routine facility records do not consistently capture it. |
| C26 | 23 | Strongest evidence is Syrian refugees in Türkiye | SOURCE | “Strongest” is a comparative review claim not established by citations 1–6. |
| C27 | 23 | Formal access to migrant health centers | NARROW | Eligibility is conditional and the 2026 financing/access regime changed. State the exact population and current rules; avoid blanket access language. |
| C28 | 23 | Listed barriers interrupt continuity | NARROW | Map each barrier to exact citations; “fragmented records,” “cost,” “mistrust,” and “mobility” may not all be supported by refs 1–3. |
| C29 | 23 | Conflicting studies + 2025 meta-analysis | KEEP | Useful nuance. Ensure outcomes/populations are not presented as directly comparable and retain the noncausal register. |
| C30 | 23 | Access pathways, not refugee status, are the problem | BLOCK | This causal conclusion does not follow from heterogeneous observational evidence. Say pathways are plausible and modifiable study targets. |
| C31 | 23 | Pathways are unmeasured where they fail | NARROW | Say incompletely measured in routine systems. |
| C32 | 25 | Conversational data can plausibly add information | KEEP | Keep as a testable rationale, not proof. |
| C33 | 25 | Nature study: 617,827, nonhumanitarian, no outcomes | KEEP | Accurate. It supports a methods precedent and explicitly notes no downstream outcomes. It does not prove refugee novelty. |
| C34 | 25 | Humanitarian research is almost all structured surveys | BLOCK | Citation 14 does not support this. It reviewed implementation-framework use and found diverse qualitative, quantitative, and mixed methods. Delete or replace. |
| C35 | 25 | Six of 69 used an implementation framework | KEEP | Accurate, but it supports a framework-use gap, not a conversational-data or survey-only gap. |
| C36 | 25 | HERA preprint: 2.5 vs 1.9; identifiers limited causality | KEEP | Accurate if labeled as an unreviewed app-era quasi-experimental preprint, not evidence for the current WhatsApp flows. |
| C37 | 25 | Lebanon study cannot isolate component | NARROW | Reasonable inference from a multicomponent intervention with historical controls; state this as a design limitation, not the paper’s definitive conclusion. |
| C38 | 29 | Humanitarian service becomes a scientific instrument | KEEP | Strong conceptual frame after defining which structured variables are the instrument and which text is contextual data. |
| C39 | 29 | Three things are new | BLOCK | Novelty search required. |
| C40 | 29 | Embedded attendance confirmations are outcomes | NARROW | They are candidate self-reported outcomes; exact wording and truth conditions are unverified. |
| C41 | 29 | Drop-off cannot exist in facility registers | BLOCK | Nonresponse is not a care event; referrals and missed appointments can exist in other systems. |
| C42 | 29 | Digital data over-represent phone users | SOURCE | Plausible, but specify platform entry requirements, phone sharing, literacy, language, connectivity, and actual service-user profile. |
| C43 | 29 | Aim 2 establishes whom data can speak for | BLOCK | Overpromises identification without a sampling frame and shared benchmark covariates. |
| C44 | 29 | Null result defines the method’s limits | NARROW | It defines limits only for the prespecified service, population, period, and measurement design. |
| C45 | 29 | Governance/subgroup/terminology built in | NARROW | Intent is not a protocol. Name controls, comparisons, thresholds, and accountable roles. |
| C46 | 31 | Reusable dataset hosted at JHU | BLOCK | Reuse and U.S. hosting need IRB, consent/waiver, data-transfer, de-identification, and controlled-access decisions. |
| C47 | 31 | Validated method + ranked barriers + tested feature | NARROW | Each output is conditional; the feature currently lacks an owner and evaluation route. |
| C48 | 35 | NLP, instrument design, representativeness are core | NARROW | Name models, tasks, annotation design, per-language evaluation, benchmark, analyst, and compute environment. |
| C49 | 35 | DrPH + CBID student benefit | REMOVE | Retain the DrPH contribution if appropriate; delete CBID/student-team language. |
| C50 | 35 | CHH retains scientific leadership | KEEP | Add named expertise for statistics/NLP/data governance if Shatha will not directly execute these components. |
| C51 | 41 | Mixed-methods characterization/validation in months 1–12 | NARROW | No sample size, recruitment, decision threshold, or IRB/data-transfer lead time supports the schedule yet. |
| C52 | 43 | Primary data arrive de-identified | BLOCK | Export and de-identification path are unverified. State who transforms raw data and whether JHU ever receives linkable text. |
| C53 | 43 | Outcome measurement needs no facility data | BLOCK | In tension with “validation.” Defend a non-criterion validation route or secure an independent reference standard. |
| C54 | 43 | Exploratory facility linkage | BLOCK | Decision marker remains and partners are hypothetical. Cut unless Shatha names a feasible route. |
| C55 | 43 | Prespecified audit documents fitness | KEEP | This is essential, but it should be a go/no-go gate before the proposal promises validation and modeling. |
| C56 | 45 | Utilization measures include engagement/referral | BLOCK | Sustained engagement is platform use, not health-service utilization. Referral follow-through needs a defined observable event. |
| C57 | 45 | Primary hierarchy finalized after audit/sub-study | NARROW | Avoid outcome selection after seeing results. Prespecify a staged rule and lock analysis before outcome testing. |
| C58 | 45 | Annotation subset supports precision/recall/F1 | NARROW | Define classifier task, label taxonomy, annotators, adjudication, train/validation/test split, per-language sample, and unit of analysis. |
| C59 | 47 | Low response merely narrows precision | BLOCK | Low or differential response can invalidate the estimand, not only widen confidence intervals. Add feasibility thresholds and selection-bias analysis. |
| C60 | 47 | Null incremental-value result | NARROW | Name the structured comparator and performance criterion that define “incremental value.” |
| C61 | 47 | Small language sample shifts to descriptive report | KEEP | Add a minimum sample threshold and explain whether affected subgroup claims are dropped. |
| C62 | 51 | Cross-sectional/longitudinal models, adjusted covariates | NARROW | Generic. Specify primary estimand, model family, time origin, clustering/repeated measures, covariates, confounding logic, and missing-data plan. |
| C63 | 51 | Formal selection function using benchmarks | BLOCK | See B5. Do not promise formal correction without identifiability. |
| C64 | 51 | Triangulation selects a barrier | NARROW | Define how conflicting qualitative, text-classification, and structured-response signals are reconciled. |
| C65 | 53 | Divergent signals assessed for subgroup effects | KEEP | Add a prespecified decision tree and protect against underpowered subgroup fishing. |
| C66 | 53 | Published fallback protects timeline | NARROW | It protects schedule but can break internal scientific logic; justify contextual fit or drop Aim 3. |
| C67 | 57 | Aim 3 requirements/prototype/testing | REMOVE | Current owner was CBID. Rebuild only if a real owner and lawful testing route exist. |
| C68 | 57 | Possible feature forms | NARROW | Too broad for a two-year 4-page plan; choose only after the barrier and delivery owner are real. |
| C69 | 59 | FIM/AIM/IAM/SUS outcomes | NARROW | Name respondent group, language versions, cultural adaptation, administration timing, and why each measure fits users versus implementers. |
| C70 | 59 | Pre-post/ITS utilization change | BLOCK | No sample, comparator, time points, exposure definition, or minimum series length. Retain only as exploratory if fully specified. |
| C71 | 59 | No causal claims | KEEP | Preserve; align the central hypothesis and all impact language with it. |
| C72 | 61 | Entire CBID work package | REMOVE | Remove due to current team decision. Reference 17 becomes unnecessary unless used only as background. |
| C73 | 61 | CHH owns NLP/statistics | SOURCE | Name the analyst/methodologist and available effort. Faculty oversight alone does not demonstrate execution capacity. |
| C74 | 63 | Single-sentence ethics plan | BLOCK | Replace with the ethics/data architecture in B10. |
| C75 | 67–70 | Timeline | NARROW | Add protocol/data-use/transfer gates and go/no-go milestones. Current Year 1 assumes an unproven dataset and validation route. |
| C76 | 74 | JHU secure storage/compute | SOURCE | Identify the approved environment and access model; do not let “secure” remain an adjective. |
| C77 | 74 | Partner provides de-identified access | BLOCK | Data rights, export method, de-identification, and transfer mechanism are unverified. |
| C78 | 74 | No new field program needed | BLOCK | Contradicted by validation, prospective flows, usability work, and intervention testing. |
| C79 | 74 | Prespecification prevents identifier failure | NARROW | It reduces risk but does not guarantee linkage, consent, data completeness, or implementation fidelity. |
| C80 | 78 | Shatha capability/ownership | KEEP | Evidence supports humanitarian health research; add the named quantitative/NLP execution role. |
| C81 | 79 | Aral’s experience and responsibilities | NARROW | Scientifically relevant, but disclose founder/data-owner/trainee conflicts and ensure independent analysis and supervision. |
| C82 | 80–81 | Yazdi and CBID team | REMOVE | Remove completely. |
| C83 | 82 | HERA provides de-identified data/integration | NARROW | The 10% cap is correct; data provision remains conditional on rights, lawful transfer, and verified extraction. |
| C84 | 84 | Ownership does not overlap; roster small | NARROW | Rewrite after removing CBID and adding the actual analyst, data steward, and Aim 3 owner or deleting Aim 3. |
| C85 | 88 | Award produces “exactly” all follow-on assets | NARROW | Outputs are conditional on feasibility gates and cannot be guaranteed. |
| C86 | 88 | NIH, foundation, DIV pathways | NARROW | Name plausible mechanism classes or specific calls only when eligibility and scientific fit are checked. |
| C87 | 92 | Funds prioritize listed JHU work | KEEP | Align with a real budget and named personnel. |
| C88 | 92 | CBID costs | REMOVE | Remove. |
| C89 | 92 | External cap and JHURA rates | KEEP | Correct posture; final figures require JHURA. |
| C90 | 96 | Not competitive externally | NARROW | Avoid an unsupported universal claim. Say which scientific assets are currently missing for the intended next mechanism. |
| C91 | 96 | Converts asset into governed research resource | KEEP | Keep as an objective, conditional on participant rights, lawful transfer, and a defensible measurement design. |

## Source-fit audit

### Reference 9: Nature Health 2026

**Accurate use:** 617,827 conversations, intent classification, general consumer context, and no downstream care-seeking outcomes.

**Important comparator omitted by the draft:** the Nature study used automated PII scrubbing, privacy-preserving summaries, an “eyes-off” model in which researchers did not access raw conversations, Microsoft-controlled processing, and aggregate reporting. The LSRI draft proposes clinician review of conversational text and a reusable JHU dataset, so its privacy exposure is materially higher and needs a stronger architecture.

### Reference 14: Norton and Tappis 2024

**Accurate use:** six of 69 included humanitarian SRH intervention studies explicitly used an implementation-research framework.

**Incorrect use:** this paper does not show that humanitarian research relies almost exclusively on structured surveys. It reports diverse quantitative, qualitative, and mixed-methods designs. Delete the survey-only sentence.

### Reference 7: HERA/JMIR preprint

**Accurate use:** planned RCT became quasi-experimental because allocation/identifier capture was incomplete; confirmed exposure group had 2.5 versus 1.9 mean visits; findings are associative and the preprint is unreviewed.

**Boundary:** it studied a smartphone app with push reminders at two Istanbul migrant health centers. It does not validate the current WhatsApp conversation corpus, the current three follow-up loops, or WhatsApp effectiveness.

### Reference 8: Lebanon intervention

The intervention combined messages, reminders, an app, provider training/gamification, and historical controls. Component attribution is therefore limited, but phrase this as a design-based inference. Do not imply the authors ran a component analysis and found none.

### References 10–13: AI and bias

These support general privacy, safety, sex/gender bias, cultural/language bias, and chatbot-quality concerns. They do not replace a study-specific plan for Turkish law, cross-border transfer, informed consent, raw-text handling, refugee/community risk, or multilingual validation.

### References 15–16: Türkiye access

Official access pages are useful but do not support a blanket statement that all Syrian refugee women currently have uncomplicated formal access. State status, registration/geographic conditions, and the current 2026 cost/coverage rules precisely.

### Reference 17

Remove if CBID is removed. A needs-finding framework from a teaching hospital in Iran does not independently justify this study’s intervention ownership.

## IRB-defense questions the PI must be able to answer

1. Which activities are retrospective secondary analysis, and which are prospective human-subjects research?
2. What exactly did users consent to when their messages and health reports were collected for service delivery?
3. Does the service consent permit research use, JHU access, U.S. storage, future reuse, and human annotation?
4. If consent is waived for existing data, what makes the research minimal risk and impracticable without a waiver?
5. Who is the data controller, who is the processor, who owns the data, and who signs the data-use agreement?
6. What lawful mechanism permits transfer of sensitive health and sexual/reproductive data from Türkiye to the United States?
7. Does JHU receive raw text, pseudonymized text, scrubbed text, summaries, or only derived variables?
8. Who holds the linkage key, and can any investigator readily re-identify a user?
9. How are indirect identifiers in free text, rare dialects, dates, locations, family events, and GBV disclosures removed or controlled?
10. Are children’s health data present through caregiver vaccination reporting, and how does that alter review and consent?
11. What independent source, if any, validates self-reported attendance?
12. What is the primary estimand, and what is the unit of observation: message, reminder event, woman, pregnancy, child, or person-period?
13. How will shared phones, changing numbers, literacy, language, connectivity, and platform attrition affect measurement?
14. How will “no response” be separated from “did not attend”?
15. What benchmark makes the representativeness analysis identifiable?
16. Who can see raw safety disclosures, and are they reviewing in real time or retrospectively?
17. If real-time risk is detected, who is on duty, in which language, in which country, with which referral directory and response window?
18. How are GBV disclosures handled without exposing participants to retaliation or unsafe mandatory-reporting consequences?
19. How can a woman refuse research contact or withdraw without losing access to the service?
20. How are Aral’s trainee role, platform-founder role, data access, financial/organizational interest, and analytic role separated and disclosed?
21. Who supplies statistical, NLP, qualitative, data-governance, and implementation-science expertise after CBID/Yazdi are removed?
22. What sample and response-rate thresholds make each aim feasible, and which aim stops if thresholds are missed?

## Recommended rebuild for Claude

Do not patch individual sentences. Rebuild from the data ontology and current team.

### Step 1. Remove obsolete collaboration content

Delete all Youseph, CBID, student-team, Caredesign, CBID-cost, and CBID-dependent prototype language from the title page, Aims, Strategic Alignment, Approach, Timeline, Team, budget narrative, and references.

### Step 2. Lock the four data objects

| Data object | Defensible use | Forbidden inference |
|---|---|---|
| Structured follow-up response | Candidate self-reported utilization event | Proof of actual attendance without independent verification |
| Free-text conversation | Perceived barrier, question, navigation need, terminology | Clinical diagnosis, objective barrier prevalence in all refugees, or utilization outcome |
| Referral/reminder event | Exposure/opportunity to respond | Proof the person acted on the referral |
| No response | Missingness/attrition outcome | Missed care or failed referral |

### Step 3. Use a two-aim default

**Aim 1:** Develop and evaluate the measurement properties of prospectively specified in-service self-report items. Separate retrospective audit from prospective instrument development. Name the reference standard or narrow “validation” to the properties actually assessable.

**Aim 2:** Characterize perceived barriers among participating users and quantify response/selection uncertainty. Model nonresponse explicitly. Estimate transportability only if a suitable benchmark exists.

**Exploratory translation:** one measurement-informed navigation workflow only if a real owner, recruitment route, safety protocol, and budget are confirmed. It should not be the central hypothesis or promise improved utilization.

### Step 4. Add hard go/no-go gates

- **Data gate:** exact loops, question wording, dates, denominators, response completeness, storage, export, and language distribution verified.
- **Rights gate:** service consent, IRB route, data-use agreement, Türkiye-to-U.S. transfer, data-controller roles, and de-identification architecture approved.
- **Measurement gate:** target constructs, primary endpoint, reference/comparator, unit of analysis, and success thresholds prespecified.
- **Selection gate:** target population and benchmark source confirmed; otherwise downgrade to descriptive transportability limits.
- **Translation gate:** named owner and participant-testing route; otherwise no Aim 3.

### Step 5. Replace the ethics sentence with a compact data-flow paragraph

The final four-page narrative does not need a legal memo, but it must show the chain:

`service collection → source-system minimization → honest-broker de-identification/pseudonymization → lawful transfer/controlled JHU environment → role-limited analysis → aggregate reporting → retention/destruction`

State where consent or waiver applies and whether raw conversational text ever leaves the source environment.

### Step 6. Re-run the committee tests

Before returning the next draft, Claude should be able to answer:

- What is the single primary outcome?
- What observation would falsify the central hypothesis?
- What validates the self-report?
- What does no response mean?
- Who is represented?
- Who is missing?
- Who owns each aim now that CBID is gone?
- What does the study stop doing if data, consent, transfer, or response thresholds fail?

## Mechanical findings on the current file

- Two unresolved `[SHATHA DECISION]` markers remain.
- Twenty-two Unicode em dashes remain in the external narrative.
- Yazdi/CBID/student-team content remains in Aim 3, Strategic Alignment, Approach, Team, and budget language.
- Body text before references is approximately 2,272 whitespace-delimited words. Four-page compliance at 12-point font and ½-inch margins remains unverified and needs an actual PDF render.
- The current file labels itself a final handoff but contains unresolved study-design decisions and unverified data-access claims.

## External standards and primary sources checked

- [JHU IRB forms and research-plan routes](https://publichealth.jhu.edu/offices-and-services/institutional-review-board-irb/forms): separates existing-data analysis from new data collection and includes international-transfer consent language.
- [JHU student research guidance](https://publichealth.jhu.edu/offices-and-services/institutional-review-board-irb/student-research): new collection generally requires recruitment, consent, and instrument materials; de-identified secondary analysis receives a formal determination.
- [JHU individual-level data-sharing expectations](https://publichealth.jhu.edu/sites/default/files/2023-02/bsphirbsdatasharingguidancejan122023.pdf): sharing depends on consent, local approvals, re-identification risk, and controlled access; waiver datasets require strong de-identification controls.
- [HHS/OHRP coded private-information guidance](https://www.hhs.gov/ohrp/coded-private-information-or-biospecimens-used-research.html): coded data can remain identifiable; investigators should not independently declare that secondary use is not human-subjects research.
- [Türkiye KVKK special-category data rules](https://www.kvkk.gov.tr/Icerik/6609/Conditions-for-Processing-Of-Special-Categories-of-Personal-Data): health and sexual-life data receive heightened protection.
- [Türkiye KVKK cross-border transfer rules](https://www.kvkk.gov.tr/Icerik/6649/Personal-Data-Protection-Law): transfer needs a lawful condition and an adequacy/safeguard route, including standard-contract mechanisms where applicable.
- [Nature Health 2026 conversational-data precedent](https://www.nature.com/articles/s44360-026-00117-x): supports the general method precedent and also demonstrates a much stricter eyes-off privacy architecture than the current draft describes.
- [Norton and Tappis 2024 scoping review](https://reproductive-health-journal.biomedcentral.com/articles/10.1186/s12978-024-01793-2): supports the six-of-69 framework claim but not the survey-only claim.
- [HERA JMIR preprint](https://preprints.jmir.org/preprint/97767): supports the 2.5-versus-1.9 association and the identifier-failure lesson, not current WhatsApp-loop validity.
- [WHO ethics and governance of AI for health](https://www.who.int/publications/i/item/9789240029200): supports autonomy, consent, privacy, accountability, equity, and study-specific governance.
- [AIM/IAM/FIM development paper](https://pubmed.ncbi.nlm.nih.gov/28851459/): supports the implementation outcome measures but does not decide respondent group, language adaptation, or cultural validity for this study.

## Final instruction to Claude

Return the next narrative only after rebuilding the hypothesis and aims around the separated data objects. Do not preserve a sentence merely because it is cited. A reference can support a neighboring fact while failing to support the inference made in the sentence.

Red-team pass applied: current-version-only claim audit; measurement, missingness, selection, ethics, and team blockers isolated for rebuild.
