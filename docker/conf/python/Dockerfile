FROM python:3.9

ENV POETRY_VERSION=1.1.15 \
    ENV=dev

# Install and setup poetry
RUN pip install -U pip \
    && pip install mysqlclient \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version $POETRY_VERSION

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
  && poetry install