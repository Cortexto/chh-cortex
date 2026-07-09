---
name: grant-writer
description: Use for CHH grant writing, proposal drafting, grant fit assessment, concept notes, application answers, budget narratives, donor-specific revisions, or uploaded proposal review. Triggers include "write this grant", "start a proposal", "grant fit", "application answer", "revise this proposal", "donor narrative", and "concept note". Before final external-facing grant output, run the grant-red-team-reviewer gate.
---

# HERA Grant Writer

Use this skill for grant strategy, fit assessment, outlining, drafting, editing, and review.

## Activation Test

If this skill is loaded correctly, the response should begin grant work by identifying:

- donor / program;
- project or proposal target;
- deadline and section constraints, if known;
- recommended voice register;
- **tone capsule loaded** (path + section from `wiki/concepts/workflow/grant-tone-capsule-registry.md`, or `none`);
- **canonical blocks loaded** (for concept notes / 2-pagers without a donor template: `wiki/principles/source-banks/hera-canonical-blocks.md`, or `none`);
- **revision log** (package `REVISION-LOG.md` principles if workbench active, or `none`);
- files/patterns it will use.

Do not start with a generic draft.

## Required Reads

Read only what is relevant:

1. `CORTEX.md`
2. **`wiki/entities/hera-current-state.md`** — team capacity, partner model, Turkey exit direction, Syria funding narrative shift, budget calibration, product naming, Humanitech status. Read before any proposal draft.
3. `wiki/concepts/workflow/cortex-grant-writing-process.md`
3b. **`wiki/concepts/workflow/cortex-donor-obsession-gate.md`** + package `DONOR-DOSSIER.md` when status must be `ready` before external draft (override: human says `skip donor gate`)
3c. **`.cursor/rules/cortex-grant-institutional-open-register.mdc`** — institutional open (org + PoC first; no vignette) before first external paragraph ships
3. `wiki/principles/voice-dna.md`
4. `wiki/principles/source-banks/aral-voice.md` or `wiki/principles/source-banks/berktug-voice.md` depending on register
5. Relevant donor files in `wiki/donors/`
6. Relevant project files in `wiki/projects/`
7. Relevant evidence files in `wiki/evidence/`
8. `wiki/principles/patterns/ACTIVATION-INDEX.md` to identify which pattern cards should fire for the current form, donor, or section
9. Relevant pattern files in `wiki/principles/patterns/`
10. `wiki/principles/patterns/donor/039-reviewer-legibility-for-credentials.md` whenever using awards, funders, accelerators, university programs, partners, acronyms, platforms, or technical initiatives as credibility signals
11. `TASKS.md` only when checking active deadline/pipeline context
12. `wiki/concepts/workflow/cortex-partner-co-applicant-grant-pipeline.md` when the work is a **joint proposal**, **co-applicant**, **subgrantee**, or **named university partner** on the same submission — default **Phase 0 funding facts** and **G2 / G3 gates** before treating section prose as the main deliverable (see `_system/agents/grant-pipeline-orchestrator.md`).
13. **`wiki/concepts/workflow/grant-tone-capsule-registry.md`** — resolve trigger context, read the listed capsule section(s) **before** the first draft sentence (canonical capsule index; do not duplicate paths here).
14. **Active proposal workbench** — when working a package under `raw/proposals/` with workbench files: read `wiki/concepts/workflow/grant-proposal-workbench.md`, then package `DECISION-CHART.md`, `BRAINSTORM-LEDGER.md`, **`REVISION-LOG.md`**, `AGENT-HANDOFF.md`; emit boot summary before donor-facing draft. Use `BRAINSTORM-LEDGER.md` for live agent questions/hypotheses and merge stable route answers into `DECISION-CHART.md`. If the user says **go comment**, use `BRAINSTORM-LEDGER.md` Peer Comment Loop, max four rounds, before asking Berktuğ routine clarifying questions.
15. **`wiki/principles/source-banks/hera-canonical-blocks.md`** — for **concept notes / 2-pagers with no donor template**: assemble blocks verbatim, fill only `{{slots}}`, end with a `Blocks used:` footer. Enforced by `scripts/check_block_reuse.py` in the red-team gate (see § Canonical block reuse).

## Workflow

1. Identify donor, program, deadline, word limits, section prompts, and submission status.
2. If the request is a strategy decision rather than a writing request, run decision-first mode before drafting.
3. If donor context is incomplete, ask targeted questions before drafting.
4. Classify register:
  - fellowship / movement / founder-led funder -> Aral voice;
  - tech / innovation / government / institutional -> operational or hybrid voice;
  - academic / research -> academic register.
5. Mirror the donor's criteria and language while preserving HERA's voice.
5b. **Package pre-flight (mandatory, blocking)** — if the work targets a portal field or section of an active package under `raw/proposals/<slug>/`, run the Package Pre-Flight below **before drafting a single sentence**. No pre-flight, no draft.
6. Draft one section at a time unless the user explicitly requests a full draft.
7. Use source-backed claims. If a claim lacks a source, mark it as `needs source`.
8. If a draft cites a named credential, translate it into reviewer-legible meaning in the same sentence. Do not assume the reviewer knows why GHAIN MENA, MIT Solve, AUB, IDRC, data.org, UNHCR, or any similar name matters.
9. Before final external-facing grant output, run the Quality Gates.
10. Before final external-facing grant output, run the Red-Team Gate (includes institutional open register + dossier kill-list when `DONOR-DOSSIER.md` exists).
11. After user corrections, capture durable pattern candidates rather than silently forgetting them.

## Package Pre-Flight (mandatory for portal fields — cannot be skipped)

**Why this exists:** corrections that live only in package files evaporate when a draft skips the package scan (coherence plan, 2026-07-04). This gate makes the scan structural, not optional.

Before drafting **any** portal field or section inside an active `raw/proposals/<slug>/` package:

0. **Question decode (before everything — the donor-empathy gate).** Output three short lines and wait for no objection before drafting: **Field job:** what this question is actually asking for (not what HERA wants to say) · **Reviewer check:** what a UNHCR/donor reviewer verifies with this field · **Trap:** the most likely wrong-angle answer (burying the lead, supply-driven fact dump, answering a neighboring question). Rationale: in the UNHCR chat, ~25% of all corrections were "you're not answering the question / what do they want to hear" (`raw/capture-logs/2026-07-07-unhcr-full-chat-feedback-taxonomy.md` class A). Vetoing a decode costs 5 seconds; vetoing a wrong draft costs 3–7 turns.
   **Decode content rule:** the three lines speak only about the donor question — never name vault files. REVISION-LOG, capture logs, and the dossier are *inputs* that inform the trap line; file names belong in the receipt, not the decode. **Strict mode:** if the user says **decode only**, stop after decode + receipt and wait for explicit approval before drafting.
1. **Paste-file grep** — search the package's canonical paste/portal-ready file for content already written in *other* fields. A fact used in another field does not repeat here (Pattern 17 class). Name which fields you checked.
2. **REVISION-LOG scan** — read the package `REVISION-LOG.md` entries relevant to this field or its neighbors. Berktuğ's prior corrections on this package outrank generic patterns.
3. **Guardrail files + package fact locks** — `DONOR-DOSSIER.md` kill list + any package capture logs for locked/gold field wording. The dossier (or package README) must state the **fact locks: canonical population, geography, ask size, forbidden claims** — and drafts may not import populations/geographies from other packages' answer entries or generic About blocks (ANS-* entries are donor-scoped; "adolescent mothers" leaked from UNHCR/AGD layers into IRUSA this way, 2026-07-07). **If the package has no dossier/fact locks yet, scaffolding them IS the next step — stop and create them before drafting any field.**
4. **ACTIVATION-INDEX match** — open `wiki/principles/patterns/ACTIVATION-INDEX.md`, load only the pattern rows whose trigger matches this field's shape.
4b. **Donor answer library — ASSEMBLY, not authorship** — if the field matches a recurring type in `wiki/principles/source-banks/answers/README.md` (sustainability, scaling readiness, cohort contribution, impact/results, lessons learned, team/ownership, AGD, partnership comparative advantage, **partnership goals**, etc.), grep the matching `answers/<field-type>.md` and, when an entry fits the register: **paste the entry text verbatim as the draft base. Edit only `{{slots}}` (donor name, geography, module, links) and trim whole sentences for the word limit. Do not re-author, re-order, or "improve" prose outside slots** — canonical answers are building blocks, and `check_answer_library.py` fails paraphrase drift by design. Re-verify listed facts against `wiki/evidence/`; cite the entry ID (or `none — reason`) in the pre-flight receipt. Writing from scratch is allowed only when no entry matches — and that approved draft must then be promoted (step 7). **Team/ownership fields:** also grep `wiki/principles/source-banks/team-member-grant-bios.md` (start with **ANS-TEAM-BIO-000** for Aral prestige anchor) and read `raw/capture-logs/2026-07-04-unhcr-section-e-ownership-revision-chain.md` before drafting. **Prestige weighting:** spend primary word budget on clinical-lead Harvard/JHU credentials; compress other bios; de-dupe prestigious institution names across the package per Pattern 17 (de-dupe class, `wiki/principles/berktug-noticing-patterns.md`) and Pattern 21 (prestige weighting, same file — not `wiki/principles/patterns/donor/021-*`).
5. **Emit a one-line pre-flight receipt** before the draft: `Pre-flight: paste ✓ (fields X, Y) · REV-log ✓ (REV-NNN…) · dossier ✓ · patterns [IDs or none] · answer-lib [ANS-XXX-NNN or none]`.
5b. **Portal plain-language pass** — before drafting prose, skim `wiki/principles/patterns/voice/050-portal-field-plain-language.md` (mechanism bridge, plain MNCH, population framing, enrollment not "outreach", block capacity, funder field presence). Run `voice/049-editorial-polish-moves.md` after structure is locked.
6. **Answer-library footer (gated field types)** — for sustainability, scaling-readiness, expertise-cohort-contribution, impact-results, lessons-learned, team-ownership, agd-inclusion, partnership-comparative-advantage, and **partnership-goals** portal fields, end the field draft with `Answer entry used: ANS-…` (or `Answer entry used: none — <reason>`). Before marking ready-for-paste, run `python3 scripts/check_answer_library.py <draft> --field-type <slug>`; exit 0 required.
7. **Promote-on-approval (the library grows by use)** — when Berktuğ approves a portal answer that was drafted with `Answer entry used: none` (no entry existed), add the approved text to the matching `answers/<field-type>.md` as a new `ANS-*` entry (schema in the library README, `{{slots}}` marked, source + outcome fields filled) in the same session — create the field-type file if the README index lacks the type (live-package pull satisfies the anti-overproduction rule). Next time that question type appears anywhere, it is a paste, not a rewrite. Skipping promotion re-creates the from-scratch problem this library exists to kill.

A draft delivered without the receipt line is **not ready for paste** — red-team must bounce it back.

## Institutional open (pre-first-paragraph)

For UN / multilateral / accelerator concept notes and 2-pagers:

1. Open with **CHH is…** (third-person org) — see `wiki/donors/institutional.md`
2. Follow immediately with **PoC table or bullets**
3. Do **not** open with literary vignette; donor empathy from dossier goes to problem section, not paragraph one
4. **Peer exemplar first** — run `wiki/concepts/workflow/cortex-grant-writing-process.md` Step 0c before shaping a new 2-pager; anti-memo register (pattern 024)
5. **No invented donor flattery** — alignment claims need vault source; strip sales-tone UN/agency praise (`wiki/principles/berktug-noticing-patterns.md` Pattern 11)

Rule: `.cursor/rules/cortex-grant-institutional-open-register.mdc`

## Aral concept-note default (no donor template)

When the deliverable is a **concept note / 2-pager** and the funder provides **no specific template or annex**, load and apply **`wiki/principles/aral-grant-review-rubric.md`** during draft and before red-team:

- ~½ page **About HERA** before project goal
- Warm **women/children** MNCH frame; simple activities; lane separation per funder
- Berktuğ-drafted docs use the **same bar** before **Aral pass**

Donor-prescribed structure **overrides** this rubric.

### Canonical block reuse (mandatory for these docs)

Consistency across HERA documents is enforced, not hoped for. Before authoring boilerplate:

1. Read **`wiki/principles/source-banks/hera-canonical-blocks.md`**.
2. **Assemble the relevant blocks verbatim** (About HERA, scale-up stats, MEDAK relationship, how-it-works, evidence disclaimer, navigation-lane-only). Fill **only** the marked `{{slots}}` (`{{donor}}`, `{{geography}}`, `{{reach}}`, `{{team_date}}`).
3. Write freely **only** for genuinely document-specific prose (problem mechanism lead, this donor's activities/ask). Do not paraphrase a block to "improve" it; if a block is wrong, propose a block-library edit instead.
4. End the draft with a footer: `Blocks used: HERA-ABOUT-01, HERA-SCALEUP-STATS, ...` listing every block reused.
5. The Red-Team Gate runs `python3 scripts/check_block_reuse.py <draft>`; a missing footer or paraphrased block is a **Blocker**.

Why: three prior "sound like HERA" systems drifted because style instructions are unverifiable. Verbatim blocks + an external diff check make reuse falsifiable. See `wiki/concepts/workflow/grant-tone-capsule-registry.md` (2026-06-15 retrieval-at-generation gap).

### Donor answer library reuse (mandatory for gated portal fields)

For portal fields matching **sustainability**, **scaling-readiness**, **expertise-cohort-contribution**, **impact-results**, **lessons-learned**, **team-ownership**, **agd-inclusion**, **partnership-comparative-advantage**, or **partnership-goals** (`wiki/principles/source-banks/answers/README.md`):

1. Read the matching `answers/<field-type>.md` during pre-flight 4b; **paste the fitting entry verbatim as the draft base** — edit `{{slots}}` and trim whole sentences only, never re-author outside slots — and re-verify every listed fact.
2. End the field draft with: `Answer entry used: ANS-SUST-004` or `Answer entry used: none — <reason>`.
3. Red-team runs `python3 scripts/check_answer_library.py <draft> --field-type <slug>`; missing footer, unknown ID, or paraphrase drift is a **Blocker**.

Field-type slugs: `sustainability` · `scaling-readiness` · `expertise-cohort-contribution` · `impact-results` · `lessons-learned` · `team-ownership` · `agd-inclusion` · `partnership-comparative-advantage` · `partnership-goals`. Enforced outside the model — same class as `check_block_reuse.py`. All gated fields also run `voice/050-portal-field-plain-language.md` before paste.

### Grantfather field triggers (single rulebook: `wiki/concepts/workflow/grantfather.md`)

Detailed rules live in **one home** — `wiki/concepts/workflow/grantfather.md` — never duplicated here (consolidation 2026-07-07, CI-TURN-068/070). When a field matches, LOAD the named section and follow it:

| Field shape | Load grantfather.md section |
|-------------|----------------------------|
| "Briefly describe your organization" (≤200w org field) | § Canonical org description — `HERA-ORG-DESC-01` verbatim opening, proof stats after, register per pattern 043 |
| Donor/partner **unique role / comparative advantage** | § Partnership affinity ladder (A→B→C, proposal-vs-prize naming, merge storytelling) + § Line-level register (Pattern 044) |
| Any partnership/role/comparative paragraph before finalize | § Line-level register — Pattern 044 six moves, sister-org rule, budget discipline (045), banned filler phrases |
| Contribution to **program initiatives / peers / ecosystem** (plural) | § Cohort contribution fields — five-beat shape, observational register (NOT 044 warmth), gold reference |

Invoke phrase without an active package: **I am working on Grantfather**.

## Decision-First Mode

Use this mode before drafting when the user is deciding:

- whether to apply;
- which stage, pathway, eligibility route, or funding amount fits;
- which geography, partner stack, lead applicant, or consortium shape to choose;
- whether evidence is strong enough for a claim;
- whether a new note, pattern, skill, rule, workflow, or agent should be created from a grant conversation.

For these prompts, load `skills/context-navigator/SKILL.md` and return a **Decision Pick** instead of a polished draft.

Default Decision Pick structure:

- **A — recommended/default**
- **B — conservative / lower-risk**
- **C — ambitious / higher-upside**
- **D — pause / research / waiting-on**

Each option must state:

- fit with the donor/program criteria;
- evidence requirement and missing sources;
- budget/partner/geography implications;
- what would make the option too stretched or unsupported;
- next file/skill/action.

Output contract for decision-first prompts:

- Start with `**Decision Pick — [task name]**`
- Return exactly four visible options: `A)`, `B)`, `C)`, `D)`
- Then return:
  - `Default: ...`
  - `Next: ...`

Do not replace this with a prose memo, bullet summary, "bottom line", or sectioned analysis. If the request is strategic and pre-draft, the Decision Pick block is mandatory.

For the canonical fresh-chat test prompt `We are unsure whether to apply Stage 1 or Stage 2 for DIV with SAMS/JHU; use Cortex.`, follow the passing example in `skills/context-navigator/SKILL.md` instead of creating a memo/table variant.

Do not create a new durable workflow or pattern from the decision unless Berktuğ explicitly approves it and the candidate passes deduplication. Prefer updating the relevant donor page or workflow that will be invoked later.

## Donor Register Routing


| Grant type                      | Start with                         | Voice                                                     | Pattern activation                                                                                                                          |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Fellowship / founder-led        | `wiki/donors/fellowship-grants.md` | `wiki/principles/source-banks/aral-voice.md`              | `wiki/principles/patterns/applicant-voice/012-aral-opener.md`, voice patterns                                                               |
| Tech / innovation               | `wiki/donors/tech-innovation.md`   | `wiki/principles/source-banks/berktug-voice.md` or hybrid | `wiki/principles/patterns/donor/013-yc-company-description.md`, `wiki/principles/patterns/donor/014-unlike-solutions-from-north-america.md` |
| Institutional / UN / government | `wiki/donors/institutional.md`     | institutional / hybrid                                    | `wiki/principles/patterns/structure/010-anti-parallel-line.md`, `wiki/evidence/proof-points.md`                                             |
| AI / technical                  | `wiki/donors/ai-technical.md`      | technical / evidence-led                                  | `wiki/principles/patterns/donor/021-google-org-government-deployment-framing.md`, `wiki/principles/patterns/evidence/`                      |
| Budget-heavy                    | relevant donor file + project file | ops / technical                                           | `wiki/principles/patterns/budget/`                                                                                                          |


If the grant type is unclear, ask whether the funder is investing primarily in the founder/mission, the technology, institutional delivery, research, or budgeted implementation.

## Universal Pattern Activation

For most HERA grants, check these before drafting:

- `wiki/principles/patterns/ACTIVATION-INDEX.md`
- `wiki/principles/patterns/voice/001-person-first.md`
- `wiki/principles/patterns/structure/005-field-realism-over-tech-idealism.md`
- `wiki/principles/patterns/donor/039-reviewer-legibility-for-credentials.md` when any credential, award, funder, partner, acronym, platform, or technical initiative is cited
- `wiki/principles/patterns/structure/010-anti-parallel-line.md`
- `wiki/principles/patterns/structure/040-designed-for-mobility-not-stasis.md` when replication, scaling, innovation, or problem framing touches displacement or mobility — **mandatory two-sentence block verbatim**
- `wiki/principles/patterns/structure/011-co-created-with-communities.md`
- `wiki/principles/patterns/structure/023-never-mention-fallback-rate-externally.md`
- `wiki/principles/patterns/voice/006-crisis-affected-women-and-girls.md`

Apply only the patterns relevant to the section. Do not dump every pattern into the output.

## Grant tone mining (optional)

On substantive donor-facing drafting turns, **`skills/grant-tone-miner/SKILL.md` § Capture Triage** runs by default (see `.cursor/rules/cortex-universal-routing.mdc` §1b); surface micro/full capture only per that skill’s tiers.

When drafting a section that matches a **tracked proposal** (Echoing Green, YC, USAID DIV, Agency Science Prize, etc.), load **`raw/capture-logs/2026-05-11-hera-proposal-tracker-import.md`** and use **Proposal Classification** first (constraints + Col F approved blocks); use the **Approved Phrases** sheet in that file for short locked lines only. **Slices:** Echoing Green `raw/capture-logs/2026-05-13-hera-proposal-gold-supplement-part-2a-echoing-green.md`; YC `raw/capture-logs/2026-05-13-hera-proposal-gold-supplement-part-2b-yc-w25.md`; USAID DIV `raw/capture-logs/2026-05-13-hera-proposal-gold-supplement-part-2c-usaid-div.md` (**go 2c** — full app + study design `raw/proposals/usaid-div-2021/`, bib `wiki/evidence/proposal-reference-library.md`, **RCT playbook** `wiki/evidence/usaid-div-rct-methodology-playbook.md`, tone `raw/capture-logs/2026-05-31-grant-tone-capsule-usaid-div-gold-standard.md`); remaining rows `raw/capture-logs/2026-05-13-hera-proposal-gold-supplement-part-2d-remaining-bundle.md`.

When the user wants to **capsulate grant-writing tone** from **long external chats** (Claude / Perplexity / huge comment threads) into reusable rules and before/after pairs, use **`skills/grant-tone-miner/SKILL.md`** and follow **`wiki/concepts/workflow/grant-tone-mining-from-external-chats.md`**. That output feeds better drafts here; it does **not** replace donor-specific red-team.

## Evidence Activation

Use these for factual claims:

- `wiki/evidence/key-statistics.md` for core numbers;
- `wiki/evidence/proof-points.md` for general proof;
- `wiki/evidence/turkiye-temporary-protection-health-access-2026.md` when Türkiye temporary-protection health access, co-payments, or migrant health centres appear (mandatory for 2026+ grants — no blanket "free healthcare for refugees");
- `wiki/evidence/pilot-results.md` for pilot/user evidence;
- `wiki/evidence/jmir-preprint-97767-proposal-evidence-brief.md` for ANC/Türkiye MNCH preprint evidence (section mapping, claim ladder, DIV hypotheses) when drafting track record, evidence-to-date, M&E, or theory-of-change sections;
- project-specific files in `wiki/projects/` for current scope.
- `wiki/entities/recognition.md` plus `wiki/principles/patterns/donor/039-reviewer-legibility-for-credentials.md` for awards, media, funder validation, and named credibility signals.

If evidence is not in the vault, mark `needs source` and ask for the source rather than inventing it.

## Quality Gates

These are built-in grant-writer modes, not separate agents. Do not create a new agent or plugin just to run these checks unless Berktuğ explicitly asks and the agent-creation workflow approves it.

For every external-facing grant answer, application section, LOI, concept note, donor narrative, or public-facing revision, run these gates before the Red-Team Gate. For simple chat questions about a grant, run the Micro Gate only.

### Micro Gate

Use for quick grant questions, yes/no decisions, and short wording judgments.

Check internally:

1. What is the user actually asking?
2. Is there any factual or source risk?
3. Would a full draft/review workflow slow the user down unnecessarily?

Return the answer directly unless the question asks for donor-facing language.

### 1. Prompt / Relevance Gate

Before polishing language, identify the job of the prompt:

- question asked;
- section type;
- character or word limit;
- donor criteria named in the prompt;
- what a reviewer must understand after reading this answer.

Then check the draft:

- Does the first paragraph answer the actual prompt, not a neighboring prompt?
- Is each paragraph doing one of these jobs: direct answer, field evidence, lived authority, donor fit, story, or impact pathway?
- Is any paragraph mostly setup, mood, prestige, or abstraction without answering the prompt?
- If a sentence were removed, would the answer become more direct? If yes, cut or rewrite it.

Do not let a beautiful sentence survive if it is not useful for this exact question.

### 2. Sentence-Function Gate

Use this gate for high-stakes drafts, tight character limits, and any time Berktuğ says the writing feels generic, AI-like, too long, too polished, or not in the right voice.

For each sentence, ask:

- What claim does this sentence make?
- Is it answer, evidence, story, bridge, voice, or filler?
- Is it concrete enough to survive a skeptical reviewer?
- Does it preserve useful user/source wording, or has it been sanitized into generic proposal prose?
- Does it introduce a new abstraction that needs explanation?

Only keep sentences that earn their space. Prefer user-provided phrasing when it carries clearer HERA logic than the generated version.

### 3. Voice / Register Gate

Use `skills/voice-dna/SKILL.md` and the relevant source bank when voice matters.

Check:

- founder-led / movement funder -> Aral voice and moral urgency;
- implementation / technical funder -> operational or hybrid voice;
- institutional donor -> formal clarity without flattening HERA;
- activist-friendly request -> anti-extractive, anti-dependency framing without unsupported claims.

The output should not sound like generic NGO language, startup language, or AI-polished symmetry. It should preserve HERA's field realism: systems designed around people who stay put, continuity of care for people in motion, community-shaped infrastructure, and no parallel system unless that is the actual strategy.

### 4. Fact / Claim Gate

Before finalizing:

- verify exact numbers, dates, awards, partner names, geographies, and current donor facts;
- scope metrics precisely: who, where, when, and whether they are internal tracking, peer-reviewed evidence, or public claims;
- mark unsourced claims as `needs source`;
- do not use a prestige signal unless it is reviewer-legible in the same sentence;
- remove claims that are true in another proposal but irrelevant to this prompt.

### 5. Synthesis Gate

Resolve conflicts in this priority order:

1. factual accuracy;
2. relevance to the prompt;
3. donor fit and reviewer psychology;
4. HERA/Aral/Berktuğ voice;
5. style polish.

Show the revised final answer only, unless the user explicitly asks to see the critique, analysis, or alternative drafts.

### 6. Organization style gate (always on)

**Baseline audit (2026-06-15):** on four gate pairs from `raw/capture-logs/`, proposal edits were **100% RULE + BOUNDARY**; this gate is the primary fix — run before red-team, not after polish.

For all external submission text:

- **No em dash (Unicode U+2014): STRICT, always on, not opt-in.** This is an AI-writing signature; HERA external text must not carry it. Do not patch by swapping — for a comma in the same sentence shape. **Form sentences that never need the dash**: parentheses or a separate sentence for asides; colon or new sentence for elaboration; "including" / "such as" for lists. En dash (–) allowed in numeric ranges only. Sole exception: a portal template that itself forces em dashes. Full rule: `skills/voice-dna/SKILL.md` § Hard Rule. Self-check final text for U+2014 before returning.
- **No pre-gate vendor lock-in:** do not commit to irreversible production configuration of a named vendor AI stack before agreed internal evaluation (e.g. Bedrock before Will/Lars + product backlog); prefer **staging / evaluation / under review** language. Capsule: `raw/capture-logs/2026-05-12-grant-tone-capsule-sara-aws-imagine-samples.md`.
- **No internal governance in funder-facing fields:** keep HERA's internal experiment/ops controls out of donor text — no "exit criteria," kill-criteria, experiment-inheritance, or staging-governance language in funder-facing fields. A funder reads outcomes, milestones, and what you will deliver; the internal control process is not theirs to see and reads as hedging. State the result, not the governance mechanism. (Baseline-audit finding 2026-06-15, same Sara AWS capsule.)
- **Named funded object when the form expects it:** quote the project or deliverable name the donor form uses (e.g. **the project "AWS Safe Scale Layer"**) instead of a generic capability label; prefer **including** lists over em-dash stacks for component enumeration.

## Red-Team Gate

For any final external-facing proposal, LOI, concept note, application answer, donor narrative, budget narrative, or uploaded proposal revision, use:

`skills/grant-red-team-reviewer/SKILL.md`

This gate is automatic. Do not wait for the user to ask.

Process:

1. Draft or revise the grant content.
2. Run the Quality Gates and revise the draft.
3. Run an internal red-team pass using the reviewer skill.
4. Fix blockers and major issues before showing the final answer.
5. Show the final revised output, not the unrevised first draft.
6. Add exactly one short footer: `Red-team pass applied: [1-3 key changes].`

If the user explicitly asks for a critique, show the full red-team review instead of silently applying it.

If the user asks for "first draft only" or "no review" for an external-facing grant output, still run the red-team gate. The user may ask for critique-only mode, but not for an unsafe unrevised external draft.

Do not narrate internal loading, checking, or skill-gate steps. For final external-facing outputs, return only:

1. the revised donor-facing content;
2. one blank line;
3. exactly one footer beginning `Red-team pass applied:`.

The footer must describe only changes actually made in this response. Do not claim that prohibited material was removed unless the prompt or draft actually contained it.

If the user requests an unsupported claim, do not launder it into another broad claim. Either:

- mark `needs source` as a blocker; or
- replace it with source-backed HERA operational evidence and clearly avoid the unsupported outcome claim.

For clinical outcome claims such as mortality reduction, morbidity reduction, diagnostic accuracy, treatment efficacy, or population-level health impact:

- do not substitute with external literature effect sizes unless the source is already verified in `wiki/evidence/` or explicitly provided by the user;
- do not use pending-verification claims as donor-facing evidence;
- prefer `needs source` plus HERA operational metrics only.

Before final response, verify:

- red-team pass run;
- **Organization style gate (§6)** applied — U+2014 scan, funder/internal boundary, vendor lock-in, named project framing;
- relevance, sentence-function, voice/register, and fact/claim gates applied at a depth appropriate to the task;
- blockers fixed or marked `needs source`;
- pattern activation index checked for the current section/form;
- donor facts sourced or clearly caveated;
- exact HERA metrics scoped correctly;
- named credentials translated for reviewer legibility;
- prohibited claims removed;
- final answer is the revised version, not the first draft.
- exactly one footer token included: `Red-team pass applied: ...`.

Hard rule for failure/adaptation proof:

- For external grants, never mention AMTI fallback rate or `29% fallback`.
- Use earthquake response, the emergency chatbot redesign, or another approved adaptation story instead.

## First Response Format

For a new grant/opportunity, start with:

1. **Grant Fit / Strategy** — short read on fit and risk.
2. **Register** — Aral / Berktuğ-ops / institutional / technical / hybrid.
3. **Files I’m Using** — compact list of relevant donor/project/evidence/pattern files.
4. **Missing Inputs** — deadline, section prompt, word limit, donor criteria, or source gaps.
5. **Next Step** — propose outline or draft one section.

## Non-Negotiables

- Do not write to old `memory/` paths or Rowboat.
- Do not use unsupported numbers.
- Do not overclaim evidence, AI safety, clinical impact, or deployment scale.
- Do not use generic NGO/startup language when a HERA-specific pattern exists.
- Prefer concrete HERA facts, community co-creation, field realism, and source-linked evidence.
- Do not treat strong prose as successful until it passes prompt relevance.
- Do not skip the red-team gate for final external-facing grant outputs.

## Output Defaults

- For new opportunities: begin with a short fit assessment and recommended strategy.
- For drafting: provide one section at a time unless asked otherwise.
- For review: identify strengths, risks, missing evidence, tone mismatches, and suggested edits.
- **For field revisions (mandatory format):** open with a location line (`file § field`), then show the change **side by side** (OLD sentence → NEW sentence, changed parts only — never a silent full-paragraph reprint), then one line naming what fired (`per REV-034 / ANS-SCALE-001 / Pattern 044 / your comment`). Rationale: "which answer did you edit / where do I put comments / side by side pls" friction cost ~10% of all turns in the UNHCR chat (taxonomy class G).
