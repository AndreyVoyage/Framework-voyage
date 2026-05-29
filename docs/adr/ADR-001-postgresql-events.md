---
id: ADR-001
title: PostgreSQL Events as Primary Persistence
date: 2026-05-20
status: Accepted
author: AndreyVoyage
---

# ADR-001: PostgreSQL Events as Primary Persistence

## Context
Voyage Framework needs a reliable, structured persistence layer for:
- Event logs (AI interactions, decisions, errors)
- Project metadata
- Session history
- Audit trail

## Decision
Use **PostgreSQL** as the primary persistence layer.

## Rationale
1. **ACID compliance** — reliable transactions for critical data
2. **JSONB support** — flexible schema for evolving event structures
3. **Mature ecosystem** — extensive tooling, backups, monitoring
4. **VPS-ready** — runs on standard Linux VPS without complex setup

## Consequences
### Positive
- Reliable data integrity
- Easy backups and replication
- Rich querying capabilities

### Negative
- Requires database administration skills
- Scaling beyond single node needs planning

## Alternatives Considered
- **SQLite** — rejected: not suitable for concurrent access and VPS deployment
- **MongoDB** — rejected: adds complexity without clear benefit over PostgreSQL JSONB
- **Redis** — rejected: not durable enough for primary persistence

## Related
- [ADR-002: ChromaDB Semantic Search](./ADR-002-chromadb-semantic.md)
- [ADR-004: Dual Location Storage](./ADR-004-dual-location.md)
