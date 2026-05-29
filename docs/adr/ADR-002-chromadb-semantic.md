---
id: ADR-002
title: ChromaDB for Semantic Memory
date: 2026-05-21
status: Accepted
author: AndreyVoyage
---

# ADR-002: ChromaDB for Semantic Memory

## Context
AI sessions need context retrieval beyond simple chronological lookup. Semantic similarity search enables:
- Finding relevant past decisions
- Retrieving similar error patterns
- Building knowledge base from previous projects

## Decision
Use **ChromaDB** as the semantic/vector memory layer.

## Rationale
1. **Open source** — no vendor lock-in
2. **Local-first** — runs on VPS without external API dependencies
3. **Embedding agnostic** — supports multiple embedding models
4. **Simple API** — easy integration with Python stack

## Consequences
### Positive
- Semantic context retrieval
- Fast similarity search
- Embeddings can be tuned per project

### Negative
- Adds another data store to maintain
- Embedding model choice impacts quality
- Storage grows with project history

## Alternatives Considered
- **Pinecone** — rejected: SaaS dependency, cost concerns
- **Weaviate** — rejected: heavier resource requirements
- **PostgreSQL pgvector** — rejected: at the time, ChromaDB had better Python integration

## Related
- [ADR-001: PostgreSQL Events](./ADR-001-postgresql-events.md)
- [ADR-004: Dual Location Storage](./ADR-004-dual-location.md)
