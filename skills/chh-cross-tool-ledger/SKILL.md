---
name: chh-cross-tool-ledger
description: Resume grant work across AI tools — read REVISION-LOG and optional REVIEW-LEDGER before drafting. Triggers include continue, cross-tool, same slug new session.
---

# CHH Cross-Tool Ledger

Use when Paul/team switches between Claude, ChatGPT, or folder-mounted assistants on the **same grant**.

## Required Reads

1. `wiki/concepts/workflow/chh-workflows-guide.md` § Cross-tool ledger
2. `raw/proposals/<slug>/REVISION-LOG.md`
3. `raw/proposals/<slug>/DECISION-CHART.md`
4. Optional: `raw/proposals/<slug>/REVIEW-LEDGER.md` if present

## Workflow

### Resume

1. User says **continue [slug]** or **I am working on [slug]**
2. Read decision chart, dossier, revision log (and review ledger if any)
3. Emit short continuity brief: decided · open · next section
4. Draft only after brief

### New session row (optional)

If user asks to log the session, append to `REVIEW-LEDGER.md`:

| Date | Tool | What changed | Open items |

Never delete prior rows.

## Guardrails

- Workbench files beat chat memory
- Do not invent decisions not in files
- Curator approves file writes
- **Git handles collisions** — ledgers are coordination records, not locks and not model telemetry
