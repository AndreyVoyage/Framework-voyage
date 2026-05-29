---
id: TECH-001
title: Application Security Stack
date: 2026-05-26
status: Active
category: Security
---

# TECH-001: Application Security (AppSec) Stack

> **Category:** Security Infrastructure  
> **Status:** Active  
> **Owner:** ROLE-002 (Security Engineer)

---

## 1. Security Layers

```
┌─────────────────────────────────────────────┐
│              WAAP / API Gateway               │  ← Future
├─────────────────────────────────────────────┤
│              CNAPP / Cloud Security           │  ← Future
├─────────────────────────────────────────────┤
│              IAST (Runtime)                   │  ← Future
├─────────────────────────────────────────────┤
│              DAST (Dynamic)                   │  ← Staging
├─────────────────────────────────────────────┤
│              SCA (Dependencies)               │  ← CI/CD
├─────────────────────────────────────────────┤
│              SAST (Static)                      │  ← CI/CD
├─────────────────────────────────────────────┤
│              Secrets Management                 │  ← CI/CD + Local
├─────────────────────────────────────────────┤
│              Kubernetes Security                │  ← If applicable
├─────────────────────────────────────────────┤
│              DevSecOps Pipeline                 │  ← CI/CD
└─────────────────────────────────────────────┘
```

---

## 2. Toolchain

### 2.1 SAST (Static Application Security Testing)

| Tool | Language | Purpose |
|------|----------|---------|
| **Semgrep** | Multi | Pattern-based security scanning |
| **Bandit** | Python | Python-specific security issues |
| **eslint-security** | JS/TS | JavaScript security rules |

**Integration:** CI pipeline, pre-commit hooks

### 2.2 DAST (Dynamic Application Security Testing)

| Tool | Purpose |
|------|---------|
| **OWASP ZAP** | Web app vulnerability scanning |

**Integration:** Staging environment, weekly scans

### 2.3 SCA (Software Composition Analysis)

| Tool | Purpose |
|------|---------|
| **Snyk** | Dependency vulnerability detection |
| **Dependabot** | GitHub-native dependency updates |

**Integration:** CI pipeline, daily scans

### 2.4 IAST (Interactive Application Security Testing)

| Tool | Purpose |
|------|---------|
| **(Future)** | Runtime security monitoring |

**Status:** Planned for Phase 3

### 2.5 Secrets Management

| Tool | Purpose |
|------|---------|
| **HashiCorp Vault** | Centralized secret storage |
| **Gitleaks** | Prevent secret leakage in commits |
| **TruffleHog** | Deep secret scanning in history |

**Rules:**
- Never commit secrets to Git
- Use `.env` files (in `.gitignore`)
- Rotate secrets quarterly
- Vault for production, `.env` for local dev

### 2.6 Kubernetes Security (if using K8s)

| Tool | Purpose |
|------|---------|
| **Trivy** | Container image vulnerability scanning |
| **Falco** | Runtime threat detection |
| **OPA/Gatekeeper** | Policy enforcement |

### 2.7 CNAPP / WAAP (Future)

| Layer | Tool | Status |
|-------|------|--------|
| CNAPP | (TBD) | Planned |
| WAAP | (TBD) | Planned |

---

## 3. Security Pipeline

```
Developer Commit
      │
      ▼
┌─────────────┐
│  Pre-commit  │ ← Gitleaks local scan
│   Hooks      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    CI/CD     │ ← SAST + SCA + Secrets
│   Pipeline   │
└──────┬──────┘
       │
       ├──► Fail → Block merge
       │
       └──► Pass → Merge
              │
              ▼
       ┌─────────────┐
       │   Staging    │ ← DAST scan
       │   Deploy     │
       └──────┬──────┘
              │
              ├──► Fail → Alert ROLE-002
              │
              └──► Pass → Production
                     │
                     ▼
              ┌─────────────┐
              │  Production  │ ← Runtime monitoring (future IAST)
              │   Monitor    │
              └─────────────┘
```

---

## 4. AI Security

### 4.1 AI-Specific Risks
- **Prompt Injection** — Malicious input manipulating AI output
- **Data Leakage** — AI exposing sensitive training data
- **Hallucination** — AI generating insecure code patterns
- **Dependency Poisoning** — AI suggesting vulnerable packages

### 4.2 Mitigations
- Input validation before AI processing
- Output sanitization (escape HTML, SQL, etc.)
- Dependency verification (SCA on AI-suggested packages)
- Security review of AI-generated code (ROLE-002)

---

## 5. Incident Response

### 5.1 Severity Levels

| Level | Response Time | Action |
|-------|---------------|--------|
| Critical | Immediate | Stop pipeline, alert, investigate |
| High | 4 hours | Assess impact, patch, deploy |
| Medium | 24 hours | Schedule fix, monitor |
| Low | 7 days | Backlog, address in next sprint |

### 5.2 Playbook
1. **Detect** — Automated scan or manual report
2. **Assess** — ROLE-002 evaluates severity
3. **Contain** — Isolate affected component
4. **Remediate** — Fix and verify
5. **Document** — Update ADR if architectural
6. **Learn** — Update rules to prevent recurrence

---

## 6. Related

- [ROLE-002: Security Engineer](../roles/ROLE-002-security-engineer.md)
- [TEST_STRATEGY.md](./TEST_STRATEGY.md)
- [ADR-005: Project Isolation](../adr/ADR-005-project-isolation.md)

---

*Last updated: 2026-05-28*
