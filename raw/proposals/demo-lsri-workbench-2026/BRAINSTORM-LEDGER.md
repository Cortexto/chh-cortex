# JHU LSRI Individual Award Brainstorm Ledger

## Use

Shared live board for Codex, Cursor, Claude, and future agents. Open questions, hypotheses, source checks, merge decisions.

Accepted decisions land in `DECISION-CHART.md`.

## STATE

- **Status:** active (fusion proposed 2026-07-13)
- **Top blocker:** Confirm fusion **LSRI-H005** (Fork C frame + Fork B method) with Shatha + Aral; Shatha yes/no on CHH facility recruitment for exploratory linkage aim
- **NEXT:** Shatha/Aral confirm H005 → tech team answers 4 self-report verify questions → **Yazdi role scoping call** (soft yes 2026-07-07) → narrative v2 by Jul 15
- **Hard constraints registered 2026-07-13:** no active clinic connection (linkage = exploratory only); no AMTI name; HERA back-staged; no unverified figures
- **Last touched:** 2026-07-13
- **Yazdi:** soft yes 2026-07-07 — roles TBD; see capture log

## Verify Queue

| Claim | Blocks | Owner -> next action | Closing source / close condition | Status |
|-------|--------|----------------------|-----------------------------------|--------|
| Fork B corpus size and representativeness | LSRI-H002 narrative | Berktuğ + Aral -> quantify de-identified conversation volume | HERA ops metrics or published preprint | verify |
| Yazdi co-PI availability | LSRI-Q003 | Aral + Yazdi -> role scoping when hypothesis clear | Written role agreement (student vs faculty co-PI) | **soft yes** 2026-07-07 |
| HERA subaward vs service contract | LSRI-Q004 | Shatha / JHURA | JHURA guidance | verify |
| Shatha full-time faculty eligibility | LSRI-Q001 | Shatha | ORS confirmation | verify |
| Self-report loops: response rate per template (1 vaccination / 2 pregnancy / 3 health access) | Aim 1 evidence table | Berktuğ -> ask Sara / Su-Yuen / Husam | Product/database export | verify |
| Self-report data window + denominators (users vs survey exposures — GHAIN R3 flag) | Aim 1 evidence table | Berktuğ -> tech team | Database reconciliation | verify |
| Self-report storage format (structured field vs free text) + export/de-ID path | Aim 1 feasibility wording | Berktuğ -> tech team | Tech confirmation | verify |
| Exact follow-up question wording per flow | Protocol drafting | Berktuğ -> land internal eval report PDF to `raw/evidence/` | Report methodology section | verify |
| CHH can recruit 2–3 facilities for linkage pilot | Exploratory aim vs cut | Shatha -> reconciliation call agenda | Shatha yes/no | **open — ask on call** |
| Conversation timestamps exportable in de-identified data (gates H3 interval analysis) | H3 / Aim 2 | Berktuğ -> tech team (add to 4-question ask) | Tech confirmation | verify |
| Design numbers (agreement thresholds, annotation subset n, cognitive-interview n≈20–30) | Expected-outcomes table | Shatha + analyst/biostatistician | Protocol prespecification | **PI to confirm** |

## Active Questions

| ID | Priority | Question | Why it matters | Owner | Status | Current answer | Next action | Source |
|----|----------|----------|----------------|-------|--------|----------------|-------------|--------|
| LSRI-Q001 | P1 | Which hypothesis — A, B, C (Syria/utilization), or hybrid? | Gates entire 4-page spine | Aral + Berktuğ | active | **Aral bullets landed 2026-07-08** — lean C (utilization + implementation learning); reconcile with Fork B | Merge into hypothesis brief + DECISION-CHART | `raw/capture-logs/2026-07-08-aral-lsri-hypothesis-direction-notes.md` |
| LSRI-Q006 | P1 | Roster: Aral suggested co-PI; vault lock = trainee only | Eligibility + reviewer read | Aral + Shatha | active | **Conflict** — do not paste Aral co-PI into donor text | Confirm with Shatha/JHU student rules | Aral notes 2026-07-08 |
| LSRI-Q007 | P2 | Yazdi co-PI still needed at $200–500k scale? | Team size vs multidisciplinarity gate | Aral | active | Aral leans **optional**; Yazdi **soft yes** on students/faculty roles TBD | Scoping call after hypothesis lock | Aral notes 2026-07-08 + Yazdi email 2026-07-07 |
| LSRI-Q008 | P3 | Bill Weiss on roster as faculty co-I? | CHH faculty leverage | verify | active | **Bill Weiss = Aral DrPH advisor** (corrected 2026-07-11); not Jul 2 stack | Confirm only if faculty co-I role fits | Berktuğ correction 2026-07-11 |
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
| LSRI-H005 | LSRI-Q001 | **Fusion (2026-07-13): Fork C as frame + Fork B as method.** Hypothesis: conversational data can identify why refugee women miss care, and a PI-designed measurement layer embedded in an operating service can validly measure self-reported utilization. Aim 1: governed pipeline + PI-designed self-report instrument + validation sub-study (corpus = deliverable). Aim 2: barrier discovery + pre-clinic drop-off + selection-function modeling ("invisible women" science, clinic-free by design). Aim 3: bounded CBID design cycle with pre-specified fallback barrier. Exploratory: CHH-led facility linkage pilot (pending Shatha network answer). Follow-on paragraph only: DIV/FID | Three self-report loops founder-confirmed (capture log 2026-07-13); resolves B-vs-C reconciliation; degrades gracefully if linkage fails; committee-scored strongest in red-team session | No-clinic constraint (below); numbers unverified; Aim 3 dependent on Aim 2 timing | medium-high | Berktuğ -> Shatha + Aral confirm | **proposed** |

## Agent Turns

| ID | Date | Agent | Input read | Contribution | Changes made | Needs from next agent | Links |
|----|------|-------|------------|--------------|--------------|-----------------------|-------|
| LSRI-TURN-001 | 2026-07-07 | cursor-fleet | decision doc, InfoReady capture, negotiation intel (internal) | Bootstrapped workbench; hypothesis brief + narrative skeleton | package files | Aral hypothesis; Shatha narrative ownership | `AGENT-HANDOFF.md` |
| LSRI-TURN-002 | 2026-07-08 | Cursor | Aral informal notes (Berktuğ relay) | Sanitized capture log; Fork C + utilization hypothesis; flagged roster conflicts; Yazdi optional | `raw/capture-logs/2026-07-08-aral-lsri-hypothesis-direction-notes.md`; this ledger | Reconcile with Shatha; update DECISION-CHART if accepted; do not promote Aral co-PI to donor text | capture log |
| LSRI-TURN-003 | 2026-07-08 | Cursor | Berktuğ paste Yazdi reply + Aral outbound | Landed email thread; Yazdi soft yes; co-PI not committed; student/faculty roles TBD | `raw/capture-logs/2026-07-07-yazdi-lsri-individual-award-email-thread.md`; `wiki/entities/people/youseph-yazdi.md`; this ledger | Role scoping after hypothesis lock; do not list Yazdi as committed co-PI in donor text | capture log |
| LSRI-TURN-004 | 2026-07-13 | Claude Code | Full package + DIV/FID/Ai4GH/Connect2Care cross-reads + Berktuğ product confirmation | Reviewer-simulation red-team of 4 idea candidates (scores 7/5/4/3); fusion LSRI-H005 (C-frame + B-method); no-clinic constraint surfaced; three self-report loops founder-confirmed; JHU-register Aim 1 draft language written into hypothesis brief | This ledger (H005, verify rows, claims); `raw/capture-logs/2026-07-13-lsri-self-report-loops-product-confirmation.md`; `wiki/concepts/tech/amti-capabilities.md` (self-report section); `lsri-hypothesis-brief.md` (fusion + Aim 1 patch) | Shatha + Aral confirm H005; Shatha yes/no on CHH facility recruitment; tech team answers 4 verify questions; then narrative v2 | capture log 2026-07-13 |

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
| **HERA has NO active clinic/facility connection anywhere** | confirmed | Berktuğ direct, 2026-07-13 | kill-rule for narrative | Facility-record linkage must be exploratory aim (CHH-recruited) or cut — never claimed as capability. Istanbul 2023 = *prior* collaboration only |
| Three structured self-report loops live in product (vaccination / pregnancy / health access templates) | founder-confirmed, numbers verify | Berktuğ direct, 2026-07-13; `raw/capture-logs/2026-07-13-lsri-self-report-loops-product-confirmation.md` | Aim 1 feasibility | Mechanism confirmable; response rates/windows/denominators unverified — no figures in narrative |
| AMTI name banned in LSRI narrative; HERA back-staged ("nonprofit platform partner", named once) | confirmed | Berktuğ instruction 2026-07-13 | whole narrative | Consistent with REV-006 academic register + DECISION-CHART |

## Merge Decisions

| Decision | Accepted by | Lands in | Supersedes | Source |
|----------|-------------|----------|------------|--------|
| Individual Award track only | Shatha + team, Jul 2 | `DECISION-CHART.md` | Team $10M+ bid | call transcript |
| Aral trainee not co-PI | Berktuğ + Shatha, Jul 2 | `DECISION-CHART.md` | — | call transcript |
| CHH demo NotebookLM source-pack route | Codex fleet, 2026-07-07 | `raw/drafts/jhu-chh-cortex-notebooklm-source-pack-2026-07-08.md` | generic Cortex tour | Three-lens fleet: CHH audience story, LSRI claim-risk, NotebookLM source-pack |
| AUB/FID responsibility cross-pollination: content yes, AUB org no | Claude assessment for Berktuğ, 2026-07-10; **updated same day** after Berktuğ pasted as-sent scope (`raw/drafts/fid-aub-nadine-outreach-2026-07-01.md`) | Three add-only elements landed in narrative (LSRI-REV-008): defer-versus-answer boundaries (Aim 3 requirements); GBV/acute-risk escalation pathways + structured flagged-conversation review (Ethics). Arabic lay-terminology already in Aim 1 (REV-007) | Initial same-day verdict "nothing further to add" (based on wiki summaries only) | Blocks on AUB as org stand: roster lock (Jul 2), 10% external lane occupied by HERA, Aral AUB gate ([[2026-06-25-fid-eval-partner-fork]]), lane separation (REV-004 principle). Reusable academic-partner template noted: IRB/ethics + de-identified conversation eval + terminology review + responsible-AI audit + co-authored publication |

## Parking Lot

- Extra maternal faculty (Megan Mary / TUMD) — deferred per Aral
- Research Resilience Fund — deprioritized

## Source(s)

- `wiki/concepts/workflow/cortex-interleaved-agent-brainstorming.md`
- `raw/meetings/2026-07-02_jhu-research-funding-opportunities-shatha-call-transcript.md`
