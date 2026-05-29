---
id: ADR-006
title: Rule Governance and Enforcement Levels
date: 2026-05-26
status: Accepted
author: AndreyVoyage
---

# ADR-006: Rule Governance and Enforcement Levels

## Context
Voyage Framework needs a governance layer to ensure rules are not just documented but enforced. Without enforcement, rules become suggestions and the framework degrades over time.

## Decision
Implement a **4-level rule governance system** with explicit enforcement mechanisms.

## Rule Levels

### 🔴 Critical (Level 1)
**Description:** Must never be violated. Breaking these rules corrupts framework integrity.

**Examples:**
- CR-01: No duplicate files in active tree
- CR-02: Sequential numbering without gaps
- CR-03: Index synchronization (every ADR/ROLE in index)
- CR-04: Frontmatter required on all ADR/ROLE/TECH files

**Enforcement:**
- CI pipeline blocks merge if violated
- ROLE-003 (Reviewer) must reject any PR violating Critical rules
- No override possible without framework version bump

**Consequence of Violation:**
- Immediate rollback required
- Incident report mandatory
- Framework version marked as compromised

---

### 🟠 High (Level 2)
**Description:** Must be followed unless explicitly overridden by accepted ADR.

**Examples:**
- HI-01: Test coverage gate (min 80% for new code)
- HI-02: Security scanning before merge
- HI-03: Every task has assigned role
- HI-04: ADR before implementation

**Enforcement:**
- CI pipeline warns; merge requires ROLE-003 approval
- Override requires documented justification in ADR

**Consequence of Violation:**
- Merge blocked pending review
- Technical debt ticket created automatically

---

### 🟡 Medium (Level 3)
**Description:** Should be followed; deviations require justification.

**Examples:**
- ME-01: Documentation completeness (Context/Decision/Consequences)
- ME-02: Link validation (all internal links valid)
- ME-03: Changelog updates for significant changes

**Enforcement:**
- CI pipeline warns but doesn't block
- Weekly review by ROLE-003

**Consequence of Violation:**
- Warning in PR review
- Optional follow-up ticket

---

### 🟢 Low (Level 4)
**Description:** Recommended best practices.

**Examples:**
- LO-01: Markdown formatting (ATX headers, fenced blocks)
- LO-02: File organization (max 500 lines per file)

**Enforcement:**
- Automated linting suggestions
- No blocking, no warnings

**Consequence of Violation:**
- Style suggestion in PR review

---

## Governance Process

```
New Rule Proposal
      │
      ▼
┌─────────────┐
│  ROLE-003   │ ← Reviewer evaluates impact
│   Review    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Assign    │ ← Determine rule level
│   Level     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Update    │ ← Add to RULES.md
│   RULES.md  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Update    │ ← Update CI pipeline
│    CI       │ ← if Critical or High
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Merge     │
│   & Deploy  │
└─────────────┘
```

## Rule Amendment Process
1. Any role can propose amendment
2. ROLE-003 reviews and assigns new level if changed
3. If level increases (e.g., Medium → High): requires ADR
4. If level decreases: requires justification and 48h review period

## Rule Deprecation
1. Propose deprecation with rationale
2. ROLE-003 approves
3. Mark as `Deprecated` in RULES.md
4. Update all references
5. Remove from CI after 30 days grace period

## Related
- [RULES.md](../../RULES.md) — Full rule definitions
- [ROLE-003: Reviewer Engineer](../roles/ROLE-003-reviewer-engineer.md)
- [ADR-009: Complexity Budget](./ADR-009-complexity-budget.md)
