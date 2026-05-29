---
id: ADR-009
title: Complexity Budget
date: 2026-05-28
status: Accepted
author: AndreyVoyage
---

# ADR-009: Complexity Budget

## Context
As Voyage Framework grows, there's a risk of uncontrolled complexity:
- Too many roles
- Overlapping ADRs
- Conflicting rules
- Bloated orchestrator

We need a mechanism to limit and manage complexity.

## Decision
Implement a **Complexity Budget** system:
- Each phase has a maximum allowed complexity score
- Adding components (roles, ADRs, rules) costs points
- Must stay within budget or justify with ADR

## Complexity Scoring

| Component | Base Cost | Notes |
|-----------|-----------|-------|
| New ROLE | 10 points | +5 if cross-domain |
| New ADR | 5 points | +3 if supersedes existing |
| New RULE (Critical) | 8 points | High impact |
| New RULE (High) | 5 points | Medium impact |
| New RULE (Medium) | 2 points | Low impact |
| New RULE (Low) | 1 point | Minimal impact |
| New Integration | 15 points | External system dependency |

## Phase Budgets

| Phase | Budget | Spent | Remaining |
|-------|--------|-------|-----------|
| Phase 0 (Docs) | 50 | 48 | 2 |
| Phase 1 (Core) | 100 | 35 | 65 |
| Phase 2 (Test/Sec) | 80 | 20 | 60 |
| Phase 3 (Self-Improving) | 120 | 0 | 120 |

## Budget Management Rules
1. Cannot exceed budget without ADR-level justification
2. Deprecating a component refunds 50% of its cost
3. Quarterly budget review by ROLE-003
4. Budget overruns trigger automatic simplification sprint

## Self-Improving Engine Integration
The Complexity Budget feeds into the Self-Improving Engine:
- Tracks which components contribute most to complexity
- Suggests consolidation when budget tightens
- Identifies low-value components for deprecation

## Consequences
### Positive
- Prevents framework bloat
- Forces intentional architecture decisions
- Makes trade-offs explicit

### Negative
- Subjective scoring (requires calibration)
- May discourage useful additions
- Needs ongoing maintenance

## Related
- [ADR-006: Rule Governance](./ADR-006-rule-governance.md)
- [ADR-007: Runtime Orchestration](./ADR-007-runtime-orchestration.md)
