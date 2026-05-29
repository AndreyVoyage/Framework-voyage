---
id: TEST-STRATEGY
title: Voyage Framework Testing Strategy
date: 2026-05-28
status: Active
version: "2.0"
---

# TEST_STRATEGY.md — Complete Testing Strategy v2.0

> **Supersedes:** v1.0 (initial version)  
> **Status:** Active  
> **Owner:** ROLE-001 (QA Engineer)

---

## 1. Testing Pyramid (Voyage Extended)

```
        ┌─────────────┐
        │  AI Eval    │  ← Evaluate AI output quality
        │  (New)      │
        ├─────────────┤
        │  E2E Tests  │  ← End-to-end user flows
        ├─────────────┤
        │  Chaos Tests│  ← Resilience under failure
        ├─────────────┤
        │  Replay Tests│  ← Record & replay sessions
        ├─────────────┤
        │  Mutation   │  ← Fault injection, robustness
        │  Tests      │
        ├─────────────┤
        │  Integration│  ← API, DB, external services
        ├─────────────┤
        │  Unit Tests │  ← Functions, classes, modules
        └─────────────┘
```

---

## 2. Test Types

### 2.1 Unit Tests
**Purpose:** Verify individual functions, classes, and modules in isolation.

**Tools:**
- Python: `pytest`, `unittest`
- TypeScript/JavaScript: `Jest`, `Vitest`

**Coverage Requirement:** ≥80% line coverage for new code

**Gate:** Blocker — must pass before merge

---

### 2.2 Integration Tests
**Purpose:** Verify interactions between components (API + DB, frontend + backend).

**Tools:**
- API: `pytest` + `httpx` / `supertest`
- DB: Testcontainers (PostgreSQL), SQLite in-memory
- E2E: `Playwright`, `Cypress`

**Scope:**
- API endpoint testing with real database
- Service-to-service communication
- External API mocking (WireMock, VCR.py)

**Gate:** Blocker — must pass before merge

---

### 2.3 Mutation Testing ⭐ NEW
**Purpose:** Verify test suite robustness by introducing artificial faults.

**Concept:**
- Modify source code slightly (e.g., change `+` to `-`)
- Check if tests catch the mutation
- High mutation score = strong test suite

**Tools:**
- Python: `mutmut`
- JavaScript: `Stryker`

**Threshold:** ≥70% mutation score

**Gate:** Non-blocker — report only, target for improvement

**Example:**
```python
# Original
def add(a, b):
    return a + b

# Mutant (should be caught by tests)
def add(a, b):
    return a - b  # mutmut changes + to -
```

---

### 2.4 Replay Testing ⭐ NEW
**Purpose:** Record real user/AI sessions and replay them to detect regressions.

**Concept:**
- Record: Capture all inputs, outputs, and state changes during a session
- Store: Save session recording to PostgreSQL
- Replay: Re-execute the same sequence of operations
- Compare: Verify outputs match (or improve)

**Tools:**
- Custom implementation using PostgreSQL event log
- VCR.py for HTTP interactions

**Use Cases:**
- Regression testing of AI agent behavior
- Reproducing complex bugs
- Benchmarking AI output quality over time

**Gate:** Non-blocker — report only

---

### 2.5 Chaos Testing ⭐ NEW
**Purpose:** Verify system resilience under failure conditions.

**Concept:**
- Introduce controlled failures (network latency, DB downtime, memory pressure)
- Verify graceful degradation
- Ensure no data loss

**Tools:**
- `chaos-monkey` (Netflix)
- `toxiproxy` for network chaos
- Custom scripts for resource exhaustion

**Scenarios:**
- PostgreSQL connection drop → retry with backoff
- ChromaDB unavailable → fallback to PostgreSQL only
- AI API rate limit → queue and retry
- Memory exhaustion → graceful shutdown with state save

**Gate:** Non-blocker — run weekly in staging

---

### 2.6 End-to-End (E2E) Tests
**Purpose:** Verify complete user workflows.

**Tools:**
- Web: `Playwright` (preferred), `Cypress`
- Mobile: `Appium` (future)
- API: `Postman` collections + Newman

**Scope:**
- Critical user journeys (login → action → logout)
- AI-assisted workflows (prompt → output → validation)
- Cross-browser testing (Chrome, Firefox, Safari)

**Gate:** Blocker for release, non-blocker for merge

---

### 2.7 AI Output Evaluation ⭐ NEW
**Purpose:** Systematically evaluate AI-generated code quality.

**Metrics:**
- **Correctness:** Does the code compile/run?
- **Completeness:** Does it solve the stated problem?
- **Style:** Does it follow project conventions?
- **Security:** No obvious vulnerabilities?
- **Performance:** Reasonable time/space complexity?

**Evaluation Methods:**
1. **Static Analysis:** Lint, type check, complexity metrics
2. **Execution:** Run generated code in sandbox
3. **Comparison:** Diff against human-written equivalent
4. **Regression:** Compare with previous AI outputs for same task

**Tools:**
- `pylint`, `mypy`, `eslint` for static analysis
- Docker sandbox for execution
- Custom scoring rubric (1–5 per metric)

**Gate:** Non-blocker — feeds into Self-Improving Engine

---

## 3. CI Quality Gates

### 3.1 Pre-Merge Gates (must pass)

| Gate | Tool | Threshold | Blocker |
|------|------|-----------|---------|
| Unit Tests | pytest/Jest | 100% pass | ✅ Yes |
| Coverage | coverage.py | ≥80% | ✅ Yes |
| Lint | flake8/eslint | 0 errors | ✅ Yes |
| Type Check | mypy/tsc | 0 errors | ✅ Yes |
| Secrets Scan | Gitleaks | 0 findings | ✅ Yes |
| SAST | Semgrep | 0 Critical/High | ✅ Yes |

### 3.2 Post-Merge Gates (run automatically)

| Gate | Tool | Frequency | Blocker |
|------|------|-----------|---------|
| Integration Tests | pytest + Testcontainers | Every merge | ✅ Yes |
| SCA | Snyk | Daily | No (report) |
| Mutation Tests | mutmut | Weekly | No (report) |
| E2E Tests | Playwright | Every release | ✅ Yes |
| Chaos Tests | toxiproxy | Weekly staging | No (report) |
| AI Eval | Custom sandbox | Every AI output | No (metrics) |

### 3.3 Release Gates (must pass before deploy)

| Gate | Verification | Blocker |
|------|-------------|---------|
| All pre-merge gates | Re-run on release branch | ✅ Yes |
| E2E on staging | Full user journey | ✅ Yes |
| Performance baseline | No regression >10% | ✅ Yes |
| Security review | ROLE-002 sign-off | ✅ Yes |
| QA sign-off | ROLE-001 sign-off | ✅ Yes |

---

## 4. Test Data Management

### 4.1 Fixtures
- Use `factory_boy` (Python) or `faker` for test data
- Seed data in `tests/fixtures/`
- Never use production data in tests

### 4.2 Database
- Each test gets fresh schema (use transactions or Testcontainers)
- Reset state between tests
- Use `pytest-postgresql` or Docker Compose for integration tests

### 4.3 Mocking
- External APIs: `responses` (Python), `nock` (JS)
- AI APIs: Record real responses, replay in tests
- File system: `tmp_path` fixture, `pyfakefs`

---

## 5. Test Documentation

### 5.1 Test Naming
```
test_{component}_{scenario}_{expected_result}

Examples:
- test_orchestrator_assigns_role_for_code_task
- test_postgresql_persists_event_with_valid_json
- test_chromadb_retrieves_semantically_similar_context
```

### 5.2 Test Comments
- Every test must explain *why*, not just *what*
- Reference ADRs or requirements when applicable

---

## 6. Metrics and Reporting

### 6.1 Dashboard Metrics
- Test pass rate (trend over time)
- Coverage percentage (by module)
- Mutation score (by component)
- Mean time to detect regression
- AI output quality score (average)

### 6.2 Alerts
- Coverage drops below 80% → Slack/email alert
- Test failure on main branch → immediate alert
- Security scan finding → ROLE-002 alert

---

## 7. Related Documents

- [ROLE-001: QA Engineer](../roles/ROLE-001-qa-engineer.md)
- [ROLE-002: Security Engineer](../roles/ROLE-002-security-engineer.md)
- [TECH-001: AppSec Stack](../infrastructure/TECH-001-appsec-stack.md)
- [ADR-008: Observability](../adr/ADR-008-observability.md)

---

*Last updated: 2026-05-28*  
*Next review: 2026-06-28*
