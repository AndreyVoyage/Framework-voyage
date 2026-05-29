---
id: PROMPT-ANALYZE
title: Prompt: Analyze Framework
date: 2026-05-28
status: Active
---

# PROMPT: Analyze Voyage Framework

## Purpose
Use this prompt to analyze the current state of Voyage Framework and identify gaps, inconsistencies, or improvements.

## Prompt Text

```
You are ROLE-003 (Reviewer Engineer) for Voyage AI Dev Framework.

Analyze the following framework files:
1. RULES.md — check for completeness and consistency
2. All ADRs — check for conflicts, gaps, missing frontmatter
3. All ROLEs — check for completeness, overlaps, missing index entries
4. TEST_STRATEGY.md — check coverage of all test types
5. Master Document — check alignment with ADRs and ROLEs

For each file:
- [ ] Verify frontmatter (id, title, date, status)
- [ ] Check internal links are valid
- [ ] Identify TODO, FIXME, or incomplete sections
- [ ] Check for duplicate or conflicting information
- [ ] Verify sequential numbering (ADR-001, ADR-002... no gaps)

Output format:
## File: {filename}
- Status: OK / Warning / Critical
- Issues: {list}
- Recommendations: {list}

## Summary
- Critical issues: {count}
- Warnings: {count}
- Recommended actions: {prioritized list}
```

## Usage
1. Copy this prompt into Kimi Code or ChatGPT
2. Attach all framework files as context
3. Review output and create ADRs for structural changes

---

*Last updated: 2026-05-28*
