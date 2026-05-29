---
id: ROLE-INDEX
title: AI Roles Index
date: 2026-05-28
status: Active
---

# ROLE Index

All AI role definitions for Voyage Framework.

## Active Roles

| ID | Title | Domain | Status | Extends |
|----|-------|--------|--------|---------|
| [ROLE-000](./ROLE-000-base-role.md) | Base Role (Template) | Foundation | ✅ Active | — |
| [ROLE-001](./ROLE-001-qa-engineer.md) | QA Engineer | Quality Assurance | ✅ Active | ROLE-000 |
| [ROLE-002](./ROLE-002-security-engineer.md) | Security Engineer | Application Security | ✅ Active | ROLE-000 |
| [ROLE-003](./ROLE-003-reviewer-engineer.md) | Reviewer Engineer | Governance | ✅ Active | ROLE-000 |

## Role Lifecycle

```
Planned → Draft → Active → Deprecated
   │         │        │          │
   │         │        │          └── Superseded by new role
   │         │        └── Used in production
   │         └── Under development/review
   └── Listed in FUTURE_ROLES_TECH_REGISTRY.md
```

## Status Legend

| Status | Meaning |
|--------|---------|
| ✅ Active | Approved, in use |
| 🟡 Draft | Under development |
| ⚠️ Deprecated | Superseded, do not use |
| 🔴 Planned | Listed in registry, not yet created |

## Sequential Check

- [x] ROLE-000 exists (Base template)
- [x] ROLE-001 exists
- [x] ROLE-002 exists
- [x] ROLE-003 exists
- [ ] ROLE-004 — reserved (see FUTURE_ROLES_TECH_REGISTRY.md)
- [ ] ROLE-005 — reserved
- [ ] ROLE-006 — reserved

## Maintenance
- Last updated: 2026-05-28
- Next review: 2026-06-28
- Reviewer: ROLE-003
