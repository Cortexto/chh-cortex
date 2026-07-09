---
name: CHH Cortex Lite — Release Gate
description: Mandatory gates before GitHub invite to JHU partners
type: system
updated: 2026-07-09
version: 0.2
---

# CHH Cortex Lite — Release Gate

**Rule:** Scripts decide ship/no-ship. Model reviews (Bugbot, Claude) are advisory only.

## Gate 1 — Build + content QA (must exit 0)

```bash
python3 scripts/build_chh_lite.py \
  --source /path/to/hera-cortex/cortex \
  --output /path/to/chh-cortex
```

Fails (exit 1) when:

- Required source template missing
- Forbidden content patterns found outside allowlist
- Post-build path verification fails
- Output guard refuses rebuild (uncommitted target changes, CHH-local `raw/` content, or non-export target) — use `--force` for intentional maintainer re-sync only

## Gate 2 — Export verifier (must exit 0)

```bash
python3 scripts/verify_chh_export.py /path/to/chh-cortex
```

Fails when:

- Skill Required Reads point to missing files
- Boot chain paths in ENTRY/README/CHH-INSTALL missing
- Broken Obsidian wikilinks in exported markdown
- Forbidden content leaks (second pass on built tree)

## Gate 3 — Bugbot (optional, advisory)

Run when build/sanitization logic changed:

```
/review-bugbot
Custom: partner export; silent skips, QA never exits non-zero, strategy leak paths
```

**Do not cite "Bugbot verdict" unless Gate 3 actually ran.** Use "static gate failed" or "manual file check."

## Gate 4 — Fusion summary (human-facing)

Read Gate 1 + Gate 2 logs only. Emit Decision Pick:

| Verdict | Condition |
|---------|-----------|
| **SHIP** | Both gates exit 0 |
| **BLOCK** | Either gate exit ≠ 0 |
| **PREVIEW ONLY** | Never for partner exports |

## v0.2 product rules

1. **CHH-native thin skills** — ≤15 Required Reads, all paths exist in export
2. **Fictional example workbench** — `raw/proposals/example-chh-rfp-2026/`, not live LSRI strategy
3. **Sanitized person cards** — templates only, no HERA negotiation intel
4. **Plugin honesty** — metadata stub; onboarding does not claim full skill registration until manifest ships

## Before GitHub invite

- [ ] Gate 1 exit 0
- [ ] Gate 2 exit 0
- [ ] Manny call confirms curator + Mac + Drive assumptions (no repo required)
- [ ] User says **go invite**

## Capture

> Partner-facing lite repos: `QA PASS` = runnable-path check + content sanitization, not forbidden-token grep alone.
