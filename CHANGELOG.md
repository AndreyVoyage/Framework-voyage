# Changelog

All notable changes to Voyage AI Dev Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [v4.0] - 2026-05-28

### Added
- Full repository restructuring: `docs/adr/`, `docs/roles/`, `docs/strategy/`, `docs/analysis/`, `docs/infrastructure/`
- ADR-006: Completed Rule Levels section (Critical/High/Medium/Low)
- TEST_STRATEGY.md: Added Mutation Testing, Replay Testing, Chaos Testing, CI Gates, AI Evaluation sections
- ROLE-000: Added to ROLE-INDEX.md
- CHANGELOG.md and CONTRIBUTING.md
- GitHub Actions workflow: markdown-lint.yml
- Frontmatter (YAML) in all ADR and ROLE files

### Changed
- Consolidated duplicate files: removed `(2)`, `RULES_OLD`, `RULES_v1.3_fixed`, `ADR-006-ACCEPTED`
- Renamed `VOYAGE_FRAMEWORK_MASTER_DOCUMENT_v4.0b.md` → `VOYAGE_FRAMEWORK_MASTER_DOCUMENT.md`
- Fixed all internal links to match new folder structure
- Updated ADR-INDEX.md and ROLE-INDEX.md

### Removed
- `VOYAGE_FRAMEWORK_MASTER_DOCUMENT (2).md` (duplicate)
- `RULES_OLD.md` (superseded by RULES.md)
- `RULES_v1.3_fixed.md` (merged into RULES.md)
- `ADR-006-rule-governance-ACCEPTED.md` (merged into ADR-006)
- `INSTRUCTIONS.md` (content merged into README.md)

## [v3.x] - 2026-05-25 to 2026-05-27

### Added
- Initial ADR set (001–005)
- ROLE-001 (QA Engineer), ROLE-002 (Security Engineer)
- TEST_STRATEGY.md initial version
- FUTURE_ROLES_TECH_REGISTRY.md
- LANGGRAPH_INTEGRATION_ANALYSIS.md

## [v2.x] - 2026-05-20 to 2026-05-24

### Added
- Voyage Framework concept and master document
- Initial RULES.md
- PROMPT files for Kimi Code
- PHASE2_PLAN.md and PHASE_STATUS.md
