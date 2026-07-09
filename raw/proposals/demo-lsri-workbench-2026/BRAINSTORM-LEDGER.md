# JHU LSRI Individual Award Brainstorm Ledger

## Use

Shared live board for Codex, Cursor, Claude, and future agents. Open questions, hypotheses, source checks, merge decisions.

Accepted decisions land in `DECISION-CHART.md`.

## STATE

- **Status:** active (demo-driven unpark 2026-07-07)
- **Top blocker:** Hypothesis pivot — Aral direction notes 2026-07-08 (Syria mapping + utilization eval) vs Jul 2 Fork B; roster conflicts (Aral co-PI suggestion vs trainee lock)
- **NEXT:** Reconcile Aral notes with Shatha → update DECISION-CHART if accepted → **Yazdi role scoping call** (soft yes 2026-07-07) → narrative v1 by Jul 15
- **Last touched:** 2026-07-08
- **Yazdi:** soft yes 2026-07-07 — roles TBD; see capture log

## Verify Queue

| Claim | Blocks | Owner -> next action | Closing source / close condition | Status |
|-------|--------|----------------------|-----------------------------------|--------|
| Fork B corpus size and representativeness | LSRI-H002 narrative | Berktuğ + Aral -> quantify de-identified conversation volume | HERA ops metrics or published preprint | verify |
| Yazdi co-PI availability | LSRI-Q003 | Aral + Yazdi -> role scoping when hypothesis clear | Written role agreement (student vs faculty co-PI) | **soft yes** 2026-07-07 |
| HERA subaward vs service contract | LSRI-Q004 | Shatha / JHURA | JHURA guidance | verify |
| Shatha full-time faculty eligibility | LSRI-Q001 | Shatha | ORS confirmation | verify |

## Active Questions

| ID | Priority | Question | Why it matters | Owner | Status | Current answer | Next action | Source |
|----|----------|----------|----------------|-------|--------|----------------|-------------|--------|
| LSRI-Q001 | P1 | Which hypothesis — A, B, C (Syria/utilization), or hybrid? | Gates entire 4-page spine | Aral + Berktuğ | active | **Aral bullets landed 2026-07-08** — lean C (utilization + implementation learning); reconcile with Fork B | Merge into hypothesis brief + DECISION-CHART | `raw/capture-logs/2026-07-08-aral-lsri-hypothesis-direction-notes.md` |
| LSRI-Q006 | P1 | Roster: Aral suggested co-PI; vault lock = trainee only | Eligibility + reviewer read | Aral + Shatha | active | **Conflict** — do not paste Aral co-PI into donor text | Confirm with Shatha/JHU student rules | Aral notes 2026-07-08 |
| LSRI-Q007 | P2 | Yazdi co-PI still needed at $200–500k scale? | Team size vs multidisciplinarity gate | Aral | active | Aral leans **optional**; Yazdi **soft yes** on students/faculty roles TBD | Scoping call after hypothesis lock | Aral notes 2026-07-08 + Yazdi email 2026-07-07 |
| LSRI-Q008 | P3 | Paul Weiss on roster? | CHH faculty leverage | verify | active | Mentioned by Aral; not in Jul 2 stack | Confirm only if faculty co-I role fits | Aral notes 2026-07-08 |
| LSRI-Q002 | P1 | What design fits Individual Award — pilot, observational, mixed methods, RCT? | Feasibility section | Shatha + Aral | active | RCT **not required** by program | Sketch in narrative skeleton | opportunity wiki |
| LSRI-Q003 | P2 | Yazdi committed as co-PI? | Team capability section | Aral | active | **Soft yes 2026-07-07** — interested; roles (student vs faculty) TBD when plan clear | Role scoping call + one-pager | `raw/capture-logs/2026-07-07-yazdi-lsri-individual-award-email-thread.md` |
| LSRI-Q004 | P2 | HERA funding line — in-kind vs ≤10% subaward? | Budget justification | Shatha | active | `verify` | Ask Shatha / JHURA | opportunity wiki |
| LSRI-Q005 | P2 | DIV/Syria prior reviews attachable? | Strengthens approach | Berktuğ | active | `verify` | Ask Shatha | opportunity wiki |

## Hypotheses

| ID | Question ID | Hypothesis | Evidence for | Evidence against / risk | Confidence | Owner | Status |
|----|-------------|------------|--------------|-------------------------|------------|-------|--------|
| LSRI-H001 | LSRI-Q001 | **Fork A:** Maternal/newborn AI product innovation inside HERA | Shatha maternal bridge; product lane familiar | Weak novelty vs current ops | medium | Aral | active |
| LSRI-H002 | LSRI-Q001 | **Fork B:** Refugee WhatsApp conversations as novel humanitarian data collection vs Kobo; refugee gap vs Nature chatbot-health lit | Aral emphasis Jul 2; Shatha novelty gate | IRB/ethics; corpus claims need source | medium | Aral | active |
| LSRI-H004 | LSRI-Q001 | **Fork C (Aral 2026-07-08):** Syria health-system mapping + LLM-mediated intelligence; test whether AI digital tools increase utilization of general/public health services among refugee/returnee populations; rapid-cycle implementation learning | Proportionate to Individual Award; CHH evidence leadership; mobile-population framing | Syria access/IRB; must not duplicate product pitch only; reconcile with Fork B | medium-high | Aral | **new lean** |
| LSRI-H003 | LSRI-Q002 | Mixed-methods: conversational analytics + bounded health-outcome linkage | Fits eval science at CHH | Must not sound tooling-only | verify | Shatha | active |

## Agent Turns

| ID | Date | Agent | Input read | Contribution | Changes made | Needs from next agent | Links |
|----|------|-------|------------|--------------|--------------|-----------------------|-------|
| LSRI-TURN-001 | 2026-07-07 | cursor-fleet | decision doc, InfoReady capture, negotiation intel (internal) | Bootstrapped workbench; hypothesis brief + narrative skeleton | package files | Aral hypothesis; Shatha narrative ownership | `AGENT-HANDOFF.md` |
| LSRI-TURN-002 | 2026-07-08 | Cursor | Aral informal notes (Berktuğ relay) | Sanitized capture log; Fork C + utilization hypothesis; flagged roster conflicts; Yazdi optional | `raw/capture-logs/2026-07-08-aral-lsri-hypothesis-direction-notes.md`; this ledger | Reconcile with Shatha; update DECISION-CHART if accepted; do not promote Aral co-PI to donor text | capture log |
| LSRI-TURN-003 | 2026-07-08 | Cursor | Berktuğ paste Yazdi reply + Aral outbound | Landed email thread; Yazdi soft yes; co-PI not committed; student/faculty roles TBD | `raw/capture-logs/2026-07-07-yazdi-lsri-individual-award-email-thread.md`; `wiki/entities/people/youseph-yazdi.md`; this ledger | Role scoping after hypothesis lock; do not list Yazdi as committed co-PI in donor text | capture log |

## Peer Comment Loop

| Round | Date | Trigger | Primary agent | Peer agent | Question IDs | Proposal under review | Peer verdict | Synthesis / decision | Status |
|-------|------|---------|---------------|------------|--------------|-----------------------|--------------|----------------------|--------|
| — | — | — | — | — | — | — | — | — | — |
| 1 | 2026-07-07 | go fleet + co comment | Codex | Codex fleet lenses | LSRI-Q001, LSRI-Q003, LSRI-Q004 | CHH demo and NotebookLM upload pack | accept with guardrails | Use LSRI as live Cortex proof object; present Fork B only as demo lean; keep Yazdi, corpus metrics, literature gap, and budget mechanism as `verify`; produce internal NotebookLM source pack, not external donor prose | commented |
| 2 | 2026-07-08 | go comment - cross-model presentation | Codex | Cursor + Claude + Codex peers | LSRI-Q001, LSRI-Q003, LSRI-Q004 | JHU CHH Cortex opening and peer model workflow | accept with peer model framing | Use the presentation itself to demonstrate the workflow: Codex, Cursor, and Claude are peers contributing to one source-governed Cortex brain | commented |
| 2 | 2026-07-08 01:12 CEST | go comment - scope note (Claude) | Codex | Claude | — | presentation coordination | escalate to own board | Presentation/demo is a separate project from the LSRI proposal (Berktuğ, 2026-07-08). Round 2 and all further demo coordination migrated to `raw/drafts/jhu-chh-demo-BRAINSTORM-LEDGER.md`. This ledger keeps LSRI proposal scope only | migrated |

## Claim Ledger

| Claim | Status | Source | Used in | Notes |
|-------|--------|--------|---------|-------|
| ≤10% subaward cap | confirmed | InfoReady capture | budget section | At $300k → ≤$30k HERA |
| Shatha lead PI | confirmed | Jul 2 call | team section | |
| Thousands of refugee conversations | verify | Aral Jul 2 call | Fork B | needs ops count |
| Nature chatbot papers exist; refugee-specific gap | verify | Aral Jul 2 call | Fork B novelty | literature check |
| Yazdi interested in LSRI CBID collaboration | soft yes | Yazdi email 2026-07-07 | team section | co-PI **not** committed; roles TBD |

## Merge Decisions

| Decision | Accepted by | Lands in | Supersedes | Source |
|----------|-------------|----------|------------|--------|
| Individual Award track only | Shatha + team, Jul 2 | `DECISION-CHART.md` | Team $10M+ bid | call transcript |
| Aral trainee not co-PI | Berktuğ + Shatha, Jul 2 | `DECISION-CHART.md` | — | call transcript |
| CHH demo NotebookLM source-pack route | Codex fleet, 2026-07-07 | `raw/drafts/jhu-chh-cortex-notebooklm-source-pack-2026-07-08.md` | generic Cortex tour | Three-lens fleet: CHH audience story, LSRI claim-risk, NotebookLM source-pack |

## Parking Lot

- Extra maternal faculty (Megan Mary / TUMD) — deferred per Aral
- Research Resilience Fund — deprioritized

## Source(s)

- `wiki/concepts/workflow/cortex-interleaved-agent-brainstorming.md`
- `raw/meetings/2026-07-02_jhu-research-funding-opportunities-shatha-call-transcript.md`
