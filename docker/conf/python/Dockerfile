FROM python:3.11

ENV POETRY_VERSION=1.2.2 \
    POETRY_HOME=/etc/poetry \
    ENV=dev

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install and setup poetry
RUN apt-get update \
    && apt install -y python3-dev default-libmysqlclient-dev build-essential \
    && pip install -U pip \
    && pip install mysqlclient \
    && apt-get update \
    && apt install -y curl \
    && curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 - --version $POETRY_VERSION


ENV PATH="${PATH}:$POETRY_HOME/bin"

WORKDIR /app__pycache__

COPY pyproject.toml poetry.lock* /app/