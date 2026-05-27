# ADR-INDEX — Реестр архитектурных решений Voyage Framework v4.0+

> **Назначение:** Единый источник правды для всех Architecture Decision Records.  
> **Правило:** Если решение не внесено в ADR-INDEX — его нет в системе.  
> **Обновляет:** Human (AndreyVoyage) + Architect Agent после каждого принятого ADR.

---

## Как пользоваться этим файлом

### Для Human (AndreyVoyage)
1. **Перед началом фазы** открой ADR-INDEX и проверь, какие ADR влияют на текущие задачи (см. колонку «Фаза»).
2. **При новом решении** создай файл `ADR-NNN-kebab-title.md`, заполни по шаблону ниже, затем добавь строку в таблицу.
3. **При изменении статуса** (Accepted → Deprecated) обнови только эту таблицу и сам ADR-файл. Мастер-документ трогать не нужно.
4. **При конфликте** двух ADR — создай новый ADR с полем `Replaces`, а в старом поставь `Status: Superseded by ADR-NNN`.

### Для Kimi Code / Kimi Agent
1. **На вход** получай только те ADR, которые указаны в `CONTEXT.json["adrs"]`.
2. **Не дублируй** содержимое ADR в мастер-документе — используй ссылки.
3. **При генерации кода** проверяй поле `Compliance` в ADR: если там написано «добавить `project_id` в модели» — это acceptance criteria для твоей задачи.

### Жизненный цикл ADR
```
Proposed → Accepted → [Deprecated | Superseded] → Archived
    ↑___________↓
    (можно вернуть из Deprecated, если отмена была ошибкой)
```
- **Proposed:** решение обсуждается, код не пишется.
- **Accepted:** решение зафиксировано, код генерируется по нему.
- **Deprecated:** решение устарело, но код ещё не мигрирован.
- **Superseded:** есть новый ADR, полностью заменяющий этот.
- **Archived:** код мигрирован, ADR сохраняется только для истории.

---

## Реестр ADR

| ID | Название | Статус | Дата | Фаза | Связанные ADR | Краткая суть |
|----|----------|--------|------|------|---------------|--------------|
| [ADR-001](ADR-001-postgresql-events.md) | PostgreSQL для Event Store | Accepted | 2026-05-21 | Phase 1 | ADR-002, ADR-004 | Primary: PostgreSQL; Fallback: SQLite WAL |
| [ADR-002](ADR-002-chromadb-semantic.md) | ChromaDB для Semantic Memory | Accepted | 2026-05-21 | Phase 1 | ADR-001, ADR-003 | Primary: ChromaDB; Fallback: SQLite keyword search |
| [ADR-003](ADR-003-tree-sitter-ast.md) | tree-sitter для AST Indexing | Accepted | 2026-05-21 | Phase 1 | ADR-004 | Unified facade ASTPython + ASTTypeScript |
| [ADR-004](ADR-004-dual-location.md) | Dual-Location Strategy | Accepted | 2026-05-21 | Phase 1 | ADR-001, ADR-002 | Отдельный репозиторий + git submodule в SkillTracer |
| [ADR-005](ADR-005-project-isolation.md) | Project Isolation & Multi-Project Core | Accepted | 2026-05-25 | Phase 1 | ADR-001, ADR-004 | `project_id` как composite key; LangGraph отложен в Phase 2 |

---

## Шаблон нового ADR

При создании `ADR-NNN-title.md` используй следующий frontmatter и структуру:

```markdown
# ADR-NNN: Краткое название решения

**Status**: Proposed | Accepted | Deprecated | Superseded | Archived  
**Date**: YYYY-MM-DD  
**Authors**: AndreyVoyage (Human) + AI Architect  
**Phase**: Phase N  
**Replaces**: ADR-XXX (или "Нет")  
**Related**: ADR-YYY, ADR-ZZZ

---

## Context
Что за проблема? Какие требования? Какие ограничения?

## Decision
Что именно решено? Однозначно, без "может быть".

## Consequences
### Positive
- ...
### Negative
- ...

## Alternatives
- **Вариант А:** ... (почему отвергнут)
- **Вариант Б:** ... (почему отвергнут)

## Compliance
Как это решение влияет на существующие принципы фреймворка?
- Event Sourcing: ...
- Security First: ...
- Spec-Driven: ...
- Fallback: ...
- Transparent: ...

## Implementation Tasks (для Kimi Code)
- [ ] Конкретное действие 1
- [ ] Конкретное действие 2

## Notes
Всё, что не влезло в формальные разделы.
```

---

## Частые ошибки (авто-правила для Self-Improving Engine)

| Ошибка | Правило |
|--------|---------|
| ADR создан, но не добавлен в ADR-INDEX | Всегда обновляй ADR-INDEX в том же коммите, что и новый ADR |
| Статус ADR = Accepted, но код не соответствует решению | Добавь `Compliance`-проверку в Reviewer Agent |
| Название файла ADR не по шаблону | Используй `ADR-NNN-kebab-case.md`, без пробелов и амперсандов |
| Дублирование ADR в мастер-документе | Мастер-документ ссылается на ADR-INDEX, не дублирует текст |

---

**Версия индекса:** 1.0  
**Дата:** 2026-05-26  
**Следующее обновление:** После принятия ADR-006
