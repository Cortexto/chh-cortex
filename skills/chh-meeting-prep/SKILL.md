---
name: chh-meeting-prep
description: Generate daily meeting briefs from pasted Outlook agenda or iCal export in raw/meetings/.
---

# CHH Meeting Prep

## When to use

User pasted today's calendar into `raw/meetings/YYYY-MM-DD_daily-agenda.md` (or similar) and wants prep bullets **without Outlook OAuth**.

## Required reads

1. The landed meeting/agenda file
2. `wiki/entities/people/` for named attendees (if exist)
3. Active `raw/proposals/<slug>/` if user named a grant boot

## Steps

1. Confirm file has frontmatter (`source: calendar-paste`, `meeting_date`).
2. For each meeting in the paste: **one-line purpose** + **three prep bullets**.
3. Pull people context only from vault — **no invented history**.
4. Flag `verify` if attendee unknown or grant link unclear.
5. If grant_slug in frontmatter, suggest one line for that package's `DECISION-CHART.md`.

## Output shape

```markdown
## [Time] — [Title]
**Purpose:** …
**Prep:**
- …
- …
- …
**Vault links:** people card if exists · optional proposal slug
```

## Do not

- Promise live Outlook access
- Fabricate prior meeting outcomes
- Promote to `wiki/` without curator approval

## Related

- `wiki/concepts/workflow/chh-sop-meeting-prep.md`
- `skills/transcript-triage/SKILL.md`
