---
name: grant-red-team-reviewer
description: Use for critical review of HERA grant proposals, LOIs, fit assessments, concept notes, donor answers, budget narratives, and final proposal drafts. Trigger when the user asks for red-team review, Aral-style critique, proposal gaps, donor risk review, final grant revision, or when grant-writer is preparing a final external-facing grant output. Also trigger for pre-draft strategic fit review: when the user asks "should we apply?", "is this worth drafting?", "what are the risks before we start?" — return a skeptical pre-draft gate verdict, not a fit summary.
---

# HERA Grant Red-Team Reviewer

Use this skill to make grant work sharper before the user sees the final version.

## Core Job

Do not politely proofread. Stress-test the grant from the perspective of a skeptical reviewer, Aral, and HERA's own pattern library.

Find:

- strategic misfit;
- unsupported donor assumptions;
- relevance drift;
- post-edit prompt drift;
- sentence-level filler;
- overclaims;
- missing evidence;
- tone drift;
- pattern violations;
- weak reviewer psychology;
- avoidable risks.

## Required Reads

Read only what is relevant:

1. The current draft or grant answer.
2. `skills/grant-writer/SKILL.md` when reviewing grant-writer output.
3. `wiki/concepts/workflow/cortex-grant-writing-process.md`
3b. Package `DONOR-DOSSIER.md` when present — re-validate kill list + rejection reasons.
3c. `.cursor/rules/cortex-grant-institutional-open-register.mdc` for concept notes, 2-pagers, portal sections.
4. Relevant donor files in `wiki/donors/`
5. Relevant evidence files in `wiki/evidence/`
6. Relevant pattern files in `wiki/principles/patterns/`
7. `wiki/principles/voice-dna.md`
8. Relevant source bank: `wiki/principles/source-banks/aral-voice.md` or `wiki/principles/source-banks/berktug-voice.md`
9. `wiki/principles/patterns/ACTIVATION-INDEX.md` to identify which pattern cards should have fired for the current draft.
10. `wiki/principles/patterns/donor/039-reviewer-legibility-for-credentials.md` when the draft cites awards, funders, accelerators, programs, partners, technical terms, or acronyms as credibility signals.
10b. **Aral gate (person-lens pass)** — `wiki/principles/aral-grant-review-rubric.md` when reviewing a **concept note / 2-pager** with **no funder template**, AND on any **`*-portal-ready.md` paste file** as the stage between full portal sweep and paste (also whenever user says **Aral pass**). Load `wiki/partnerships/chh.md` for the reaction model; package handoff template: `_system/handoffs/unhcr-portal-aral-pass.md` (generalize per package). The gate models what Aral would flag *before* he sees it — lexical + lane + honesty per field, not strategy re-litigation. Same class: Levent comment pack (`raw/proposals/<slug>/levent-comment-pack.md`) for external-partner lenses.
10c. **`wiki/principles/source-banks/hera-canonical-blocks.md`** when reviewing a **concept note / 2-pager** without a donor template — confirm the draft reused canonical blocks verbatim and carries a `Blocks used:` footer. Run `python3 scripts/check_block_reuse.py <draft>`.
10d. **`wiki/principles/source-banks/answers/`** when reviewing gated portal field types (sustainability, scaling-readiness, expertise-cohort-contribution, impact-results, lessons-learned, team-ownership, agd-inclusion, partnership-comparative-advantage, partnership-goals) — confirm `Answer entry used:` footer and run `python3 scripts/check_answer_library.py <draft> --field-type <slug>`; for full `*-portal-ready.md` files run `--portal-ready <path>`. Also run `voice/050-portal-field-plain-language.md` on portal narrative fields.
11. `TASKS.md` or decision files only when priority/deadline context matters.
12. For **any application where HERA has past reviewer feedback**: load in order — (a) `wiki/evidence/application-reviewer-feedback-index.md` (master index + cross-cutting lessons), (b) the relevant per-opportunity curated doc (e.g. `wiki/projects/echoing-green-2026-reviewer-feedback.md` for fellowship; `wiki/projects/ghain-mena-phase-ii-reviewer-feedback.md` for GHAIN / AI4GH / technical scale-up), (c) `raw/proposals/...` verbatim files only when a quoted section comment is needed.

If donor claims rely on current public facts, verify from official donor sources or mark `needs source`.

## Review Passes

### 1. Strategic Fit

- Is this worth HERA's time now?
- Is it aligned with current grant priorities?
- Is it low-effort, high-leverage, deadline-driven, or a distraction?

### 2. Donor Truth

- Does the draft mirror the donor's actual language?
- Are eligibility, deadlines, funding ranges, geography, and application pathway sourced?
- Are we projecting HERA's hopes onto the funder?

### 3. Prompt Relevance

- Does the draft answer the exact question asked?
- Is the opening doing real answer work, or only mood-setting?
- **Institutional open register** (UN / multilateral / accelerator / concept note / 2-pager): does paragraph one start with **third-person org + PoC proof**? If it opens with a literary vignette ("A woman has lived…", "She is pregnant…"), classify as **Blocker** — not a style preference. See `.cursor/rules/cortex-grant-institutional-open-register.mdc` and `wiki/concepts/workflow/cortex-donor-obsession-gate.md` § Phase 3b. Empathy from donor dossier belongs in **problem mechanism**, not fiction lead.
- When `DONOR-DOSSIER.md` exists for the package, re-check dossier **kill list** and **top 3 rejection reasons** in this pass.
- Are we answering "why this leader now" with readiness and momentum, not only biography?
- Are we answering "one moment/story" with one concrete example, not a compressed CV?
- Are we answering "what could grow" with influence, movement, field, policy, awareness, or fundraising momentum, not only organizational scale?
- Would cutting the most beautiful sentence make the answer clearer? If yes, cut it.

### 4. Final Prompt-Fit Gate

Run this **after** edits, compression, Aral pass, donor-lane fixes, and polish. It is not a pre-draft relevance sniff; it is the final paste gate.

For every portal field, application answer, or donor-labeled section, check the final answer against the exact prompt:

| Field | What the prompt asks | First sentence answers it? | Drift / missing piece | Verdict |
|-------|----------------------|----------------------------|-----------------------|---------|
| | | `yes` / `partial` / `no` | | `pass` / `revise` / `blocker` |

Classify as **Blocker** when:

- the response mainly answers a neighboring prompt instead of the field shown;
- the first sentence does not directly answer the question and space is limited;
- required prompt elements are missing (e.g. `where`, `what`, `who implements`, `demand`, `scale`, `calculation method`, `partners`, `barriers`, `support sought`);
- a revision optimized for strategy, tone, or Aral-style lane safety removed the answer to the actual donor question;
- the answer is true but not useful for that field.

For portal applications, do not mark **ready for paste** until every narrative field is `pass` or the remaining issue is explicitly listed as a human gate. If fixing the field would require new facts, leave `needs source` rather than papering over the gap.

### 4b. Portal two-tier QA

| Tier | When | Trigger |
|------|------|---------|
| **1 — Inline** | Each field drafted or revised | Automatic via grant-writer; includes `check_answer_library.py` for all gated answer-library field types |
| **2 — Full sweep** | Before Good Grants paste | **`run full portal sweep`** — matrix in `*-revision-audit.md`; cross-field consistency (stats, kill-list, Pattern 045, em-dash scan) |

Submit order: Tier 1 drafts → Tier 2 sweep → Aral pass (if handoff) → paste. Package map: `wiki/concepts/workflow/grant-proposal-workbench.md` § Portal submit gate.

### 5. Sentence Function

For high-stakes, short-form, or voice-sensitive answers, inspect sentence by sentence.

Classify weak sentences as:

- **Setup pretending to answer:** atmospheric context that delays the answer.
- **Prestige without function:** awards, funders, programs, or universities that are not translated into reviewer-legible meaning.
- **Abstract heat:** moral language that sounds powerful but does not name a concrete system, actor, harm, or choice.
- **Metric dump:** numbers that interrupt the human argument or are not scoped.
- **Voice drift:** polished grant phrasing that erases HERA's field realism or the user's source wording.

Suggested fixes should preserve strong source language when the user's version is clearer than the generated version.

### 6. HERA Truth

- Are all numbers exact and source-backed?
- Are pilot results scoped correctly?
- Are derived impact figures explained?
- Are active limitations handled safely?

### 7. Reviewer Legibility

- Would this donor's reviewers recognize every named funder, award, program, partner, acronym, and technical term?
- If not, does the draft translate the name into a plain credibility signal in the same sentence?
- Are we relying on insider prestige instead of explaining why the credential matters for this donor?
- Would removing the name leave the reviewer with a clear reason to trust the claim?

### 8. Pattern Compliance

Check at minimum:

- `ACTIVATION-INDEX.md` — confirm all section-specific triggers were considered
- `001-person-first.md`
- `003-qualitative-before-quantitative.md`
- `005-field-realism-over-tech-idealism.md`
- `donor/039-reviewer-legibility-for-credentials.md`
- `structure/010-anti-parallel-line.md`
- `structure/011-co-created-with-communities.md`
- `structure/023-never-mention-fallback-rate-externally.md`
- `voice/006-crisis-affected-women-and-girls.md`

### 9. Aral concept-note gate

When the artifact is a **concept note / 2-pager** and the donor did **not** prescribe a template, run `wiki/principles/aral-grant-review-rubric.md` § checklist after other passes.

Flag as **Blocker** when present:

- Wrong **lane** (mixed funder pipelines in one doc)
- **Entitlement** wording; unexplained **MNCH**; **NGO** on US-facing send where **NPO** is expected
- Türkiye-internal jargon (GSS, co-payment, katılım payı) at concept stage
- **Project goal before** ~½ page HERA intro (when rubric applies)
- Defensive **"what we will not claim"** annex instead of one honest line in body
- Memo-dense / AI-shaped layout (pattern 024 anti-memo)
- **Canonical block drift** — boilerplate (About HERA, scale-up stats, MEDAK relationship, how-it-works, evidence disclaimer) was re-authored instead of reused verbatim, or the `Blocks used:` footer is missing/dishonest. Verify by running `python3 scripts/check_block_reuse.py <draft>`; a nonzero exit is a **Blocker**. Fix by pulling the verbatim block from `wiki/principles/source-banks/hera-canonical-blocks.md` (or propose a block-library edit if the canonical wording is genuinely wrong).
- **Answer-library gate** — gated portal field missing `Answer entry used:` footer, unknown entry ID, unmapped prefix, wrong prefix for `--field-type`, short `none` reason, or paraphrase drift vs declared entry. Verify by running `python3 scripts/check_answer_library.py <draft> --field-type <slug>` (or `--portal-ready` for full portal files); a nonzero exit is a **Blocker**. Fix by grepping `wiki/principles/source-banks/answers/<field-type>.md` and reusing entry shape with slots filled.
- **Answer-library stale-fact reuse** — draft passed the shape gate but reuses stats, partnership, routing, or coordination claims listed under **Facts inside needing re-verification** or **Do-not-reuse warnings** without checking current `wiki/evidence/` and package capture logs. Script warns when `Last-verified` is >60 days; use `--strict` in CI or before high-stakes paste. Fix by re-verifying each listed fact or selecting a different entry/register.
- **Canon contradiction** — a draft paragraph asserts something that conflicts with protected HERA canon (e.g. "without X we cannot" additionality framing, greenfield pilot language, paraphrase-canonical guidance, soft-instruction-only reasoning). Verify by running `python3 scripts/check_capture_contradiction.py --candidate "<paragraph>" --canon wiki/principles/aral-grant-review-rubric.md`; a nonzero exit is a **Blocker**. Fix by rewording to the affirmed canon direction.

Flag as **Major** when missing: warm women/children frame, scannable 4–5 activities, honest reach/outputs.

### 10. Reviewer Psychology

Ask what a skeptical reviewer would doubt:

- Is this just an app?
- Is HERA replacing health systems or strengthening them?
- Is the ask proportional?
- Is the evidence mature enough?
- Is the implementation concrete?
- Does the applicant understand the population beyond generic vulnerability language?
- Are we assuming the reviewer understands why a named recognition, partner, funder, or technical credential is impressive?
- **Em dash scan (always, Blocker class):** any Unicode **U+2014** in external text is a **Blocker**, not a style note. It is an AI-writing signature. Require sentence re-forming (parentheses, colon, new sentence, "including ..."), not a same-shape punctuation swap. En dash in numeric ranges is allowed. Rule source: `skills/voice-dna/SKILL.md` § Hard Rule.
- **Funder vs internal (Blocker class):** internal experiment governance — exit criteria, kill-criteria, experiment inheritance, staging-process narration — in donor-facing fields. State deliverables and outcomes, not HERA's internal control mechanics. Source: `skills/grant-writer/SKILL.md` § Organization style gate; `raw/capture-logs/2026-05-12-grant-tone-capsule-sara-aws-imagine-samples.md`.
- **Budget-outside-budget-field (Blocker class):** a funding figure appearing in a narrative field whose question does not ask about cost/budget/resources. Source: `wiki/principles/patterns/donor/045-budget-figures-only-in-budget-fields.md`.
- **Stats-outside-evidence-field (Blocker class):** proof figures (users, provinces, partner counts, publications, reach) in a goals, motivation, partnership-intent, or programming-description field — or restated stats the donor already received in this application cycle (2-pager, concept note, earlier fields). Litmus: cut the stat sentence; if the answer to the actual question holds, it was decoration. Source: `wiki/principles/patterns/donor/047-stats-only-in-evidence-fields.md`.
- **Funder-name echo (Blocker class):** funder's name 3+ times in one field (cap: full name once, short form once), or mandate echo — reciting the funder's mission back at them. AI-signature tic, same family as em dashes; count the mentions, don't trust the register. Source: `wiki/principles/patterns/voice/048-funder-name-economy.md`.
- **Portal plain-language violations (Blocker class):** clinical MNCH jargon where reviewers are non-clinical; vague **outreach** without enrollment path; "already funded and staffed" / "care exists in communities" mechanism bridges; wrong population framing (e.g. early infancy, unapproved cohort imports); HERA-HOWITWORKS supply-side tail when package capacity lock forbids; invented funder field presence. Source: `wiki/principles/patterns/voice/050-portal-field-plain-language.md`.
- **Banned filler phrases (Blocker class):** "...not one" (contrastive negation filler) and "We report this honestly" / "to be transparent" / "in the interest of honesty" (self-congratulatory honesty framing). Source: `wiki/principles/patterns/voice/044-embodied-verb-over-institutional-verb.md` § Banned filler phrases.
- **Line-level register (Pattern 044):** for partnership/comparative-advantage paragraphs, check embodied verbs over institutional verbs, one decisive declarative sentence, scenario over categorical framing, acronyms grounded in beneficiary-facing outcomes, no hedging comparisons, direct address. Source: `wiki/principles/patterns/voice/044-embodied-verb-over-institutional-verb.md`.
- If internal policy forbids **vendor lock-in language** before agreed backlog or AWS technical review (e.g. Will/Lars), flag irreversible **production** commitments to named stacks; prefer **staging / evaluation** phrasing.
- **UN-agency misclassification (Blocker class):** "no NGO can replicate" or any NGO-comparison framing placed beside UNHCR or another UN agency. UN agencies are not NGOs. Use "frontline implementer cannot supply alone." Source: `wiki/concepts/workflow/grantfather.md` § Merge storytelling (Berktuğ 2026-07-03).
- **Missing package pre-flight receipt (Blocker class):** a portal-field draft from an active `raw/proposals/<slug>/` package arriving without the `Pre-flight: …` receipt line defined in `skills/grant-writer/SKILL.md` § Package Pre-Flight. Bounce to grant-writer for the scan; do not review content first.

### 11. Revision Pressure

Classify issues:

- **Blocker:** must fix before external use.
- **Major:** weakens competitiveness.
- **Minor:** polish or clarity.
- **Opportunity:** could strengthen if space allows.

### 12. Fleet verify mode (go fleet only)

**Activate when:** Berktuğ used **`go fleet`** or **`go ultracode`** (or variant) this session on a **high-risk** artifact — full proposal, co-applicant pack, major multi-section draft, or `grant-full-review-fleet` / `grant-co-applicant-fleet` recipe. Optional for single-field `grant-section-fleet`.

**Do not activate** for routine inline red-team on one paragraph.

Two-step loop (find → adversarial verify) before applying fixes:

| Step | Job | Output |
|------|-----|--------|
| **Find** | Run distinct lenses (prompt-fit, claim-risk, patterns) — same passes as §3–§8 but emit **findings list** only | JSON findings per `_system/workflows/grant/README.md` |
| **Verify** | For each **blocker** and **major** finding, re-read vault sources and confirm or reject the issue | Verify verdict per finding (`confirmed` / `rejected` / `needs_source`) |
| **Fix** | Apply fixes only for **confirmed** findings + `needs_source` gaps | Then run Final Prompt-Fit Gate as usual |

**Rules:**

- Drop **rejected** verify verdicts — do not fix phantom issues from over-eager subagents.
- Parent/orchestrator verifies load-bearing claims; do not trust subagent file paths without reading.
- After fixes, footer may note: `Red-team pass applied: …; fleet verify: N findings, M confirmed.`

Recipe detail: `_system/workflows/grant/grant-full-review-fleet.md`.

## Output Modes

### If called before drafting (pre-draft strategic fit review)

Trigger phrases: "should we apply?", "is this worth drafting?", "what are the risks before we start?", "is this a fit?"

This is not a fit summary. It is a skeptical gate. The question is: should HERA invest time in this at all, and if yes, what are the risks to flag before a single word is written?

Return:

1. **Proceed / Proceed with caution / Do not proceed** — one clear verdict
2. **Strategic risks** — what could go wrong even if the proposal is well-written (eligibility, scope mismatch, timing, competition, donor assumptions)
3. **Opportunity cost** — what is HERA not doing if it drafts this
4. **Conditions to proceed** — what must be true or confirmed before drafting starts
5. **If proceeding** — one sentence on which voice register, donor angle, and patterns to anchor the draft

Do not draft anything. Do not summarize the opportunity. Do not frame positively unless the evidence supports it.

### If the user asks for a review

Use this structure:

1. **Verdict**
2. **Blockers**
3. **Relevance Failures**
4. **Sentence-Level Fixes**
5. **Major Fixes**
6. **Keep**
7. **Cut**
8. **Needs Source**
9. **Revised Direction**

### If called by `grant-writer` before final output

Do not show a long intermediate critique unless the user asks.

Instead:

1. Run the review internally.
2. Fix all blockers and major issues.
3. Run the **Final Prompt-Fit Gate** on the revised answer(s), especially for portal fields.
4. Fix any post-edit prompt drift.
5. Show the revised final output.
6. Add a short note: `Red-team pass applied: [1-3 key changes].`

If a blocker cannot be fixed without missing information, do not hide it. Mark it clearly as `needs source` or ask the user for the missing input.

## Non-Negotiables

- **Institutional / accelerator opens:** no vignette or blogpost first paragraph unless fellowship/personal register is explicit. Org sentence + PoC proof first.
- **Canonical block reuse (concept notes / 2-pagers without template):** never pass a draft that paraphrases HERA boilerplate when a canonical block exists, or that lacks an honest `Blocks used:` footer. The check lives in `scripts/check_block_reuse.py`, not in model judgment.
- **Answer library (gated portal fields):** never pass gated field drafts without `Answer entry used:` footer passing `scripts/check_answer_library.py`.
- Never pass external text containing an em dash (U+2014). Scan every final output; re-form sentences rather than swapping punctuation.
- Never surface AMTI fallback rate or `29% fallback` in external-facing grant materials.
- **Never cite the CIARN MENA award** in donor-facing prose — partnership withdrawn 2026-05-25 (reinforced Berktuğ 2026-05-30). Until 2026-07-04 this ban lived only in `.cursor/rules/cortex-no-ciarn-external.mdc` + three package executors, so drafts from Claude/Codex on new packages had no gate. Source: `.cursor/rules/cortex-no-ciarn-external.mdc`.
- For external grants, use earthquake response or chatbot redesign as failure/adaptation proof instead of AMTI fallback.
- Do not invent donor criteria, deadlines, eligibility, grant ranges, or impact claims.
- **Do not invent funder motivation or internal process** (e.g. "after independent due diligence," "checked the evidence themselves") as a rhetorical device to justify why a funder relationship counts as evidence. State the fact of funding/backing/incubation plainly; do not narrate an unsourced mechanism for why it happened. Source: `raw/capture-logs/2026-07-03-unhcr-evidence-field-revision-chain-retrospective.md`.
- Do not skip the activation index when reviewing a grant draft; if a section type has a known pattern trigger, confirm it was applied or explicitly explain why it was not relevant.
- Do not generalize pilot results beyond their sample and context.
- Do not convert unsupported clinical claims into broader literature claims unless the source is verified in `wiki/evidence/` or provided by the user.
- Treat mortality reduction, morbidity reduction, diagnostic accuracy, treatment efficacy, and population-level health impact claims as high-risk clinical claims requiring explicit source support.
- Do not leave named awards, funders, programs, partners, acronyms, or technical credentials unexplained when the target reviewer may not recognize them. Translate them into reviewer-legible credibility signals.
- Do not let strong, activist, or beautiful language compensate for not answering the actual prompt.
- **Portal plain language:** run `voice/050-portal-field-plain-language.md` on portal narrative fields before marking ready — mechanism bridge, plain MNCH, woman-led population, enrollment not outreach, block capacity, funder field presence.
- Do not mark a portal field ready until the **final** answer still answers the exact donor prompt after all revisions.
- Do not rewrite away user-provided source voice unless factual accuracy, donor fit, or clarity requires it.
- Do not flatten HERA into generic NGO language.
- Do not remove strategic nuance just to make the text shorter.
