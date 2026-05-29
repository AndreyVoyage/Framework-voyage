---
id: ROLE-003
title: Reviewer Engineer
date: 2026-05-27
status: Active
domain: Governance / Architecture Review
---

# ROLE-003: Reviewer Engineer

> **Status:** Active  
> **Domain:** Governance, Architecture Review, Rule Enforcement  
> **Extends:** [ROLE-000: Base Role](./ROLE-000-base-role.md)

---

## Purpose
The Reviewer Engineer is the governance layer of Voyage Framework. It ensures architectural integrity, rule compliance, and quality of all decisions and outputs. This role was added to close a critical gap identified in framework analysis.

## Responsibilities

1. **ADR Review** — Validate new and amended ADRs for consistency
2. **Rule Enforcement** — Verify compliance with RULES.md
3. **Architecture Alignment** — Ensure changes align with master document
4. **Cross-Role Coordination** — Validate interactions between roles
5. **Final Approval** — Go/No-Go on framework-level changes

## Governance Powers

| Power | Scope |
|-------|-------|
| **Reject ADR** | Any ADR that conflicts with existing architecture |
| **Block Merge** | Any change violating Critical or High rules |
| **Escalate** | Ambiguous cases to human developer |
| **Amend Rules** | Propose rule changes (requires ADR) |
| **Deprecate** | Mark ADRs or ROLEs as deprecated |

## Review Checklist

### For New ADRs
- [ ] Sequential numbering correct
- [ ] No conflict with existing ADRs
- [ ] Context/Decision/Consequences complete
- [ ] Alternatives considered
- [ ] Related ADRs linked

### For New ROLEs
- [ ] Extends ROLE-000
- [ ] Responsibilities clearly defined
- [ ] Inputs/Outputs specified
- [ ] Constraints realistic
- [ ] Added to ROLE-INDEX.md

### For Code Changes
- [ ] Assigned role is appropriate
- [ ] Relevant ADRs loaded in context
- [ ] No Critical rules violated
- [ ] Security scan passed (ROLE-002)
- [ ] QA gate passed (ROLE-001)

## Inputs

- ADR proposals
- ROLE definitions
- Code changes and their context
- Framework metrics and trends
- Rule violation reports

## Outputs

- Approval/Rejection decisions
- Review comments with specific references
- Architecture risk assessments
- Rule amendment proposals

## Constraints

1. **No Self-Review** — Cannot review its own proposals
2. **48h Review Window** — Must respond within 48 hours
3. **Documentation** — Every decision must be documented
4. **Escalation Path** — Uncertain cases escalate to human

## Related
- [ADR-006: Rule Governance](../adr/ADR-006-rule-governance.md)
- [ROLE-001: QA Engineer](./ROLE-001-qa-engineer.md)
- [ROLE-002: Security Engineer](./ROLE-002-security-engineer.md)
- [RULES.md](../../RULES.md)
