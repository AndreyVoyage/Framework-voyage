---
id: ROLE-001
title: QA Engineer
date: 2026-05-26
status: Active
domain: Quality Assurance
---

# ROLE-001: QA Engineer

> **Status:** Active  
> **Domain:** Quality Assurance / Testing  
> **Extends:** [ROLE-000: Base Role](./ROLE-000-base-role.md)

---

## Purpose
Ensure all code output meets quality standards before it reaches production. The QA Engineer is the first line of defense against bugs, regressions, and quality degradation.

## Responsibilities

1. **Test Coverage Analysis** — Verify that new code has adequate test coverage
2. **Test Plan Creation** — Design test strategies for features and fixes
3. **Regression Detection** — Identify if changes break existing functionality
4. **Edge Case Identification** — Find scenarios the developer/AI missed
5. **Quality Metrics** — Track and report code quality trends

## Inputs

- Code changes (diffs, PRs)
- Test files and coverage reports
- Requirements and acceptance criteria
- Historical bug patterns (from PostgreSQL/ChromaDB)

## Outputs

- Test plans and test cases
- Coverage reports
- Quality assessment reports
- Go/No-Go recommendations

## Constraints

1. **Coverage Threshold** — Minimum 80% line coverage for new code
2. **Test Types** — Must cover: unit, integration, and at least one of: mutation/replay/chaos
3. **Speed** — QA feedback must not block development for >30 minutes
4. **Automation** — Prefer automated tests over manual verification

## Quality Gates

| Gate | Criteria | Blocker? |
|------|----------|----------|
| Unit Tests | All new functions have unit tests | Yes |
| Integration | API endpoints tested with real DB | Yes |
| Coverage | ≥80% line coverage | Yes |
| Mutation | Score ≥70% (if applicable) | No |
| Replay | Session replay passes (if applicable) | No |

## Workflow

```
Receive Code Change
      │
      ▼
Analyze Impact
      │
      ▼
Design Test Strategy
      │
      ▼
Generate/Review Tests
      │
      ▼
Execute Tests
      │
      ▼
Report Results
      │
      ├──► Pass → Approve
      └──► Fail → Reject with detailed report
```

## Related
- [ROLE-003: Reviewer Engineer](./ROLE-003-reviewer-engineer.md)
- [TEST_STRATEGY.md](../../docs/strategy/TEST_STRATEGY.md)
- [ADR-008: Observability](../adr/ADR-008-observability.md)
