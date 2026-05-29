# Contributing to Voyage Framework

## Naming Conventions

### ADR (Architecture Decision Records)
- Format: `ADR-NNN-short-name.md`
- NNN: 3-digit sequential number (001, 002, ...)
- Must include frontmatter with `date`, `status`, `author`
- Status values: `Proposed`, `Accepted`, `Deprecated`, `Superseded`

### ROLE (AI Role Definitions)
- Format: `ROLE-NNN-role-name.md`
- NNN: 3-digit sequential number (000 for base/template)
- Must include frontmatter with `date`, `status`, `domain`
- Status values: `Draft`, `Active`, `Deprecated`

### TECH (Technology Stacks)
- Format: `TECH-NNN-tech-name.md`
- NNN: 3-digit sequential number
- Must include frontmatter with `date`, `status`, `category`

## File Structure

All new files must be placed in correct folders:
- ADR → `docs/adr/`
- ROLE → `docs/roles/`
- Strategy/Plan → `docs/strategy/`
- Analysis → `docs/analysis/`
- Infrastructure → `docs/infrastructure/`
- Prompts → `prompts/`
- Deprecated → `archive/`

## Before Committing

1. Run markdown link check: `npx markdown-link-check docs/**/*.md`
2. Run markdown lint: `npx markdownlint-cli docs/**/*.md`
3. Update relevant INDEX file (ADR-INDEX.md or ROLE-INDEX.md)
4. Update CHANGELOG.md
5. Ensure no duplicate file versions exist

## Index Maintenance

When adding a new ADR or ROLE:
1. Add entry to respective INDEX file
2. Update README.md table if applicable
3. Ensure sequential numbering (no gaps)
