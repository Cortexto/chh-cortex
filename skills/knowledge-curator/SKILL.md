---
name: knowledge-curator
description: Use when adding, updating, or organizing HERA Cortex knowledge: new facts, project updates, partner information, donor intelligence, evidence, recognition, decisions, raw-to-wiki promotion, task candidates, or when the user says "update Cortex", "add this to the knowledge base", "save this", "where should this go", or "put it in the relevant parts".
---

# HERA Knowledge Curator

Use this skill to place information in the correct Cortex location without creating duplicate knowledge systems.

## Required Reads

1. `CORTEX.md`
2. `_system/SYSTEM-DECISIONS.md`
3. `wiki/concepts/workflow/cortex-triage-matrix.md`
4. Relevant existing `wiki/` page(s)
5. `TASKS.md` when task candidates may be created

## Folder Contract

- Land original source material in `raw/`.
- Promote durable knowledge to `wiki/`.
- **Competitors & market analogues:** one org per `wiki/competitors/{slug}.md`; index at `wiki/competitors/00-index.md`; workflow `wiki/concepts/workflow/competitor-collaborator-capture.md`.
- Keep operating metadata in `_system/`.
- Keep durable tasks in `TASKS.md`.

## Competitor / collaborator writes

When filing from meetings or Aral forwards:

1. Read `wiki/concepts/workflow/competitor-collaborator-capture.md`.
2. Use `wiki/competitors/_template.md` for new orgs; patch existing pages instead of duplicating.
3. Every meeting-sourced fact needs a **HERA mentions** row linking `raw/fireflies/...` or `raw/meetings/...`.
4. Update `wiki/competitors/00-index.md` when adding a new slug.
5. Do not invent scale, funding, or geography — mark `verify` if only hearsay.

## Promotion Rules

- Anything promoted from `raw/` into `wiki/` needs a `Source(s)` section linking back to the raw file.
- Do not promote low-signal details just because they were mentioned.
- Check whether the fact, task, pattern, or decision already exists before adding it.
- If uncertain, create a verify/open-question item rather than turning uncertainty into fact.
- **Bulk promotions** (many raw files at once, multi-source reconciliation, or dedup against existing wiki) → run `.cursor/rules/cortex-multi-agent-orchestration.mdc`: fan out per-source extraction across distinct-lens agents, merge on one surface, and run a verify/red-team pass before writing. A single-fact save stays a direct edit — no fleet.
- **Contradiction check before wiki write:** before promoting any candidate that makes a claim about HERA's approach, evidence, or strategy, run `python3 scripts/check_capture_contradiction.py --candidate "<claim>" --canon <relevant wiki/principles file>`. A nonzero exit means the claim conflicts with protected canon — reword or mark `verify` before writing. Do not promote a contradictory claim into `wiki/`.

## Promotion-Completeness Smoke Test

Before finishing a wiki update from raw meeting, transcript, Trello, email, or capture-log material, check whether the update should land in more than one layer:

- **Project layer:** project-specific implementation facts, partner dependencies, deadlines, and pending actions.
- **Decision layer:** dated strategic or operational choices.
- **Evergreen concept layer:** current platform, roadmap, architecture, evidence, donor, workflow, or reusable reference summaries.

Run this smoke test when the source updates platform-wide status, roadmap requirements, implementation status, grant-delivery metrics, architecture, privacy, Langfuse, AMTI, Twilio, AWS, surveys, or repeated project-wide dependencies.

Checklist:

1. Identify every current wiki page that already summarizes the topic.
2. Compare the raw source date against each page's `updated:` and visible `Last updated` / status line.
3. If a project page is updated but an evergreen summary is older and still speaks as current, patch the evergreen summary with a short sourced status update.
4. If the evergreen page intentionally stays unchanged, note why in the final response.
5. Do not duplicate full project detail into the evergreen page; add only the status/date/source layer needed to prevent stale guidance.

## Output Defaults

- If asked to update files, make the minimal relevant edits.
- If asked where something belongs, recommend the destination first.
- If new tasks are implied, add or propose them only after checking for duplicates.
- **Mandatory dedup receipt:** any durable file creation (including "capture this" requests) must be preceded by the visible `Dedup: searched … → updating X / no home, creating Y` line per `wiki/concepts/workflow/deduplication-protocol.md` § Mandatory dedup receipt. Updating an existing file is the default; creation is the exception that must be justified by the receipt.
- Never remove or mark tasks complete without human approval.

## Prohibited Writes

- Do not write to Rowboat `knowledge/`.
- Do not write to old `memory/` paths.
- Do not treat parent repo files as canonical for Cortex.
