---
id: ADR-008
title: Observability and Telemetry
date: 2026-05-27
status: Accepted
author: AndreyVoyage
---

# ADR-008: Observability and Telemetry

## Context
To enable the Self-Improving Engine and debug framework behavior, we need comprehensive observability:
- What decisions were made and why
- How long operations take
- Where errors occur
- How AI output quality changes over time

## Decision
Implement **three-pillar observability**:
1. **Metrics** — quantitative data (timing, counts, rates)
2. **Logs** — structured event records
3. **Traces** — end-to-end request flow

## Technology Choices

| Pillar | Tool | Rationale |
|--------|------|-----------|
| Metrics | Prometheus + Grafana | Open source, VPS-friendly |
| Logs | PostgreSQL (structured) + Loki (optional) | Already have PostgreSQL |
| Traces | OpenTelemetry (future) | Vendor-neutral standard |

## Key Metrics

### Framework Metrics
- Rule violation rate per level
- ADR/ROLE lookup latency
- Context builder assembly time
- AI request success/failure rate

### AI Quality Metrics
- Output acceptance rate (after validation)
- Retry count per task
- Semantic similarity between AI outputs and expected results
- Time to first correct output

### Project Metrics
- Tasks completed per day
- Phase transition velocity
- Test pass rate over time
- Security scan findings trend

## Log Schema

```json
{
  "timestamp": "2026-05-28T08:56:00Z",
  "level": "INFO",
  "component": "Orchestrator",
  "event": "role_assigned",
  "task_id": "abc123",
  "role_id": "ROLE-001",
  "project": "skilltracer",
  "duration_ms": 45,
  "metadata": {}
}
```

## Consequences
### Positive
- Data-driven framework improvements
- Fast debugging of AI behavior issues
- Historical trend analysis

### Negative
- Storage growth (logs accumulate)
- Performance overhead of telemetry collection
- Need dashboards and alerting setup

## Related
- [ADR-007: Runtime Orchestration](./ADR-007-runtime-orchestration.md)
- [ADR-009: Complexity Budget](./ADR-009-complexity-budget.md)
