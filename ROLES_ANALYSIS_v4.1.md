# Анализ ролевой модели Voyage Framework v4.0 → v4.1+

> **Назначение:** Определить, какие роли из мира веб-разработки стоит внедрить во фреймворк, когда и почему.  
> **Целевая аудитория:** Solo-разработчик (AndreyVoyage), который ведёт 1–3 проекта одновременно.  
> **Принцип:** Расширяемость без переписывания. Реестр ролей (`RoleRegistry`) позволяет добавлять агентов без изменения `agents/runtime.py`.

---

## 1. Текущая ситуация (v4.0 Phase 1)

| Роль | Статус | Что делает | Чего не хватает |
|------|--------|-----------|-----------------|
| **Architect** | ✅ Реализована | Планирует, пишет ADR, генерирует TASK.md | — |
| **Developer** | ✅ Реализована | Пишет код, тесты, читает AST | — |
| **Reviewer** | ✅ Реализована | Линтеры, quality gates, auto-rules | — |
| **DevOps** | ✅ Реализована | Деплой, мониторинг, rollback | — |

Этот набор покрывает 80% задач solo-разработчика. Но есть пробелы, которые ты уже ощущаешь:

1. **Тестирование:** Reviewer запускает pytest, но не пишет тест-кейсы и не анализирует flaky-тесты.
2. **Безопасность:** Sandbox блокирует команды, но не аудитит код на уязвимости (SQL-инъекции, XSS).
3. **Производительность:** Нет нагрузочного тестирования и профилирования.
4. **Продукт:** Нет приоритизации фич — всё решается "вручную" human'ом.

---

## 2. Предлагаемые роли для v4.1 / v4.2

### 2.1 QA Engineer (Quality Assurance Engineer)

**Зачем:**
- Reviewer проверяет *качество кода*, но не *качество продукта*.
- Ты писал про проблемы с Telegram-ботом (initData invalid, фото не удаляется) — это баги, которые QA должен ловить ДО деплоя.
- Автотесты для frontend (Playwright/Cypress) — рутина, которую можно делегировать AI.

**Обязанности:**
- Генерация тест-кейсов по acceptance criteria
- Написание E2E-тестов (Playwright для React, Aiogram-тесты для бота)
- Анализ flaky-тестов: "этот тест падает 30% времени — вот почему"
- Regression testing перед деплоем
- Покрытие кода (coverage report)

**Инструменты:** `pytest`, `playwright`, `coverage`, `grep_code` (ищет отсутствие тестов)

**Prompt focus:**
- "Напиши тест для этого acceptance criteria"
- "Почему этот тест flaky? Анализируй race condition"
- "Coverage упал с 85% до 72% — что не покрыто?"

**Когда внедрять:** v4.1 (Phase 2), сразу после стабилизации Agent Runtime.

---

### 2.2 Security Engineer (SecOps / AppSec)

**Зачем:**
- Ты спрашивал про "типичные уязвимости готового проекта" и "хакерские атаки".
- Solo-разработчик часто забывает о безопасности: hardcoded secrets, SQL-инъекции, XSS, CSRF.
- Security Sandbox блокирует *команды*, но не аудитит *код*.

**Обязанности:**
- Статический анализ кода на уязвимости (bandit, semgrep, npm audit)
- Проверка зависимостей: "у тебя 3 критических CVE в пакетах"
- Аудит конфигурации: "CORS разрешён для всех доменов — это риск"
- Проверка секретов: "найден hardcoded token в `config.py:15`"
- Compliance с ADR-005 security measures

**Инструменты:** `bandit`, `semgrep`, `npm_audit`, `grep_code` (ищет `password=`, `token=`), `cat_file`

**Prompt focus:**
- "Просканируй код на OWASP Top 10"
- "Найди все hardcoded secrets"
- "Проверь CORS и CSP конфигурацию"

**Когда внедрять:** v4.1 (Phase 2), параллельно с QA Engineer. Это не требует новой инфраструктуры — только новый адаптер в `tools/adapters/`.

---

### 2.3 Performance Engineer

**Зачем:**
- SkillTracer — это Telegram-бот + React SPA. Пока нагрузка низкая, но при росте пользователей (3 → 30 → 300) нужно понимать узкие места.
- Solo-разработчик не делает нагрузочное тестирование "потому что некогда".

**Обязанности:**
- Профилирование: "эта функция выполняется 2.3 секунды — вот bottleneck"
- Нагрузочное тестирование API (locust, k6)
- Анализ БД: "этот запрос делает sequential scan на 50k строк"
- Frontend: "LCP 4.2 секунды — оптимизируй изображения"

**Инструменты:** `locust`, `k6`, `explain_query` (PostgreSQL), `chrome_lighthouse`

**Prompt focus:**
- "Сделай нагрузочный тест для `/api/entries`"
- "Почему этот SQL-запрос медленный?"
- "Оптимизируй React re-renders"

**Когда внедрять:** v4.2 (Phase 2+). Не критично для текущего этапа SkillTracer.

---

### 2.4 Product Manager (PM)

**Зачем:**
- Сейчас приоритизация фич — полностью на human'е. "Что делать следующим?" — ты решаешь сам.
- PM-агент может анализировать бэклог, метрики и ошибки, и предлагать: "вот топ-3 задачи на следующую неделю".

**Обязанности:**
- Приоритизация бэклога по impact/effort
- Анализ ошибок: "эта ошибка затронула 80% пользователей — критично"
- Генерация user stories по метрикам
- Связь бизнес-целей и технических задач

**Инструменты:** `semantic_query` (поиск по ошибкам), `event_engine` (статистика по событиям), `github` (активность PR)

**Prompt focus:**
- "Какие фичи дадут максимальный impact при минимальном effort?"
- "Проанализируй ошибки за неделю и предложи приоритеты"

**Когда внедрять:** v5.0 (Phase 3). Это скорее "nice to have", чем необходимость. Solo-разработчик обычно хорошо знает продукт.

---

## 3. Роли, которые НЕ нужны (пока)

| Роль | Почему не нужна |
|------|-----------------|
| **UX/UI Designer** | Для SkillTracer дизайн уже определён (Telegram WebApp + стандартные компоненты). Если понадобится — используй отдельные AI-инструменты (Midjourney, Figma AI). |
| **Frontend-архитектор** | Обязанности покрываются Architect + Developer. Для SPA нет сложной frontend-архитектуры. |
| **Backend-архитектор** | Architect уже делает это. |
| **Database Developer** | SQLAlchemy + PostgreSQL покрывают 95% задач. Сложные миграции — задача Architect. |
| **HTML-верстальщик** | React + Tailwind/CSS-in-JS — Developer справляется. |
| **SEO-специалист** | SkillTracer — закрытое приложение (Telegram WebApp), SEO не нужен. |
| **Технический писатель** | Документация генерируется автоматически из ADR + specs. |
| **SRE / Cloud-инженер** | DevOps покрывает мониторинг и деплой. VPS на FirstVDS не требует Kubernetes. |

---

## 4. Матрица компетенций (кто что может)

| Действие | Architect | Developer | Reviewer | DevOps | QA | Security | Performance |
|----------|-----------|-----------|----------|--------|----|----------|-------------|
| Писать код | ❌ | ✅ | ❌ | ❌ | ✅ (тесты) | ✅ (скрипты аудита) | ✅ (скрипты нагрузки) |
| Писать ADR | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Запускать pytest | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Запускать mypy/ruff | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Деплоить | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Писать E2E-тесты | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Аудит безопасности | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Нагрузочное тестирование | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Human approval | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Генерировать TASK.md | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Добавлять правила в RULES.md | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |

---

## 5. Реализация через RoleRegistry

Чтобы не переписывать `agents/runtime.py` при добавлении роли, используем реестр:

```python
# agents/roles/registry.py
from typing import Dict, Type
from .base import AgentRole

class RoleRegistry:
    _roles: Dict[str, Type[AgentRole]] = {}

    @classmethod
    def register(cls, name: str, role_class: Type[AgentRole]):
        cls._roles[name] = role_class

    @classmethod
    def get(cls, name: str) -> Type[AgentRole]:
        if name not in cls._roles:
            raise ValueError(f"Unknown role: {name}. Available: {list(cls._roles.keys())}")
        return cls._roles[name]

    @classmethod
    def list_roles(cls) -> list[str]:
        return list(cls._roles.keys())

# Регистрация базовых ролей (Phase 1)
from .architect import ArchitectRole
from .developer import DeveloperRole
from .reviewer import ReviewerRole
from .devops import DevOpsRole

RoleRegistry.register("architect", ArchitectRole)
RoleRegistry.register("developer", DeveloperRole)
RoleRegistry.register("reviewer", ReviewerRole)
RoleRegistry.register("devops", DevOpsRole)

# Регистрация новых ролей (Phase 2) — просто добавить файл и строку
from .qa import QAEngineerRole
from .security import SecurityEngineerRole
from .performance import PerformanceEngineerRole

RoleRegistry.register("qa", QAEngineerRole)
RoleRegistry.register("security", SecurityEngineerRole)
RoleRegistry.register("performance", PerformanceEngineerRole)
```

**Workflow YAML** тоже не меняется:
```yaml
nodes:
  - name: run_tests
    role: qa  # ← просто меняем строку, runtime подтянет класс из реестра
    tools: [pytest, playwright]
```

---

## 6. Roadmap внедрения ролей

```
Phase 1 (v4.0, сейчас)
├── Architect
├── Developer
├── Reviewer
└── DevOps

Phase 2 (v4.1, Q3 2026)
├── + QA Engineer (тесты, coverage, flaky analysis)
├── + Security Engineer (bandit, semgrep, secrets audit)
└── + RoleRegistry (рефакторинг без breaking changes)

Phase 2+ (v4.2, Q4 2026)
├── + Performance Engineer (locust, profiling, SQL explain)
└── + Parallel agent execution (Developer + QA одновременно)

Phase 3 (v5.0, 2027)
├── + Product Manager (приоритизация, бэклог)
└── + Custom roles через plugin system
```

---

## 7. Чек-лист добавления новой роли

Когда решишь, что пора добавить роль (например, QA Engineer):

- [ ] Определить **обязанности** — что именно агент будет делать, чего не делают текущие 4 роли.
- [ ] Определить **инструменты** — какие адаптеры нужны в `tools/adapters/`.
- [ ] Создать класс `agents/roles/qa.py`, наследующий `AgentRole`.
- [ ] Зарегистрировать в `RoleRegistry`.
- [ ] Добавить workflow-определения, использующие `role: qa`.
- [ ] Написать тесты: `test_agents_roles_qa.py`.
- [ ] Обновить `RolePolicy` в `security/policy.py` — что может QA.
- [ ] Обновить этот документ (ROLES_ANALYSIS.md) — статус роли изменён на "Implemented".
- [ ] НЕ трогать `agents/runtime.py` — реестр должен работать автоматически.

---

## 8. Вывод

**Для SkillTracer прямо сейчас:**
- 4 роли (Architect, Developer, Reviewer, DevOps) достаточны.
- Не раздувай Phase 1. Закончи foundation, потом добавляй.

**Первая роль для v4.1:**
- **QA Engineer** — потому что ты уже сталкиваешься с багами (initData, фото, удаление), и ручное тестирование через Telegram-бот — медленно.

**Вторая роль для v4.1:**
- **Security Engineer** — потому что ты спрашивал про уязвимости, и solo-разработчик склонен забывать о безопасности.

**Performance Engineer и Product Manager:**
- Отложить до v4.2/v5.0. Не критично для текущего масштаба.

---

**Версия документа:** 1.0  
**Дата:** 2026-05-26  
**Авторы:** AndreyVoyage (Human) + AI Architect  
**Следующее обновление:** После внедрения RoleRegistry в Phase 2
