---
name: CHH SOP — Meeting prep (manual calendar)
description: Paste Outlook iCal or agenda → raw/meetings → brief without OAuth
type: workflow
updated: 2026-07-15
---

# SOP — Meeting prep (no Outlook OAuth)

**Time:** ~2 minutes per day  
**Owner:** Paul or designated staff  
**When:** Start of day or before heavy meeting blocks

Hopkins blocks AI from reading Outlook directly. This SOP replaces the hassle with a **repeatable file-first step** the vault can use all day.

---

## Steps

### 1 — Export from Outlook (Mac)

**Option A — iCal (day or week)**

1. Outlook → Calendar → select day or week view
2. File → Export (or drag events) → save as `.ics` **or** copy agenda text

**Option B — Copy agenda text**

1. Select today's events in calendar list view
2. Copy visible titles, times, attendees, locations

### 2 — Land in vault

Save as:

```
raw/meetings/YYYY-MM-DD_daily-agenda.md
```

**Frontmatter:**

```yaml
---
source: calendar-paste
meeting_date: YYYY-MM-DD
participants: optional-comma-list
curator: your-name
---
```

Paste iCal export or copied agenda under the frontmatter.

### 3 — Generate brief (AI assistant)

Boot phrase (paste into your AI tool with `chh-cortex/` as workspace root):

```
Read raw/meetings/YYYY-MM-DD_daily-agenda.md and wiki/entities/people/ for attendees.
Produce a one-line purpose + three prep bullets per meeting. No invented context.
```

**If the assistant cannot find a file:** confirm `chh-cortex/` is open as the workspace/project root, then paste the file path directly.

**Output shape (per meeting):**

```markdown
## [Time] — [Title]
**Purpose:** …
**Prep:**
- …
- …
- …
**Vault links:** people card if exists · optional proposal slug
```

**Rules:** pull people context only from the vault; flag `verify` if attendee unknown; do not promise live Outlook access; do not promote to `wiki/` without curator approval.

### 4 — Triage (optional, weekly)

```
Use skills/transcript-triage/SKILL.md and triage this meeting file.
```

Promote durable facts to `wiki/` via curator only.

---

## Link to grants

If a meeting ties to an active RFP, add one line to that package's `DECISION-CHART.md` or `REVISION-LOG.md`:

> Meeting YYYY-MM-DD: [decision or action] — see `raw/meetings/...`

---

## Optional workaround (CHH decision only)

**Gmail shadow calendar:** invite a Gmail address to every Outlook event so Google Calendar becomes extractable. Paul found double-calendar management burdensome on Jul 8 — try only if CHH commits to a one-week test.

---

## Not in scope (pilot)

- Live Outlook OAuth
- Automatic nightly calendar pull

See `CHH-DEPLOYMENT-OPTIONS.md` Phase 3 for IT petition track.

## Source(s)

- `CHH-ROADMAP.md` Layer 1
- Jul 8 demo transcript — Paul iCal export pain
