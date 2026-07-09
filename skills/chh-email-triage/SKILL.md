---
name: chh-email-triage
description: Triage curator-selected email files in raw/email/ — classify, propose tasks and wiki updates, link to grant workbenches. No mailbox OAuth.
---

# CHH Email Triage

Use when processing **landed** markdown in `raw/email/`. Vault-only — no Gmail actions.

## Required Reads

1. `raw/email/README.md`
2. `wiki/concepts/workflow/chh-workflows-guide.md` § Triage matrix
3. `wiki/partnerships/chh.md`
4. `TASKS.md` before proposing tasks

## Workflow

1. Read the email file; do not modify the source
2. Classify primary bucket:
   - `grant_or_partner_critical`
   - `action_required`
   - `needs_reply`
   - `low_priority_info`
   - `spam_or_promo`
3. Extract units: task, decision, project-fact, contact-intel, background, noise, verify
4. Propose `TASKS.md` updates — **curator approves before write**
5. If `grant_slug` in frontmatter, note link in that package’s `REVISION-LOG.md`
6. Propose wiki promotions with `Source(s)` — no PII/PHI

## Guardrails

- Curator-selected threads only
- No person-observation or negotiation-intel wiki pages
- Mark uncertainty `verify`

## Output

Triage summary in chat: buckets, task candidates, wiki candidates, workbench links.
