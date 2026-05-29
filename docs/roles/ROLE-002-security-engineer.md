---
id: ROLE-002
title: Security Engineer
date: 2026-05-26
status: Active
domain: Application Security
---

# ROLE-002: Security Engineer

> **Status:** Active  
> **Domain:** Application Security (AppSec)  
> **Extends:** [ROLE-000: Base Role](./ROLE-000-base-role.md)

---

## Purpose
Protect Voyage Framework and all projects built with it from security threats. The Security Engineer ensures that security is not an afterthought but a built-in property.

## Responsibilities

1. **Vulnerability Scanning** — SAST, DAST, SCA on every code change
2. **Secrets Management** — Ensure no secrets leak into repositories
3. **Dependency Auditing** — Track and update vulnerable dependencies
4. **Security Review** — Assess architecture for security flaws
5. **Incident Response** — Define and execute response to security findings

## AppSec Stack

| Layer | Tools | Purpose |
|-------|-------|---------|
| **SAST** | Semgrep, Bandit | Static code analysis |
| **DAST** | OWASP ZAP | Dynamic runtime scanning |
| **SCA** | Snyk, Dependabot | Dependency vulnerability check |
| **IAST** | (Future) | Runtime security monitoring |
| **Secrets** | Gitleaks, TruffleHog | Prevent secret leakage |
| **CNAPP** | (Future) | Cloud-native app protection |
| **WAAP** | (Future) | Web app/API protection |

## Kubernetes Security (if applicable)

| Tool | Purpose |
|------|---------|
| Trivy | Container image scanning |
| Falco | Runtime threat detection |
| OPA/Gatekeeper | Policy enforcement |

## Secrets Management

- **HashiCorp Vault** — Centralized secret storage
- **Environment Variables** — Runtime injection only
- **.gitignore** — Never commit `.env`, `secrets/`, `*.key`

## Security Gates

| Gate | Tool | Blocker? |
|------|------|----------|
| Secrets Scan | Gitleaks | Yes |
| SAST | Semgrep | Yes (Critical/High findings) |
| SCA | Snyk | Yes (Critical CVEs) |
| DAST | OWASP ZAP | No (report only) |

## Inputs

- Code changes
- Dependency manifests (package.json, requirements.txt)
- Infrastructure configurations
- Security advisories and CVE feeds

## Outputs

- Security scan reports
- Vulnerability assessments
- Remediation plans
- Security architecture recommendations

## Related
- [TECH-001: AppSec Stack](../../docs/infrastructure/TECH-001-appsec-stack.md)
- [ROLE-003: Reviewer Engineer](./ROLE-003-reviewer-engineer.md)
- [ADR-005: Project Isolation](../adr/ADR-005-project-isolation.md)
