---
name: CHH Cortex Lite — Sanitization Manifest
description: Allowlist and strip rules for exporting HERA Cortex → Cortexto/chh-cortex
type: export-manifest
updated: 2026-07-09
version: 0.2
upstream: Cortexto/hera-cortex
downstream: Cortexto/chh-cortex
---

# CHH Cortex Lite — Sanitization Manifest (v0.2)

## Build + verify (mandatory)

```bash
python3 scripts/build_chh_lite.py \
  --source /path/to/hera-cortex/cortex \
  --output /path/to/chh-cortex

python3 scripts/verify_chh_export.py /path/to/chh-cortex
```

Both must exit 0 before GitHub invite. See `_system/RELEASE-GATE.md`.

## v0.2 changes

- **Templates-only export** — skills, people, partnership, example workbench from `_system/chh-cortex-lite/templates/`
- **No live LSRI strategy** — replaced by fictional `example-chh-rfp-2026/`
- **No HERA skill copy** — CHH-native thin skills with verified Required Reads
- **Failing QA** — build script exits 1 on content leaks or missing paths

## Strip (never export)

| Pattern | Reason |
|---------|--------|
| `wiki/observations/**` | Person negotiation intel |
| `_system/state/**`, `_system/HOT_CACHE.md`, `_system/live/**` | HERA internal ops |
| `raw/email/**`, `raw/fireflies/**` (full archive) | Sensitive |
| HERA-only proposals (IRUSA, AWS, DIV, UNHCR, etc.) | Not CHH joint |
| Live LSRI package internals | Use synthetic example instead |
| `rowboat_source` frontmatter | Strip on copy |

## Keep (generated from templates)

### Skills (CHH-native)

- `skills/grant-writer/SKILL.md`
- `skills/grant-red-team-reviewer/SKILL.md`
- `skills/transcript-triage/SKILL.md`
- `skills/knowledge-curator/SKILL.md`
- `skills/context-navigator/SKILL.md`
- `skills/chh-onboarding/SKILL.md`

### Wiki

- `wiki/partnerships/chh.md`
- `wiki/concepts/workflow/chh-grant-writing-process.md`
- `wiki/concepts/workflow/grant-proposal-workbench.md`
- `wiki/principles/chh-grant-voice.md`
- `wiki/entities/people/*` (sanitized templates)

### Raw

- `raw/proposals/example-chh-rfp-2026/**` (fictional)
- `raw/proposals/_template-chh-rfp/**` (empty scaffold)
- `raw/meetings/_template/README.md`

## QA enforced by scripts

- Forbidden content patterns (see `verify_chh_export.py`)
- All skill Required Reads exist in output
- Boot chain paths in ENTRY/README/CHH-INSTALL exist
- Broken `[[wikilinks]]` fail verify

## Before GitHub invite

- [ ] `build_chh_lite.py` exit 0
- [ ] `verify_chh_export.py` exit 0
- [ ] Manny call confirms curator + Mac + Drive (no repo required)
- [ ] User says **go invite**
