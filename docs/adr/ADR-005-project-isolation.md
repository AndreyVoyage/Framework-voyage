---
id: ADR-005
title: Project Isolation
date: 2026-05-23
status: Accepted
author: AndreyVoyage
---

# ADR-005: Project Isolation

## Context
Voyage Framework must support multiple projects without cross-contamination:
- SkillTracer (Telegram bot + React)
- service-center (Payload CMS + Next.js)
- Future projects

## Decision
Each project gets **complete isolation** at the framework level:
- Separate PostgreSQL schema per project
- Separate ChromaDB collection per project
- Separate configuration file
- Separate AI context window

## Rationale
1. **No data leakage** — one project's secrets don't appear in another
2. **Independent evolution** — each project can have different rules/roles
3. **Clean deletion** — removing a project removes all its data

## Consequences
### Positive
- Strong security boundaries
- Easy project onboarding/offboarding
- Parallel development without interference

### Negative
- Resource overhead per project
- Cross-project learning requires explicit export/import

## Implementation
```
/projects/
  ├── skilltracer/
  │   ├── config.yaml
  │   ├── schema.sql
  │   └── chroma_collection/
  └── service-center/
      ├── config.yaml
      ├── schema.sql
      └── chroma_collection/
```

## Related
- [ADR-001: PostgreSQL Events](./ADR-001-postgresql-events.md)
- [ADR-004: Dual Location Storage](./ADR-004-dual-location.md)
