---
id: ADR-004
title: Dual Location Storage (PostgreSQL + ChromaDB)
date: 2026-05-22
status: Accepted
author: AndreyVoyage
---

# ADR-004: Dual Location Storage

## Context
Voyage Framework needs two types of memory:
1. **Structured** — events, logs, decisions (query by time, type, project)
2. **Semantic** — context, meaning, similarity (query by relevance, concept)

No single database optimally serves both needs.

## Decision
Implement **dual storage**:
- **PostgreSQL** for structured data
- **ChromaDB** for semantic/vector data

## Rationale
1. **Best of both worlds** — each database optimized for its use case
2. **Clear separation** — structured queries don't pollute semantic space
3. **Independent scaling** — can optimize each store separately

## Consequences
### Positive
- Optimal query performance for each data type
- Independent backup and maintenance strategies
- Can replace one store without affecting the other

### Negative
- Data consistency across two stores
- More complex backup/restore procedures
- Need synchronization logic

## Synchronization Strategy
- PostgreSQL is source of truth for events
- ChromaDB is populated asynchronously from PostgreSQL events
- Event ID serves as correlation key

## Related
- [ADR-001: PostgreSQL Events](./ADR-001-postgresql-events.md)
- [ADR-002: ChromaDB Semantic Search](./ADR-002-chromadb-semantic.md)
