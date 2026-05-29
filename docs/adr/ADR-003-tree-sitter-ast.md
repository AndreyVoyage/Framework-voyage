---
id: ADR-003
title: Tree-sitter for AST Analysis
date: 2026-05-22
status: Accepted
author: AndreyVoyage
---

# ADR-003: Tree-sitter for AST Analysis

## Context
The Self-Improving Engine needs to analyze code structure to:
- Measure complexity
- Detect patterns
- Suggest refactorings
- Build dependency graphs

## Decision
Use **Tree-sitter** for Abstract Syntax Tree (AST) parsing.

## Rationale
1. **Multi-language** — supports Python, TypeScript, JavaScript, and more
2. **Fast** — incremental parsing, real-time performance
3. **Battle-tested** — used by GitHub, Neovim, VS Code
4. **Python bindings** — easy integration with Voyage stack

## Consequences
### Positive
- Accurate code structure analysis
- Language-agnostic framework core
- Enables complex static analysis

### Negative
- Requires grammar files for each language
- AST complexity varies by language

## Alternatives Considered
- **Babel** — rejected: JavaScript-only
- **ANTLR** — rejected: heavier, more complex setup
- **Custom parser** — rejected: too much maintenance burden

## Related
- [ADR-009: Complexity Budget](./ADR-009-complexity-budget.md)
