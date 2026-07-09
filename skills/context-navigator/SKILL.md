---
name: context-navigator
description: Use when a Cortex task is ambiguous, when the user is unsure which skill/context/tone/files to use, or before drafting a personal application, grant, email, profile, meeting-derived task, transcript/email triage, or other mixed request where multiple Cortex skills could apply. Presents a compact context menu of likely skills, voice/person context, wiki files, and asks for confirmation only when the route is genuinely ambiguous.
---

# Cortex Context Navigator

Use this skill as the lightweight “which brain should I load?” layer.

The goal is not to slow the user down. The goal is to prevent silent wrong routing: wrong voice, wrong person context, wrong skill, wrong source files, or wrong write behavior.

## When To Use

Use before answering when:

- the user asks “which skill/context should we use?” or “do we have a skill/agent for this?”;
- the task could reasonably route to multiple skills;
- the prompt is a personal application/form/profile/bio and the speaker/applicant could matter;
- the prompt says “use Cortex,” “look at my patterns,” “use relevant context,” or “don’t start from scratch”;
- the user is pasting a large messy form, email, meeting note, transcript, or grant opportunity;
- the task requires choosing between Aral voice, Berktuğ voice, institutional voice, donor voice, or team voice;
- **Vague short openers** — e.g. only a grant/donor/project name with no verb (“AWS Imagine Grant”, “DIV”) or under ~30 words without a clear deliverable;
- **Cursor:** `.cursor/rules/cortex-universal-routing.mdc` flags the turn — always follow that rule’s pick requirement when it applies.

Only **skip** this skill’s pick menu for **narrow** single-route tasks, and only when the user already specified the route:

- “Prepare weekly update for Aral” (or equivalent) → `skills/weekly-aral-email/SKILL.md` only;
- “Triage `raw/email/…`” with explicit paths → `skills/email-triage/SKILL.md` only;
- “Process this transcript” **with** the transcript file attached or path given → `skills/transcript-triage/SKILL.md` only;
- user included an explicit bypass in the same message (`skip pick`, `go`, `draft now`, etc.) per universal routing rule.

If unsure whether the task is narrow, **use this skill** — false-positive picks are cheaper than wrong routing.

## Fast Workflow

1. Read `_system/AGENTS-AND-SKILLS.md` only enough to identify candidate skills and routers.
2. Read `_system/HOT_CACHE.md` only if current phase/status matters.
3. Decide whether the user needs a **Context Pick** or **Decision Pick**:
  - **Context Pick** = which skill, voice, person context, or files should be loaded.
  - **Decision Pick** = which strategic/technical option is most viable, and what evidence/files/skills are needed to decide.
4. Build a lettered **Context Pick** with:
  - primary skill (A);
  - voice/person context (B);
  - source bank or key wiki files (C);
  - optional supporting skills or alternative voice (D, E if needed);
  - proposed output mode.
5. Or build a four-option **Decision Pick** when the user is deciding among routes, partners, stages, geographies, budgets, evidence claims, or technical strategies.
6. Always show the lettered pick for personal applications, forms, grants, technical decisions, or ambiguous tasks. End with the default route and the next action.
7. For fully unambiguous single-route tasks (weekly Aral email, email triage, transcript triage), skip the pick and proceed directly.

## Output Template

Always use the lettered pick format for personal applications, forms, grants, or any ambiguous task. Do not silently proceed:

```md
**Context Pick — [task name]**

A) Primary skill: `skills/.../SKILL.md` — what it will do for this task
B) Person context: `wiki/entities/people/...` — background, role, credentials, relationship context
C) Source bank: `wiki/principles/source-banks/...` — raw voice anchors
D) Signals: `wiki/entities/people/...-signals.md` — positioning, communication, and behavioral patterns
E) Optional layer: `skills/.../SKILL.md` or `wiki/...` — only if a secondary route could improve the answer

Loading A + B + C + D by default. Say **go** to proceed, or reply with letters to swap/add.
```

Rules for this format:

- Always show the lettered menu for personal applications, forms, grants, or multi-voice tasks — even when one route seems obvious.
- Make labels task-specific. Example: `Context Pick — TBH STEM+ Founding Member Application`, not generic `Context Pick`.
- Use **Optional layer** for secondary skills such as grant-writer, budget-architect, or institutional voice. Do not make optional layers look equally recommended.
- Only skip the menu for fully unambiguous single-route tasks (weekly Aral email, email triage, transcript triage).
- Always end with the "Loading X by default / say go to proceed" line so the user can verify without re-reading the whole pick.
- If the user replies with letters or says "go," proceed immediately — no re-asking.

For strategic or technical decisions, use this instead:

```md
**Decision Pick — [decision name]**

A) Recommended/default: [option] — why this is the current best route; evidence/files/skills to load; next action
B) Conservative option: [option] — what risk it avoids; what it gives up
C) Ambitious option: [option] — what upside it unlocks; what evidence/budget/partner bar it raises
D) Pause/research option: [option] — what missing input would change the decision

Default: [A/B/C/D] because [one sentence].
Next: I will load [files/skills] and proceed unless you choose another route.
```

Decision Pick rules:

- Use this when the user is confused because several plausible routes exist, not when they simply need a draft.
- Do not ask "which skill should I invoke?" as the main question. Choose a default route and name alternatives.
- Tie every option to evidence, source files, partner/budget constraints, and what would make the option fail.
- Do not create a new durable pattern/workflow from a Decision Pick unless the user explicitly asks and the candidate passes deduplication.
- Do not return a freeform memo, essay, or numbered analysis in place of a Decision Pick. For these prompts, the answer must visibly contain:
  - `**Decision Pick — ...**`
  - exactly four option lines `A)` through `D)`
  - one `Default:` line
  - one `Next:` line
- If the model finds itself writing sections like "Bottom line", "What this means", or "Recommended next step" without the Decision Pick block, it should stop and reformat before answering.

## Passing Example

Use this shape for the fresh-chat test prompt: `We are unsure whether to apply Stage 1 or Stage 2 for DIV with SAMS/JHU; use Cortex.`

```md
**Decision Pick — DIV Stage And Partner Route**

A) Recommended/default: Syria-first with HERA + SAMS as a Stage 2 ask — fits Cortex's current reading for adaptation, Telegram-first implementation, and powered eval in Syria; use `wiki/donors/div-fund-usaid.md` and `wiki/projects/div-syria-sams-stage2-2026.md`; fails if the team needs three deep partners or a ~500k+ budget without JHU plan.
B) Conservative option: keep the first DIV concept HERA + SAMS only and leave JHU out of formal co-applicant language for now — avoids mixing the Somalia/JHU lane with the Syria/SAMS lane; gives up the prestige/evaluation advantage until the theory of change is locked.
C) Ambitious option: pursue Stage 2 with HERA + SAMS + JHU — only viable if the proposal can state a credible causal or strong quasi-experimental design for this Syria outcome chain, with power/MDE, cost-effectiveness logic, and partner roles that justify ~500k (or rare 750k).
D) Pause/research option: do not choose stage yet — use `wiki/donors/div-fund-usaid.md` § Pre-geography decision checklist to lock primary geography, pathway, evidence maturity, partner roles, and non-goals before any partner-facing co-applicant language.

Default: A because Cortex currently treats Syria + SAMS as a new deployment context where Stage 1 is the honest default unless a Stage 2 evaluation design is already defensible.
Next: Load `wiki/donors/div-fund-usaid.md`, `wiki/projects/div-syria-sams-stage2-2026.md`, and any submitted DIV form/evaluation text, then draft a one-page internal memo locking geography, stage, pathway, partners, and non-goals.
```

This example is a format fixture, not a permanent DIV decision. If the underlying donor/project facts change, preserve the same shape and update the substance.

## Common Routes


| User intent                                                               | Primary skill                                       | Supporting context                                                                                                         |
| ------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Berktuğ personal application, bio, LinkedIn/profile, founding-member form | `skills/voice-dna/SKILL.md`                         | `wiki/entities/people/berktug.md`, `wiki/partnerships/chh.md`, `wiki/principles/source-banks/berktug-voice.md` |
| Aral/founder/movement/fellowship voice                                    | `skills/voice-dna/SKILL.md`                         | `wiki/principles/source-banks/aral-voice.md`, relevant Aral/person/project files                                           |
| Grant proposal, donor answer, LOI, concept note                           | `skills/grant-writer/SKILL.md`                      | `skills/grant-red-team-reviewer/SKILL.md`, donor/project/evidence/pattern files                                            |
| Grant budget or budget narrative                                          | `skills/budget-architect/SKILL.md`                  | master Excel if provided, budget patterns, donor/project files                                                             |
| Weekly Aral brief/email                                                   | `skills/weekly-aral-email/SKILL.md`                 | `TASKS.md`, Berktuğ voice, weekly brief pattern                                                                            |
| Manual email markdown triage                                              | `skills/email-triage/SKILL.md`                      | `raw/email/`, `_system/state/triage_email.json`, `wiki/inbox/triage/`                                                      |
| Fireflies/Granola transcript triage                                       | `skills/transcript-triage/SKILL.md`                 | transcript priority matrix, dedup protocol, `TASKS.md`                                                                     |
| Record a correction or thinking pattern                                   | `skills/collective-brain-reflection/SKILL.md`       | pattern detector, dedup protocol, promotion matrix                                                                         |
| Save facts into Cortex                                                    | `skills/knowledge-curator/SKILL.md`                 | relevant `wiki/`, `raw/`, dedup protocol                                                                                   |
| Audit legacy pattern material                                             | `wiki/concepts/workflow/pattern-migration-audit.md` | `_system/state/pattern_migration.json`, dedup protocol                                                                     |
| Strategic/technical decision with multiple viable options                 | Decision Pick mode in this skill                    | relevant donor/project/evidence files, then the domain skill such as grant-writer                                          |


## Choosing Voice

When multiple voices could apply, ask the real routing question:

- Is the audience investing in **Berktuğ as a person**?
- Is the audience investing in **Aral/founder story**?
- Is the audience evaluating **HERA as an organization/system**?
- Is the audience evaluating **a donor proposal or technical implementation**?

Then choose:

- Berktuğ personal external voice for his personal applications/forms/profiles.
- Aral voice for founder-led moral urgency and fellowship narratives.
- Berktuğ ops voice for execution, systems, implementation, and team coordination.
- Institutional/hybrid voice for UN, government, academic, technical, or formal donor contexts.

## Guardrails

- Do not read the whole vault.
- Do not create new rules/skills/patterns from a routing moment unless explicitly asked.
- Do not write files unless the user explicitly asks or the invoked skill requires approved writes.
- For the **narrow** single-route tasks listed under “Only skip” in **When To Use**, you may proceed without a pick when the user already gave the route; otherwise default + “Say **go**” still applies if universal routing requires a pick.
- For personal applications, forms, grants, or multi-voice tasks, always present the lettered context menu first so the user can cherry-pick or approve the default route (unless the user used an explicit bypass phrase in `.cursor/rules/cortex-universal-routing.mdc`).

