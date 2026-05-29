---
id: ADR-007
title: Runtime Orchestration
date: 2026-05-27
status: Accepted
author: AndreyVoyage
---

# ADR-007: Runtime Orchestration

## Context
Voyage Framework needs a runtime layer that:
- Selects appropriate ROLE for each task
- Manages AI session lifecycle
- Enforces rules during execution
- Handles errors and retries

## Decision
Implement an **Orchestrator** component that sits between the developer and AI agents.

## Architecture

```
Developer Input
      │
      ▼
┌─────────────┐
│  PARSER     │ ← Parse intent, detect task type
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  CLASSIFIER │ ← Match task to ROLE(s)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  CONTEXT    │ ← Load memory, rules, relevant ADRs
│  BUILDER    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  EXECUTOR   │ ← Send to AI agent (Kimi/ChatGPT/Claude)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  VALIDATOR  │ ← ROLE-001 (QA) + ROLE-003 (Reviewer)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  OUTPUT     │
│  FORMATTER  │
└─────────────┘
```

## Components

### Parser
- Natural language intent detection
- Task type classification (code, test, review, deploy)

### Classifier
- Rule-based mapping: task type → primary ROLE
- Fallback to ROLE-000 (Base) if uncertain
- Max 2 secondary roles

### Context Builder
- Load relevant ADRs based on task domain
- Load active RULES.md sections
- Load project-specific configuration
- Inject memory from PostgreSQL + ChromaDB

### Executor
- Interface with AI agent APIs
- Handle rate limits, retries, timeouts
- Stream output for real-time feedback

### Validator
- ROLE-001: Check output quality, test coverage
- ROLE-003: Check rule compliance, architectural alignment
- Auto-reject if Critical rules violated

## Consequences
### Positive
- Consistent AI interaction pattern
- Automatic rule enforcement
- Audit trail of all decisions

### Negative
- Adds latency to AI interactions
- Requires maintenance as roles evolve
- Single point of failure (needs redundancy)

## Implementation Status
> 🟡 **Partial** — Architecture defined, basic parser/classifier implemented.

## Related
- [ADR-006: Rule Governance](./ADR-006-rule-governance.md)
- [ADR-008: Observability](./ADR-008-observability.md)
