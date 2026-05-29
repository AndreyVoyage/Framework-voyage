---
id: VOYAGE-MASTER
title: Voyage AI Dev Framework Master Document
version: "4.0"
date: 2026-05-28
status: Active
author: AndreyVoyage
---

# Voyage AI Dev Framework — Master Document v4.0

> **AI-Native Engineering Operating System**  
> For solo developers and small teams who want to build production-grade software with AI assistance.

---

## 1. Vision & Philosophy

### 1.1 Core Idea
Voyage Framework is an operating system for AI-assisted software development. It treats AI not as a tool, but as a **collaborative engineer** with defined roles, responsibilities, and constraints.

### 1.2 Key Principles
1. **Role-Based AI** — Every AI interaction is scoped to a specific role (QA, Security, Reviewer, etc.)
2. **Decision Records** — Every architectural choice is documented in an ADR
3. **Executable Rules** — Rules are not suggestions; they are enforced by the framework
4. **Self-Improving** — The framework learns from each project and improves its own rules
5. **Solo-Developer Optimized** — Designed for 1-person teams with AI augmentation

### 1.3 Target Audience
- Solo full-stack developers
- Small teams (2–5 people)
- Indie hackers and bootstrappers
- Anyone using Kimi Code, ChatGPT, Claude, or similar AI assistants for coding

---

## 2. Architecture Overview

### 2.1 High-Level Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Voyage Framework v4.0                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   ROLES     │  │    ADRs     │  │   RULES ENGINE      │ │
│  │  (AI Roles) │  │(Decisions)  │  │  (Enforcement)      │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                    │              │
│         └────────────────┴────────────────────┘              │
│                          │                                  │
│                   ┌──────┴──────┐                          │
│                   │  ORCHESTRATOR │                         │
│                   │  (Runtime)    │                         │
│                   └──────┬──────┘                          │
│                          │                                  │
│         ┌────────────────┼────────────────┐                │
│         ▼                ▼                ▼                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │   MEMORY    │  │  TESTING    │  │  SECURITY   │       │
│  │  (Context)  │  │  (Quality)  │  │  (AppSec)   │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         Self-Improving Engine (Future)              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Component Descriptions

| Component | Description | File |
|-----------|-------------|------|
| **Roles** | AI persona definitions with responsibilities, inputs, outputs | [docs/roles/](./docs/roles/) |
| **ADRs** | Architecture Decision Records — why we chose what we chose | [docs/adr/](./docs/adr/) |
| **Rules Engine** | Executable rules with severity levels (Critical/High/Medium/Low) | [RULES.md](./RULES.md) |
| **Orchestrator** | Runtime layer that assigns roles and manages workflow | [ADR-007](./docs/adr/ADR-007-runtime-orchestration.md) |
| **Memory** | Context persistence across sessions (PostgreSQL + ChromaDB) | [ADR-001](./docs/adr/ADR-001-postgresql-events.md), [ADR-002](./docs/adr/ADR-002-chromadb-semantic.md) |
| **Testing** | Comprehensive test strategy including AI output evaluation | [TEST_STRATEGY.md](./docs/strategy/TEST_STRATEGY.md) |
| **Security** | AppSec stack and security scanning pipeline | [TECH-001](./docs/infrastructure/TECH-001-appsec-stack.md) |
| **Self-Improving Engine** | Meta-layer that analyzes framework performance and suggests improvements | [ADR-009](./docs/adr/ADR-009-complexity-budget.md) |

---

## 3. Data Flows

### 3.1 Development Flow
```
Developer Task
      │
      ▼
┌─────────────┐
│  ROLE SELECT │ ← Pick ROLE-XXX based on task type
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   CONTEXT    │ ← Load memory (PostgreSQL + ChromaDB)
│   LOADING    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  AI AGENT    │ ← Kimi Code / ChatGPT / Claude
│  EXECUTION   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   OUTPUT     │
│  VALIDATION  │ ← ROLE-001 (QA) + ROLE-003 (Reviewer)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   COMMIT     │ ← If all gates passed
│   & SAVE     │
└─────────────┘
```

### 3.2 Memory Flow
```
AI Session Output
      │
      ├──► PostgreSQL (structured events, logs, decisions)
      │
      └──► ChromaDB (semantic embeddings, context vectors)
                │
                ▼
         Next Session Query
                │
                ▼
         Retrieved Context
                │
                ├──► Short-term (recent N messages)
                └──► Long-term (semantic similarity search)
```

---

## 4. Role System

### 4.1 Active Roles

| ID | Name | Domain | Status |
|----|------|--------|--------|
| [ROLE-000](./docs/roles/ROLE-000-base-role.md) | Base Role | Template | ✅ Active |
| [ROLE-001](./docs/roles/ROLE-001-qa-engineer.md) | QA Engineer | Quality | ✅ Active |
| [ROLE-002](./docs/roles/ROLE-002-security-engineer.md) | Security Engineer | Security | ✅ Active |
| [ROLE-003](./docs/roles/ROLE-003-reviewer-engineer.md) | Reviewer Engineer | Governance | ✅ Active |

### 4.2 Role Lifecycle
```
Planned → Draft → Active → Deprecated
   │         │        │          │
   │         │        │          └── Superseded by new role
   │         │        └── Used in production
   │         └── Under development/review
   └── Listed in FUTURE_ROLES_TECH_REGISTRY.md
```

### 4.3 Role Assignment Rules
1. Every task must have exactly one primary role
2. Complex tasks may have secondary roles (max 2)
3. ROLE-003 (Reviewer) must validate any cross-role interaction
4. ROLE-000 (Base) is automatically included as foundation

---

## 5. ADR System

### 5.1 ADR Lifecycle
```
Proposed → Accepted → Deprecated
    │          │           │
    │          │           └── New ADR supersedes
    │          └── Approved by ROLE-003
    └── Created by any role, requires review
```

### 5.2 ADR Registry

| ID | Title | Status | Date |
|----|-------|--------|------|
| [ADR-001](./docs/adr/ADR-001-postgresql-events.md) | PostgreSQL Events | ✅ Accepted | 2026-05-20 |
| [ADR-002](./docs/adr/ADR-002-chromadb-semantic.md) | ChromaDB Semantic Search | ✅ Accepted | 2026-05-21 |
| [ADR-003](./docs/adr/ADR-003-tree-sitter-ast.md) | Tree-sitter AST Analysis | ✅ Accepted | 2026-05-22 |
| [ADR-004](./docs/adr/ADR-004-dual-location.md) | Dual Location Storage | ✅ Accepted | 2026-05-22 |
| [ADR-005](./docs/adr/ADR-005-project-isolation.md) | Project Isolation | ✅ Accepted | 2026-05-23 |
| [ADR-006](./docs/adr/ADR-006-rule-governance.md) | Rule Governance & Levels | ✅ Accepted | 2026-05-26 |
| [ADR-007](./docs/adr/ADR-007-runtime-orchestration.md) | Runtime Orchestration | ✅ Accepted | 2026-05-27 |
| [ADR-008](./docs/adr/ADR-008-observability.md) | Observability & Telemetry | ✅ Accepted | 2026-05-27 |
| [ADR-009](./docs/adr/ADR-009-complexity-budget.md) | Complexity Budget | ✅ Accepted | 2026-05-28 |

---

## 6. Security Architecture

### 6.1 AppSec Stack
See full details: [TECH-001: AppSec Stack](./docs/infrastructure/TECH-001-appsec-stack.md)

### 6.2 Security Gates
1. **SAST** — Static analysis on every commit
2. **DAST** — Dynamic scanning in staging
3. **SCA** — Dependency vulnerability check
4. **Secrets Scanning** — Gitleaks/TruffleHog in CI
5. **IAST** — Runtime security monitoring (future)

---

## 7. Testing Architecture

### 7.1 Test Pyramid (Voyage Extended)
```
        ┌─────────────┐
        │  AI Eval    │  ← Evaluate AI output quality
        │  (New)      │
        ├─────────────┤
        │  E2E Tests  │  ← End-to-end user flows
        ├─────────────┤
        │ Integration   │  ← API, DB, external services
        ├─────────────┤
        │  Unit Tests   │  ← Functions, classes, modules
        ├─────────────┤
        │ Mutation Tests│  ← Fault injection, robustness
        ├─────────────┤
        │ Replay Tests  │  ← Record & replay sessions
        ├─────────────┤
        │ Chaos Tests   │  ← Resilience under failure
        └─────────────┘
```

See full strategy: [TEST_STRATEGY.md](./docs/strategy/TEST_STRATEGY.md)

---

## 8. Self-Improving Engine (Concept)

### 8.1 Purpose
The Self-Improving Engine analyzes:
- Framework rule effectiveness (which rules are followed/broken)
- AI output quality trends
- Project delivery velocity
- Error patterns and root causes

### 8.2 Outputs
- Suggested ADR amendments
- New ROLE proposals
- RULE adjustments
- Complexity budget reallocation

### 8.3 Current Status
> 🟡 **Conceptual** — Architecture defined, implementation pending Phase 3.

See: [ADR-009: Complexity Budget](./docs/adr/ADR-009-complexity-budget.md)

---

## 9. Terminology

| Term | Definition |
|------|------------|
| **ADR** | Architecture Decision Record — documents why an architectural choice was made |
| **ROLE** | AI persona definition — scoped responsibilities, inputs, outputs for an AI agent |
| **RULE** | Executable constraint with severity level (Critical/High/Medium/Low) |
| **Orchestrator** | Runtime component that assigns roles and manages AI workflow |
| **Memory** | Persistence layer for context across AI sessions (PostgreSQL + ChromaDB) |
| **Self-Improving Engine** | Meta-layer that analyzes and improves the framework itself |
| **Complexity Budget** | Maximum allowed architectural complexity per phase |
| **AppSec Stack** | Application security toolchain (SAST/DAST/SCA/IAST) |

---

## 10. Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| Phase 0 | Framework definition & documentation | ✅ Complete |
| Phase 1 | Core runtime (Orchestrator + Memory) | 🟡 In Progress |
| Phase 2 | Testing & security integration | 🟡 In Progress |
| Phase 3 | Self-Improving Engine | 🔵 Planned |
| Phase 4 | Multi-project support | 🔵 Planned |
| Phase 5 | Community & ecosystem | 🔵 Future |

See detailed plan: [PHASE2_PLAN.md](./docs/strategy/PHASE2_PLAN.md)

See current status: [PHASE_STATUS.md](./docs/strategy/PHASE_STATUS.md)

---

## 11. Integration Points

### 11.1 Kimi Code (VS Code)
- Load ROLE files as system prompts
- Use RULES.md as context constraints
- Reference ADRs for architectural context

### 11.2 ChatGPT / Claude
- Use PROMPT files in `prompts/` folder
- Attach relevant ADR and ROLE files to conversation

### 11.3 LangGraph (Future)
See analysis: [LANGGRAPH_INTEGRATION_ANALYSIS.md](./docs/analysis/LANGGRAPH_INTEGRATION_ANALYSIS.md)

---

*This document is the single source of truth for Voyage Framework architecture.*  
*For questions or contributions, see [CONTRIBUTING.md](./CONTRIBUTING.md)*
