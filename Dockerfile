FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./app /app 

WORKDIR /app

COPY ./poetry.lock /
COPY ./pyproject.toml /
COPY ./README.md /

RUN apt-get update -y && apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
RUN apt-get remove curl -y



