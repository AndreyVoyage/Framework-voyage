# ROLE-INDEX — Реестр ролей агентов Voyage Framework v4.0+

> **Назначение:** Единый источник правды для всех ролей AI-агентов.  
> **Правило:** Если роль не внесена в ROLE-INDEX — её нет в системе.  
> **Обновляет:** Human (AndreyVoyage) + Architect Agent при добавлении новой роли.  
> **Связь с ADR:** Роли реализуют архитектурные решения, но не являются ими. ROLE ≠ ADR.

---

## Как пользоваться этим файлом

### Для Human (AndreyVoyage)
1. **Перед планированием фазы** открой ROLE-INDEX и проверь, какие роли уже реализованы, а какие запланированы.
2. **При добавлении роли** создай файл `ROLE-NNN-kebab-name.md`, заполни по шаблону ниже, затем добавь строку в таблицу.
3. **При изменении статуса** (Planned → Implemented) обнови только эту таблицу и сам ROLE-файл.
4. **Не дублируй** содержимое ROLE в мастер-документ — используй ссылки.

### Для Kimi Code / Kimi Agent
1. **На вход** получай `CONTEXT.json["roles"]` — список активных ролей для текущего workflow.
2. **Не инициализируй** роль, если она в статусе `Planned` — логируй warning.
3. **При генерации кода** проверяй поле `Tools` в ROLE: если там `bandit` — убедись, что адаптер существует в `tools/adapters/`.

### Жизненный цикл роли
```
Concept → Planned → Implemented → Active → Deprecated → Archived
    ↑___________↓
    (можно вернуть из Deprecated, если отмена была ошибкой)
```
- **Concept:** идея роли, обсуждается в ROLES_ANALYSIS.md.
- **Planned:** решено внедрить, есть спецификация ROLE-NNN, но кода нет.
- **Implemented:** класс роли создан, зарегистрирован в RoleRegistry, тесты проходят.
- **Active:** роль используется в workflow (есть YAML-определения, использующие `role: xxx`).
- **Deprecated:** роль устарела, заменена другой.
- **Archived:** код удалён, ROLE-файл сохранён для истории.

---

## Реестр ролей

| ID | Название | Статус | Phase | Инструменты | Технологии | Краткая суть |
|----|----------|--------|-------|-------------|------------|--------------|
| [ROLE-000](ROLE-000-base-role.md) | Base AgentRole (ABC) | Implemented | Phase 1 | — | Python ABC | Базовый класс для всех ролей |
| [ROLE-001](ROLE-001-qa-engineer.md) | QA Engineer | Planned | Phase 2 | pytest, playwright, coverage, grep_code | Playwright, Cypress, Jest | Тесты, coverage, flaky analysis |
| [ROLE-002](ROLE-002-security-engineer.md) | Security Engineer (AppSec) | Planned | Phase 2 | bandit, semgrep, gitleaks, npm_audit, grep_code | SAST, DAST, SCA, IAST, Vault | Уязвимости, secrets, compliance |
| ROLE-003 | Performance Engineer | Concept | Phase 2+ | locust, k6, explain_query, chrome_lighthouse | Locust, k6, PostgreSQL EXPLAIN | Нагрузка, profiling, оптимизация |
| ROLE-004 | Product Manager | Concept | Phase 3 | semantic_query, event_engine, github | Metrics, Backlog, Prioritization | Приоритизация, бэклог, метрики |

---

## Шаблон новой роли

При создании `ROLE-NNN-kebab-name.md` используй следующую структуру:

```markdown
# ROLE-NNN: Название роли

**Status**: Concept | Planned | Implemented | Active | Deprecated | Archived  
**Date**: YYYY-MM-DD  
**Authors**: AndreyVoyage (Human) + AI Architect  
**Phase**: Phase N  
**Replaces**: ROLE-XXX (или "Нет")  
**Related**: ROLE-YYY, ADR-ZZZ, TECH-WWW

---

## Purpose
Зачем эта роль? Какую задачу решает, которую не решают текущие роли?

## Responsibilities
- Что именно делает агент?
- Что НЕ делает (границы ответственности)?

## Tools
| Адаптер | Инструменты | Требует approval |
|---------|-------------|------------------|
| xxx.py | `tool_a`, `tool_b` | Да / Нет |

## Prompt Focus
- Что спрашивать у агента?
- Какие acceptance criteria для его работы?

## Policy (что может / не может)
- **Может:** ...
- **Не может:** ...

## Implementation Tasks (для Kimi Code)
- [ ] Создать `agents/roles/xxx.py`
- [ ] Зарегистрировать в `RoleRegistry`
- [ ] Добавить workflow-определения
- [ ] Написать тесты
- [ ] Обновить `security/policy.py`

## Notes
```

---

## Частые ошибки (авто-правила для Self-Improving Engine)

| Ошибка | Правило |
|--------|---------|
| ROLE создан, но не добавлен в ROLE-INDEX | Всегда обновляй ROLE-INDEX в том же коммите |
| Роль в статусе Planned, но код уже написан | Статус должен быть Implemented ДО merge |
| Дублирование ROLE в мастер-документе | Мастер-документ ссылается на ROLE-INDEX, не дублирует текст |
| Роль реализована, но не зарегистрирована в RoleRegistry | Регистрация — обязательный шаг в Implementation Tasks |

---

**Версия индекса:** 1.0  
**Дата:** 2026-05-26  
**Следующее обновление:** После реализации ROLE-001 или ROLE-002
