---
name: transcript-triage
description: Use when processing HERA meeting transcripts from Fireflies, Granola, or raw/fireflies; normalize noisy terms, extract decisions, score task candidates, propose knowledge promotions, surface open questions, and avoid direct TASKS.md or wiki promotion without approval.
---

# Transcript Triage

Use this skill to turn noisy meeting transcripts into weighted task and knowledge candidates without over-promoting raw conversation.

## Default Behavior

- Read transcript source files from **`raw/fireflies/`**, **`raw/meetings/`**, **`raw/email/`**, or **`raw/capture-logs/`** — vault-first; do **not** call Granola or Fireflies MCP if landed material exists (`.cursor/rules/cortex-vault-first-meeting-context.mdc`).
- Return a dry-run triage report in chat by default.
- Do not edit `TASKS.md` unless explicitly approved.
- Do not promote facts into curated `wiki/` pages unless explicitly approved.
- Do not change `_system/state/fireflies_extract.json` unless explicitly asked to process and mark specific source files.
- Keep source links to the transcript file for every proposed task, decision, or knowledge update.

## Required Reads

Read only the relevant parts, in this order:

1. `wiki/concepts/workflow/transcript-to-tasks-priority-matrix.md`
2. `wiki/concepts/workflow/cortex-triage-matrix.md`
3. `wiki/concepts/workflow/deduplication-protocol.md`
4. `_system/state/fireflies_extract.json` when processing files idempotently
5. `TASKS.md` before proposing task additions
6. Relevant `wiki/projects/`, `wiki/partnerships/`, `wiki/donors/`, `wiki/entities/people/`, `wiki/competitors/`, or `wiki/concepts/decisions/` only when checking a proposed destination
7. `wiki/concepts/workflow/competitor-collaborator-capture.md` when Aral or others name competitors, analogues, or collaboration targets

## Processing Steps

1. Identify the transcript source and date.
2. Normalize likely transcript errors before interpreting content.
   - Examples: `AAUB`/`AAB` -> `AUB`; `ANGA` -> `UNGA`; `MNE` -> `M&E`; `Saray` -> `Sara`; `Aja` -> `AJA Foundation`; `Tower`/`Honey` -> likely `Thaura`/`Hani` but verify before external use.
   - **Fireflies speaker labels (required when `Speaker N` diarization present):** see **§ Fireflies diarization** below — never promote tasks/decisions from `Speaker 1`/`Speaker 2` lines alone without a speaker map or self-intro pass.
   - Apply phonetic matching for names, companies, and funders when context is strong, but mark `verify` before any external-facing use.
3. Apply recency and staleness checks before scoring tasks.
   - Urgency is relative to the transcript date, stated due date, and current date.
   - Do not treat old "urgent" language as current urgency without checking whether the task is already completed, superseded, expired, or no longer strategically relevant.
   - For grant/proposal tasks, check whether the opportunity is still active, submitted, won/lost, historical, or deadline-passed before promotion.
   - If current status is unclear, mark `verify`, `insufficient_source`, `supersedes_existing`, `exact_duplicate`, or `too_low_signal` instead of recommending a new task.
4. Split the transcript into distinct units: decisions, tasks, project facts, contact intel, opportunities, risks, waiting-on items, **competitor/collaborator intel**, background, noise, and verify items.
4b. **Competitor & collaborator pass (required when Aral is a participant):** Scan for organization names and phrases like *competitor, same space, like us, integrate with, learn from, alternative solution*. For each hit:
   - Normalize org name and assign slug (`wiki/competitors/{slug}.md`).
   - Classify `competitor` | `collaborator-adjacent` | `platform-vendor` | `inspiration` per `wiki/concepts/workflow/competitor-collaborator-capture.md`.
   - Add to **Knowledge Candidates** with suggested destination `wiki/competitors/...`.
   - Under **Recommended Wiki Updates**, specify **create** (from `wiki/competitors/_template.md`) or **patch** (append **HERA mentions** row with transcript date + path).
   - Do not write wiki files unless the user explicitly approves or says `go file` / `update competitors`.
5. Extract task candidates only when there is a clear owner, explicit request, deadline, dependency, or repeated emphasis by Aral/Berktuğ.
6. Score task candidates using the transcript priority formula:
   `Deadline x3 + Strategic value x3 + Aral emphasis x2 + Contact leverage x2 + Effort efficiency x1`.
   Each input factor is scored 1-5. Aral emphasis includes explicit post-session notes if they are source-linked and strategically directive.
7. Score non-task knowledge using the Cortex triage matrix.
8. Run task dedup reasoning against `TASKS.md` and `wiki/inbox/triage/` before recommending any `TASKS.md` addition.
9. Run knowledge dedup reasoning against relevant `wiki/` pages before recommending any durable wiki update.
10. Run the promotion-completeness smoke test below before finalizing recommended wiki updates.
11. Keep speculative, low-signal, stale, expired, or ambiguous material in `raw` / `verify`, not in durable tasks or wiki.

## Fireflies diarization (required normalization)

**Trigger:** `Speaker 1` / `Speaker 2` labels, `fireflies_id` in frontmatter, or `fireflies_capture: direct-meeting-recording`.

**Known failure modes (HERA vault):**

| Mode | Symptom | Example |
|------|---------|---------|
| **Label reuse** | Same `Speaker N` = different humans in one file | UNHCR Levent call — `Speaker 1` = Aral **and** Levent |
| **Direct recording split** | One presenter split across multiple speaker IDs | Elevate webinar — **Alex = Speaker 4**; short `Speaker 2` "Indeed" lines = co-host bleed |
| **False Speaker 1 presenter** | Berktuğ report: direct Fireflies recording often mis-tags; **do not assume Speaker 1 = main speaker** | Always find self-introduction or use landed `speaker_map` |

**Required steps before scoring content:**

1. Check raw frontmatter for `speaker_map`, `speaker_map_note`, `diarization_quality`.
2. If absent, build a **provisional map** from: self-introductions, name mentions, language switches, Q&A turn-taking.
3. In triage output **Normalized Terms**, include a **Speaker map** row (even if partial).
4. Treat isolated `Indeed` / `Yes` / `Yeah` lines on low-numbered speakers as **noise** unless mapped to a named person.
5. When landing new Fireflies raw files, add `speaker_map` to frontmatter when Berktuğ or transcript confirms attribution.

**Canonical examples:** `raw/meetings/2026-06-23_unhcr-levent-partnership-call-transcript.md` · `raw/meetings/2026-07-02_elevate-prize-2027-application-webinar-transcript.md`

Also codified in `wiki/concepts/workflow/cortex-triage-matrix.md` § Fireflies diarization.

## Promotion-Completeness Smoke Test

Before finishing any transcript/meeting promotion, check whether the source updates both a project page and an evergreen concept/reference page.

Trigger this smoke test when the source includes any of:

- product roadmap, Trello roadmap, PM tasks, requirements, implementation status, or grant-delivery roadmap;
- platform-wide AMTI, Langfuse, metrics, survey, Twilio, AWS, privacy, or architecture updates;
- wording like `Last updated`, `current status`, `roadmap`, `implementation status`, `Req 1`, `Req 2`, `Req 3`, or `Knowledge Routing`.

When triggered:

1. Search for existing evergreen pages in `wiki/concepts/tech/`, `wiki/concepts/workflow/`, `wiki/evidence/`, or `wiki/donors/` that summarize the same system-level topic.
2. If project pages are recommended, also ask whether an evergreen summary needs a small status/source update.
3. Compare source date with the candidate evergreen page's `updated:` / `Last updated` fields.
4. If the source is newer and materially changes status, add the evergreen page to **Recommended Wiki Updates** with dedup class `partial_overlap` or `supersedes_existing`.
5. If no evergreen page should change, state that explicitly under **Open Questions / Verify** or **Noise / Raw-Only**.

Smoke-test example: if an Apr 30 tech call updates Langfuse status, MSD survey timing, and InterSOS implementation dependencies, checking only `wiki/projects/dory-foundation-2026.md` and `wiki/projects/intersos-greece.md` is incomplete. Also check `wiki/concepts/tech/roadmap-2026.md` and `wiki/concepts/tech/langfuse-observability.md`.

## Output Contract

Return these sections unless the user asks for another format:

1. **Source**
2. **Normalized Terms**
3. **Decisions**
4. **Task Candidates With Scores**
5. **Knowledge Candidates**
5b. **Competitor / Collaborator Updates** (table: Org | Relationship | Action create/patch | Facts to add | Source line | verify?)
6. **Recommended `TASKS.md` Additions**
7. **Recommended Wiki Updates**
8. **Open Questions / Verify**
9. **Noise / Raw-Only**

For task candidates, use:

| Candidate | Owner | Due date | Deadline | Strategic | Aral emphasis | Contact leverage | Effort efficiency | Score | Tier | Dedup status | Source |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|

For knowledge candidates, use:

| Candidate | Type | Suggested destination | Signal score | Dedup status | Source |
|---|---|---|---:|---|---|

`Dedup status` must use the deduplication protocol classes only: `exact_duplicate`, `near_duplicate`, `partial_overlap`, `supersedes_existing`, `conflicts_existing`, `new_unique`, `insufficient_source`, or `too_low_signal`.

Do not use vague dedup labels such as `likely new`, `check TASKS`, or `dedup needed` in final tables. If a full check was not completed, use `insufficient_source` or state the needed check under **Open Questions / Verify**.

## Promotion Rules

- `TASKS.md` additions are recommendations only unless the user explicitly asks to add them.
- Wiki updates are recommendations only unless the user explicitly asks to write them.
- Decisions and open questions are recommendation-only unless explicitly approved and dedup-checked.
- Only Tier 1 task candidates can be recommended for `TASKS.md`; Tier 2 and Tier 3 stay in the report unless the user explicitly asks to promote them.
- If an item duplicates an existing task/fact/pattern, link the existing item instead of creating another.
- If a transcript item conflicts with current canon, mark `verify`; do not silently overwrite.
- If the user requests `return only`, `report only`, `dry-run only`, `strict format`, or `no narration`, suppress process narration and output only the requested report sections in the required order; do not add preambles like "I'm reading/checking/extracting" and do not add extra sections unless asked.

## Collective-brain reflection gate (after triage)

When triage completes and the user asked for vault population (or you wrote `wiki/` / `TASKS.md` recommendations), run `skills/collective-brain-reflection/SKILL.md` **before closing the session**. See `.cursor/rules/cortex-transcript-collective-brain-gate.mdc`.

- Weight **Aral** and **Sara** lines for operating principles, donor-scope boundaries, and partner discipline — not only scored tasks.
- Surface Tier-2 items and person-signal candidates in the reflection report even if omitted from `TASKS.md`.
- Do not promote to `wiki/entities/people/` or `wiki/concepts/decisions/` without approval.
