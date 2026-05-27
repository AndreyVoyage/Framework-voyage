# FUTURE_ROLES_TECH_REGISTRY — Сводный реестр будущего развития

> **Назначение:** Единая таблица "что запланировано → когда → в каком статусе".  
> **Правило:** Это 'дорожная карта' на уровне ролей и технологий, а не фаз.  
> **Обновляет:** Human (AndreyVoyage) каждую неделю или при принятии решения.

---

## Как читать этот файл

**Строка = одна единица развития** (роль, технология, интеграция).  
**Колонки:**
- **ID:** ROLE-NNN, TECH-NNN, INT-NNN (integration).
- **Название:** Человекочитаемое.
- **Тип:** Role / Tech / Integration.
- **Phase:** Когда внедрять (Phase 1/2/3).
- **Статус:** Concept → Planned → In Progress → Implemented → Active.
- **Блокируется:** Что нужно сделать ДО этого (зависимости).
- **AC:** Acceptance Criteria — когда считать "готово".

---

## Сводная таблица

| ID | Название | Тип | Phase | Статус | Блокируется | AC |
|----|----------|-----|-------|--------|-------------|----|
| ROLE-000 | Base AgentRole | Role | Phase 1 | Implemented | — | ABC класс, наследование |
| ROLE-001 | QA Engineer | Role | Phase 2 | Planned | ROLE-000, Agent Runtime stable | Playwright + aiogram tests, coverage ≥80% |
| ROLE-002 | Security Engineer | Role | Phase 2 | Planned | ROLE-000, Agent Runtime stable | bandit + semgrep + gitleaks clean |
| ROLE-003 | Performance Engineer | Role | Phase 2+ | Concept | ROLE-001, ROLE-002 | Locust tests, profiling reports |
| ROLE-004 | Product Manager | Role | Phase 3 | Concept | Visualizer API, metrics | Приоритизация по impact/effort |
| TECH-001 | AppSec Stack | Tech | Phase 2 | Planned | Tool Engine stable | 6 адаптеров (bandit, semgrep, zap, sca, secrets, config) |
| TECH-002 | Testing Stack | Tech | Phase 2 | Planned | Tool Engine stable | 3 адаптера (playwright, aiogram_test, coverage) |
| TECH-003 | Performance Stack | Tech | Phase 2+ | Concept | TECH-002 | locust, k6, explain_query |
| INT-001 | LangGraph Adapter | Integration | Phase 2+ | Planned | Orchestrator Adapter stub | YAML workflow → LangGraph graph |
| INT-002 | GitHub Actions CI | Integration | Phase 2 | Planned | ROLE-001, ROLE-002 | Pipeline: lint → test → security → deploy |
| INT-003 | HashiCorp Vault | Integration | Phase 2+ | Concept | DevOps role stable | Secrets вне репозитория |
| INT-004 | Cloudflare WAF | Integration | Phase 2+ | Concept | DevOps role stable | DDoS + bot protection |

---

## Принцип добавления новой строки

**Ты спрашиваешь:** "с развитием проекта мы просто добавим ещё один файл под номером 5?"  
**Ответ:** Да, но с разделением по типам:

```
Новая роль → ROLE-005-xxx.md + строка в ROLE-INDEX.md + строка в FUTURE_ROLES_TECH_REGISTRY
Новая технология → TECH-004-xxx.md + строка в TECH-001 (или новый TECH-NNN) + строка в FUTURE_ROLES_TECH_REGISTRY
Новая интеграция → INT-005-xxx.md + строка в FUTURE_ROLES_TECH_REGISTRY
```

**Почему так:**
- ADR — это для архитектурных решений (почему PostgreSQL, а не MongoDB).
- ROLE — это для агентов (кто и что делает).
- TECH — это для инструментов (чем делать).
- INT — это для внешних интеграций (с чем соединяться).

**Не смешивай:** Не пиши про `bandit` в ADR — это технология, не архитектурное решение. Не пиши про `project_id` в ROLE — это архитектура, не роль.

---

## Чек-лист еженедельного обзора

Каждую неделю (или при планировании спринта):

- [ ] Открыть FUTURE_ROLES_TECH_REGISTRY.
- [ ] Проверить статусы: что перешло из Planned → In Progress?
- [ ] Проверить блокеры: что разблокировалось?
- [ ] Выбрать 1–2 пункта на следующую неделю.
- [ ] Обновить статусы и AC (если достигнуты).
- [ ] НЕ трогать мастер-документ — он обновляется только при смене Phase.

---

**Версия реестра:** 1.0  
**Дата:** 2026-05-26  
**Следующее обновление:** После перехода ROLE-001 или ROLE-002 в статус In Progress
