---
id: PROMPT-PHASE2
title: Prompt: Execute Phase 2
date: 2026-05-28
status: Active
---

# PROMPT: Execute Phase 2 — Testing & Security

## Purpose
Use this prompt to guide AI through Phase 2 implementation tasks.

## Prompt Text

```
You are executing Phase 2 of Voyage Framework: Testing & Security Integration.

Current context:
- Project: {project_name}
- Phase: 2 (Testing & Security)
- Available roles: ROLE-001 (QA), ROLE-002 (Security), ROLE-003 (Reviewer)

Your task: {specific_task}

Before starting:
1. Load relevant ADRs:
   - ADR-001 (PostgreSQL)
   - ADR-006 (Rule Governance)
   - ADR-008 (Observability)
2. Load relevant ROLEs:
   - ROLE-001 (QA Engineer)
   - ROLE-002 (Security Engineer)
3. Load TEST_STRATEGY.md v2.0
4. Load TECH-001 (AppSec Stack)

Execution rules:
- Follow RULES.md Critical and High rules
- Every code change must have tests (≥80% coverage)
- Run security scan before finishing
- Update PHASE_STATUS.md when complete

Output format:
## Task: {description}
## Decisions
{why choices were made}
## Implementation
{code + tests}
## Validation
{test results, coverage report}
## Security Scan
{SAST/SCA results}
## Status Update
{PHASE_STATUS.md changes}
```

## Usage
1. Fill in `{project_name}` and `{specific_task}`
2. Attach relevant framework files
3. Execute with Kimi Code or ChatGPT

---

*Last updated: 2026-05-28*
