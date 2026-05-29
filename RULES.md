# RULES.md — Executable Rules for Voyage Framework

> **Version:** v1.4  
> **Status:** Active  
> **Date:** 2026-05-28  
> **Supersedes:** RULES_OLD.md, RULES_v1.3_fixed.md

---

## Rule Levels

| Level | Name | Description | Examples |
|-------|------|-------------|----------|
| 🔴 **Critical** | Must never be violated | Breaking these rules corrupts the framework integrity | Naming conventions, index updates, no duplicates |
| 🟠 **High** | Must be followed unless explicitly overridden by ADR | Core operational rules | Test coverage gates, security scanning, role assignment |
| 🟡 **Medium** | Should be followed; deviations require justification | Quality and consistency rules | Documentation completeness, link validation |
| 🟢 **Low** | Recommended best practices | Style and formatting | Markdown formatting, file organization |

---

## 🔴 Critical Rules

### CR-01: No Duplicate Files
- Only one canonical version of each document may exist in the active tree.
- Old versions must be moved to `archive/` or deleted (rely on Git history).

### CR-02: Sequential Numbering
- ADR: `ADR-001`, `ADR-002`, ... — no gaps, no duplicates.
- ROLE: `ROLE-000` (base), `ROLE-001`, `ROLE-002`, ... — no gaps.
- TECH: `TECH-001`, `TECH-002`, ... — no gaps.

### CR-03: Index Synchronization
- Every ADR must be listed in `ADR-INDEX.md`.
- Every ROLE must be listed in `ROLE-INDEX.md`.
- Every TECH must be listed in `FUTURE_ROLES_TECH_REGISTRY.md`.

### CR-04: Frontmatter Required
- Every ADR, ROLE, and TECH file must include YAML frontmatter:
  ```yaml
  ---
  id: ADR-001
  title: PostgreSQL Events
  date: 2026-05-28
  status: Accepted
  author: AndreyVoyage
  ---
  ```

---

## 🟠 High Rules

### HI-01: Test Coverage Gate
- Every code change must have corresponding test coverage.
- Minimum threshold: 80% line coverage for new code.
- Refer to [TEST_STRATEGY.md](./docs/strategy/TEST_STRATEGY.md).

### HI-02: Security Scanning
- All dependencies must be scanned for vulnerabilities before merge.
- Secrets must never be committed (use `.env` + `.gitignore`).
- Refer to [TECH-001](./docs/infrastructure/TECH-001-appsec-stack.md).

### HI-03: Role Assignment
- Every task must be assigned to a specific ROLE from the registry.
- No task without an assigned role may enter the execution pipeline.

### HI-04: ADR Before Implementation
- No architectural change may be implemented without an accepted ADR.
- ADR must be reviewed by at least one other role (ROLE-003 Reviewer).

---

## 🟡 Medium Rules

### ME-01: Documentation Completeness
- Every ADR must include: Context, Decision, Consequences, Status.
- Every ROLE must include: Responsibilities, Inputs, Outputs, Constraints.
- Every TECH must include: Stack description, Rationale, Alternatives considered.

### ME-02: Link Validation
- All internal links must be valid before commit.
- Use relative paths (`./docs/adr/ADR-001.md`, not absolute URLs).

### ME-03: Changelog Updates
- Every significant change must be recorded in `CHANGELOG.md`.
- Use categories: Added, Changed, Deprecated, Removed, Fixed, Security.

---

## 🟢 Low Rules

### LO-01: Markdown Formatting
- Use ATX-style headers (`#` not `=====`).
- Use fenced code blocks with language tags.
- Tables should be aligned for readability.

### LO-02: File Organization
- Keep files under 500 lines when possible.
- Split large documents into sections with clear anchors.

---

## Rule Governance

- **Authority:** ROLE-003 (Reviewer Engineer) has final say on rule interpretation.
- **Amendment:** New rules require ADR approval (follow ADR-006 process).
- **Deprecation:** Rules may be deprecated via ADR with `Superseded` status.

---

*This file is the single source of truth for Voyage Framework rules.*
