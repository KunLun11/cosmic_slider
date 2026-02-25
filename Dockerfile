FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml uv.lock req.pip ./

RUN uv venv && . .venv/bin/activate && uv pip install -r req.pip

COPY . .

RUN . .venv/bin/activate && python manage.py collectstatic --noinput

RUN mkdir -p /app/data/logs /app/data/media

EXPOSE 8000

CMD [".venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
