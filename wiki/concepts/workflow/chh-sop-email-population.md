---
name: CHH SOP — Email population (curator-selected)
description: Forward or paste grant-related threads → raw/email → triage → workbench link
type: workflow
updated: 2026-07-15
---

# SOP — Email population (curator-selected)

**Principle:** Context over volume · no PII/PHI in shared git · no Outlook OAuth

Paul's need (Jul 2026): email threads in the **same brain** as meetings and proposals. Hopkins blocks AI mailbox access — curator **chooses** what lands.

Full landing rules: `raw/email/README.md`

---

## Who does what

| Role | Job |
|------|-----|
| **Curator** | Selects threads, redacts, approves landing, promotes to wiki |
| **Staff** | Suggest threads; do not bulk-export mailboxes |
| **Manny** | Optional `.eml` batch export path (Phase 2) |

---

## Steps

### 1 — Select (curator)

Include:

- Grant coordination with partners (Yazdi, Shatha, donors)
- Reviewer / committee feedback worth remembering
- Decisions that would otherwise live in one person's inbox

Exclude:

- Full mailbox dumps
- PHI, student records, HR, clinical identifiers
- Threads with no grant or partnership bearing

### 2 — Redact

Remove or replace:

- Phone numbers, home addresses, medical details
- Internal Hopkins politics not needed for packaging
- Attachments with sensitive data — describe in prose instead

### 3 — Land

Save as:

```
raw/email/YYYY-MM-DD_<short-subject-slug>.md
```

**Frontmatter** (required):

```yaml
---
source: email-paste
date: YYYY-MM-DD
participants: name1, name2
grant_slug: optional-workbench-slug
curator: name
redacted: true|false
---
```

Paste thread below frontmatter (oldest-first or newest-first — stay consistent).

### 4 — Triage

```
Use skills/chh-email-triage/SKILL.md on this file.
```

Or `skills/transcript-triage/SKILL.md` for simple threads.

### 5 — Link to workbench

Add one line to active package:

- `REVISION-LOG.md` — if email changes draft direction
- `DECISION-CHART.md` — if email locks a route or blocker

### 6 — Promote (curator approves)

Durable facts → `wiki/` via `skills/knowledge-curator/SKILL.md` with `Source(s)` pointing to this raw file.

---

## Contextual boot example

```
I am working on demo-lsri-workbench-2026 — use any landed email about this grant.
```

---

## Phase 2 — batch `.eml` (optional)

1. Export selected threads from Outlook as `.eml`
2. Convert to markdown (manual or Manny script — not in pilot repo)
3. Same frontmatter + triage flow

---

## Not in scope (pilot)

- AI OAuth to Outlook
- Automatic forward-to-bot pipelines
- Full SharePoint mail archive sync

See `CHH-DEPLOYMENT-OPTIONS.md` Phase 3.

## Source(s)

- `raw/email/README.md`
- `CHH-ROADMAP.md` Layer 2
- `skills/chh-email-triage/SKILL.md`
