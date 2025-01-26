# Educational Modules API

Дипломный проект для управления образовательными модулями, уроками и пользователями с поддержкой ролей и авторизации через JWT.

## Структура проекта

Проект состоит из двух основных приложений:
- **modules** — управление образовательными модулями и уроками.
- **users** — управление пользователями с возможностью присвоения ролей.

## Технологии

- **Django** — веб-фреймворк.
- **Django Rest Framework** — для создания API.
- **PostgreSQL** — база данных.
- **JWT** — для аутентификации пользователей.
- **Docker** — для контейнеризации приложения.
- **Swagger** — для автогенерации документации API.

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Dontgoingforyou/educational_modules.git
cd educational_modules
```

### 2. Собрать контейнер Docker(Миграции и фикстуры будут загружены автоматически, код описан в docker/entrypoint.sh)
```bash
docker compose up --build
```

### 3. Доступ к серверу

- API будет доступно по адресу [http://localhost:8000](http://localhost:8000)
- Swagger документация доступна по адресу [http://localhost:8000/swagger](http://localhost:8000/swagger)

### 4. Эндпойнты API

#### Пользователи
- POST /users/token/ — Получить токен для аутентификации.
- POST /users/token/refresh/ — Обновить токен.
- GET /users/ — Получить список всех пользователей.
- GET /users/{id}/ — Получить информацию о пользователе.
- PATCH /users/{id}/update_role/ — Обновить роль пользователя (admin, teacher, student).

#### Образовательные модули
- GET /api/modules/ — Получить список образовательных модулей.
- POST /api/modules/ — Создать новый образовательный модуль.
- GET /api/modules/{id}/ — Получить информацию о модуле.
- PATCH /api/modules/{id}/ — Обновить образовательный модуль.
- DELETE /api/modules/{id}/ — Удалить образовательный модуль.
- POST /api/modules/{id}/publish/ — Опубликовать образовательный модуль.

#### Уроки
- GET /api/lessons/ — Получить список всех уроков.
- POST /api/lessons/ — Создать новый урок.
- GET /api/lessons/{id}/ — Получить информацию о уроке.
- PATCH /api/lessons/{id}/ — Обновить урок.
- DELETE /api/lessons/{id}/ — Удалить урок.

### 5. Тесты
Чтобы запустить тесты, выполните команду:
```bash
docker compose exec app python manage.py test
```