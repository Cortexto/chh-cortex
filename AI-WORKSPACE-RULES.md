---
name: CHH Cortex — AI workspace rules (canonical)
description: Host-agnostic rules for any coding agent — Cursor, Claude Code, Codex
type: system
updated: 2026-07-15
---

# CHH Cortex — AI workspace rules

**Canonical rule file.** Adapters: `CLAUDE.md` (Claude Code) · `AGENTS.md` (Codex) · `.cursor/rules/chh-cortex-pilot.mdc` (Cursor).

Humans start at `ENTRY.md` and `CHH-DECISIONS.md`.

---

## Session startup

1. `CHH-ROADMAP.md` — product frame
2. `CHH-DECISIONS.md` — which file to use; pilot locks
3. On grant work: **`I am working on [slug]`** → read that package's `README.md`, `DECISION-CHART.md`, `DONOR-DOSSIER.md`, `REVISION-LOG.md` (demo: `demo-lsri-workbench-2026`)

Emit a short continuity brief (decided · open · next) before drafting when resuming a workbench.

---

## Hard rules (every turn)

1. **No PII/PHI** in vault writes or git commits.
2. **No invented** donor criteria, deadlines, impact claims, or credentials.
3. **Curator approval** before paste-ready funder text and before promoting `raw/` → `wiki/`.
4. **External grant prose** → `skills/grant-writer/SKILL.md` then `skills/grant-red-team-reviewer/SKILL.md`.
5. **Git handles edit collisions** (pull, commit, resolve). Ledgers (`REVISION-LOG`, `REVIEW-LEDGER`, `CHH-DECISIONS`) are **coordination records** — not file locks, not model telemetry.
6. **Workbench files beat chat memory** — do not invent decisions not in files.
7. Questions and bottlenecks → GitHub Issues on this repo when email is not enough (`CHH-DECISIONS.md`).

---

## Skills index

See `_system/AGENTS-AND-SKILLS.md` and `wiki/concepts/workflow/chh-workflows-guide.md`.

---

## Host boot (if rules do not auto-load)

| Host | Auto-loads |
|------|------------|
| **Cursor** | `.cursor/rules/chh-cortex-pilot.mdc` |
| **Claude Code** | `CLAUDE.md` → this file |
| **Codex** | `AGENTS.md` → this file |
| **Other** | Paste: *Read AI-WORKSPACE-RULES.md and CHH-ROADMAP.md, then confirm the folder contract.*
