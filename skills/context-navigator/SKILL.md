---
name: context-navigator
description: Route ambiguous CHH Cortex tasks to the right skill before drafting.
---

# CHH Context Navigator

Use when the user is unsure which skill applies, or when a request could be grant drafting, triage, or onboarding.

## Required Reads

1. `ENTRY.md`
2. `_system/AGENTS-AND-SKILLS.md`
3. `wiki/partnerships/chh.md`

## Routes

| User intent | Skill |
|-------------|-------|
| First setup | `skills/chh-onboarding/SKILL.md` |
| Grant / RFP drafting | `skills/grant-writer/SKILL.md` |
| Draft review | `skills/grant-red-team-reviewer/SKILL.md` |
| Meeting / email paste | `skills/transcript-triage/SKILL.md` |
| Wiki promotion | `skills/knowledge-curator/SKILL.md` |

Present a short menu with a default route. Wait for **go** before long drafting unless user says **skip pick**.
