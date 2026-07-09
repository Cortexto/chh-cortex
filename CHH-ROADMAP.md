---
name: CHH Cortex — Roadmap & guide
description: Start here for pain points, what is included, raw vs wiki, and phased rollout
type: guide
updated: 2026-07-09
---

# CHH Cortex — Roadmap & guide

**Read this first** if you are Paul, William, Manny, or any CHH staff exploring the pilot. Technical install steps live in `_system/CHH-INSTALL.md`.

---

## What this is

CHH Cortex is a **shared folder of markdown files** — grant workbenches, meeting notes, selected emails, people context — that your team and an approved AI assistant read together every session. It is **not** a chatbot with hidden memory. When someone works on an RFP, the system can already know prior decisions and linked context because that knowledge lives in files you control.

---

## Raw vs wiki — the two layers

| | **`raw/`** | **`wiki/`** |
|---|-----------|-------------|
| **Plain English** | **Inbox & working files** — everything as it arrived | **Approved facts** — what the center trusts as current truth |
| **Examples** | Email paste, meeting transcript, RFP PDF notes, draft sections | People cards, partnership rules, reviewer lessons |
| **Who writes** | Anyone can land files; curator selects what enters | **Curator approves** promotions from raw |
| **Rule** | Append-only — do not silently edit source files | Every fact needs a **Source(s)** line pointing to raw |
| **Stale info** | Old files stay for audit trail | Curator **updates or supersedes** wiki when facts change |

**Typical flow:** land in `raw/` → triage skill → curator approves → promote to `wiki/` → next grant boot reads both.

See `CORTEX.md` for folder guardrails and `wiki/concepts/workflow/chh-workflows-guide.md` for step-by-step workflows.

---

## What hurts today → what Cortex does

| What you feel | Why it is hard | What we do **now** (pilot) | What comes **later** (with IT / MoU) |
|---------------|----------------|----------------------------|--------------------------------------|
| **Calendar prep takes forever** — exporting Outlook for AI | Hopkins blocks AI from reading Outlook directly | Paste your day or week (iCal or agenda text) into `raw/meetings/` | Templated meeting brief from pasted calendar only — still no OAuth until IT approves |
| **Email context disappears** — who did we email? | Same IT block on full mailbox access | Curator picks important threads → `raw/email/` → triage | Forward folder or weekly export → markdown (human step) |
| **Forgotten meeting decisions** | No shared searchable memory | Searchable files + grant boot by folder name | Links between meetings, grants, and people cards |
| **Too much time on proposals** | Drafts scattered, no reuse | One folder per RFP + review before paste | Center boilerplate blocks + reviewer lessons library |
| **Many departments, unclear who is involved** | Siloed inboxes | People cards + triage from meetings/emails | “Who touched this funder?” from promoted wiki facts |
| **Claude and ChatGPT don’t share memory** | Different tools, no ledger | **One git or Drive folder** for the center | Same |
| **SharePoint / Dropbox not AI-readable** | File walls | Curator copies approved files into `raw/` | Scheduled sync of approved proposal folders only |
| **Hopkins GPT forgets after 30 days** | Session-bound cloud | **Files outlive any AI product** | Same |

**Pilot priority:** grant packaging first. Email and meeting layers **support grants**, not personal calendar automation.

---

## Included in this repo (use today)

| Capability | Where |
|------------|--------|
| Grant workbench (one folder per RFP) | `raw/proposals/` |
| **Demo walkthrough** — real JHU grant *shape*, sanitized | `raw/proposals/demo-lsri-workbench-2026/` |
| Red-team before paste | `skills/grant-red-team-reviewer/SKILL.md` |
| Email landing + triage | `raw/email/README.md`, `skills/chh-email-triage/SKILL.md` |
| Meeting / note triage | `skills/transcript-triage/SKILL.md` |
| Wiki promotion (approval-gated) | `skills/knowledge-curator/SKILL.md` |
| Workflow guide (portal gate, donor lens, cross-tool ledger) | `wiki/concepts/workflow/chh-workflows-guide.md` |
| People & CHH pilot rules | `wiki/entities/people/`, `wiki/partnerships/chh.md` |

## Not in this repo (HERA maintains separately)

- Background automation bots, live email/Fireflies intake
- Full internal donor pipeline for non-CHH funders
- Usage-learning and person-analytics loops (HERA-side only)
- Maintainer build tools — **you do not need another GitHub repo**

Pattern updates arrive when HERA re-syncs **this** repo (`Cortexto/chh-cortex`) after your curator approves.

---

## Try the demo (5 minutes)

1. Open this folder in your AI tool.
2. Say: **`I am working on demo-lsri-workbench-2026`**
3. Read `raw/proposals/demo-lsri-workbench-2026/HOW-TO-USE.md` — it shows decision chart, donor lens, revision log, and routes **without** being a live submission.

Then copy `raw/proposals/_template-chh-rfp/` for your real RFP.

---

## Roadmap phases

### Phase 1 — Now

- Grant workbench + LSRI **demo** walkthrough
- Manual meeting + email population
- Triage, curator, red-team skills
- Folder or git install

### Phase 2 — After Manny call

- Dedicated CHH Mac or Drive workflow
- First **live** grant workbenches
- Weekly curator rhythm; email capture SOP
- Seed reviewer lessons from revision cycles

### Phase 3 — MoU + IT

- CHH canonical blocks (IRB, methods)
- Hopkins-reviewed email export path (if available)
- Documented quality feedback cycle

### Phase 4 — Later (not dated)

- Cross-grant search
- Richer email ↔ meeting ↔ grant links (**curator facts only** — no automated profiling of staff)

**Guardrail:** no person-observation mining or negotiation-intel pages in the shared vault.

---

## Support

Berktuğ Kubuk — berktug@heradigitalhealth.org (HERA Digital Health, Cortex patterns for CHH)
