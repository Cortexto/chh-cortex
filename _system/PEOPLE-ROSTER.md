---
name: CHH people roster — lite export
description: Allowlist of JHU/CHH person cards for chh-cortex sanitized repo export.
type: export-manifest
updated: 2026-07-09
---

# CHH people roster — lite export allowlist

Curated from `wiki/entities/people/` + contacts index. **Strip rules:** remove Berktuğ PhD committee angles, internal negotiation notes, HERA-only strategy from Shatha card.

## Full cards (export sanitized)

| Slug | Source | CHH-facing role |
|------|--------|-----------------|
| `paul-spiegel.md` | `wiki/entities/people/paul-spiegel.md` | CHH Director; pilot sponsor |
| `william-weiss.md` | `wiki/entities/people/william-weiss.md` | International Health; HIS |
| `chaeeun-kim.md` | `wiki/entities/people/chaeeun-kim.md` | Technical rollout owner |
| `shatha-elnakib.md` | `wiki/entities/people/shatha-elnakib.md` | Senior researcher; LSRI PI — **strip** PhD/RWJF/internal gates |
| `sheri-maria-morgan.md` | `wiki/entities/people/sheri-maria-morgan.md` | PM; Connect2Care |
| `youseph-yazdi.md` | `wiki/entities/people/youseph-yazdi.md` | CBID; LSRI co-I lane — **strip** HERA outreach verbatim |
| `hannah-tappis.md` | `wiki/entities/people/hannah-tappis.md` | Research/eval |
| `geeta-nanda.md` | `wiki/entities/people/geeta-nanda.md` | Affiliate researcher |

## Thin contacts (promote minimal stub in lite repo)

| Name | Lite stub content |
|------|-------------------|
| Makieba Duff | Scheduling coordinator, JHMI — pbspiegel@jhu.edu thread |
| Cherry | Research Associate, CHH — anthropology + global health |

## Exclude from lite export

- All `wiki/observations/*`
- HERA core team cards (aral, berktug, sara-floijer, etc.) except brief HERA org stub in partnerships
- Person negotiation / "gates" / "negotiation style" observations

## Source(s)

- `wiki/entities/people/00-contacts-index.md`
- Plan: CHH Cortex Lite — jhu-people-roster todo
