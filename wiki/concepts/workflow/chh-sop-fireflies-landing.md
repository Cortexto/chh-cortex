---
name: CHH SOP — Fireflies landing
description: Export Fireflies transcript → raw → triage → link to grant workbench
type: workflow
updated: 2026-07-15
---

# SOP — Fireflies → vault

**Cadence:** Weekly (or within 48h of grant-related calls)  
**Owner:** Curator or Manny (assign on Phase 0 call)

Fireflies cannot auto-feed CHH Cortex in pilot v1 without Hopkins security review. **Manual export** matches how HERA lands transcripts today.

---

## Steps

### 1 — Select meetings

Land only:

- Grant coordination calls
- Donor / partner discussions tied to an active workbench
- Internal decisions that should survive staff turnover

Skip: routine 1:1s with no grant bearing unless curator flags.

### 2 — Export from Fireflies

1. Open meeting in Fireflies
2. Export as **Markdown** or **plain text** (prefer markdown)
3. Redact PHI, student IDs, or negotiation details not needed in shared git

### 3 — Save in vault

**Preferred path:**

```
raw/meetings/YYYY-MM-DD_<topic-slug>.md
```

**Alternative** (if CHH standardizes on a fireflies subfolder):

```
raw/fireflies/<fireflies-id>_<topic-slug>.md
```

**Frontmatter:**

```yaml
---
source: fireflies-export
meeting_date: YYYY-MM-DD
participants: name1, name2
grant_slug: optional-workbench-slug
curator: who-approved-landing
redacted: true|false
---
```

### 4 — Triage

```
Use skills/transcript-triage/SKILL.md and triage this meeting.
```

**If the assistant cannot find a skill or file:** confirm `chh-cortex/` is open as the workspace/project root, then paste the file path directly.

Classify: task · decision · project-fact · contact-intel · background · noise.

### 5 — Link to workbench

If `grant_slug` is set, add to that package:

- `DECISION-CHART.md` — new lock or blocker
- `REVISION-LOG.md` — if feedback changes draft direction
- Open questions board in the workbench package (if your team uses one)

### 6 — Promote (curator only)

Durable facts → `wiki/entities/people/` or `wiki/partnerships/` via `skills/knowledge-curator/SKILL.md`.

---

## Contextual boot example

```
I am working on my-grant-2026 — incorporate Fireflies notes from raw/meetings/2026-07-10_partner-call.md.
```

---

## Phase 3 (not pilot promise)

Fireflies API → automated landing under CHH IT security review. Do not configure until approved.

## Source(s)

- `CHH-ROADMAP.md` Layer 1
- HERA pattern: `raw/fireflies/` + transcript-triage
