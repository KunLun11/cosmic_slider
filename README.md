# Cosmic — Django Project

(Тестовое задание) Django-проект с админ-панелью Unfold и слайдером.

## Стек

- **Backend:** Django 5.2
- **Admin:** Unfold + django-filer
- **Database:** MySQL 8.0
- **Python:** 3.12

## Быстрый старт

### Локальная разработка

```bash
# Установка зависимостей
uv sync

# Запуск сервера
python manage.py runserver
```

### Docker

#### Разработка

```bash
# Запуск всех сервисов
docker compose up -d

# Применение миграций
docker exec cosmic_web .venv/bin/python manage.py migrate

# Создание суперпользователя
docker exec cosmic_web .venv/bin/python manage.py createsuperuser

# Просмотр логов
docker compose logs -f web
```

Сервер доступен на `http://localhost:8000`  
База данных на `localhost:3307`

#### Production

```bash
docker compose --profile production up -d
```

## Админ-панель

```
http://localhost:8000/admin/
```

## Структура

```
.
├── config/          # Настройки Django
├── base/            # Базовые модели и утилиты
├── slider/          # Приложение слайдера
├── data/            # Данные (логи, медиа, шаблоны)
├── staticfiles/     # Собранная статика
├── media/           # Загруженные файлы
├── Dockerfile       # Образ для production
├── docker-compose.yml
└── req.pip          # Зависимости
```

