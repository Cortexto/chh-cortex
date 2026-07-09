# Email landing zone — CHH Cortex

Curator-selected threads only. **Do not** bulk-export full mailboxes into git.

## Why this exists

Paul Spiegel (Jul 2026 demo): CHH needs **email context** in the same institutional memory as meetings and proposals — who was contacted, what was promised, what feedback arrived — without giving AI OAuth access to Outlook.

## Naming convention

```
raw/email/YYYY-MM-DD_<short-subject-slug>.md
```

Example: `raw/email/2026-07-09_yazdi-lsri-coordination.md`

## Frontmatter (required)

```yaml
---
source: email-paste
date: YYYY-MM-DD
participants: name1, name2
grant_slug: optional-workbench-slug
curator: who approved landing
redacted: true|false
---
```

## Workflow

1. **Select** — curator chooses grant-related or decision-bearing threads only.
2. **Redact** — remove PII/PHI and student identifiers not needed for grant context.
3. **Land** — save markdown in this folder.
4. **Triage** — `Use skills/transcript-triage/SKILL.md and triage this email`
5. **Link** — if tied to an active RFP, add a line to that package’s `REVISION-LOG.md` or `DECISION-CHART.md`.
6. **Promote** — durable facts → `wiki/` via `skills/knowledge-curator/SKILL.md` (curator approves).

## Contextual awareness

When booting a grant or answering “what did we email X about?”, assistants should read:

- This file (if matched by date, participant, or grant_slug)
- `wiki/entities/people/` for parties named
- Active `raw/proposals/<slug>/` workbench

## Future (not pilot promise)

- Curated forward to a CHH capture folder → periodic export to markdown
- Hopkins IT-reviewed export path — MoU phase only

See `CHH-ROADMAP.md` for email population workflow.
