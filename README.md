# simple-api

A minimal REST API built with [FastAPI](https://fastapi.tiangolo.com/), packaged as a Docker container and shipped via GitHub Actions.

## Table of Contents

- [Requirements](#requirements)
- [Local Development](#local-development)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [Code Quality](#code-quality)

---

## Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| [Python](https://www.python.org/) | 3.14 | Runtime |
| [uv](https://docs.astral.sh/uv/) | latest | Package & project manager |
| [Docker](https://www.docker.com/) | 20.10+ | Container build & run |

---

## Local Development

**1. Clone and install dependencies**

```bash
git clone <repo-url>
cd simple-api
uv sync
```

**2. Set required environment variables**

```bash
export SERVER_HELLO="Hello, World!"
```

**3. Start the development server**

```bash
uv run fastapi dev app/main.py
```

The API will be available at `http://localhost:8000`.
Interactive docs (Swagger UI) at `http://localhost:8000/docs`.

---

## Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `SERVER_HELLO` | Yes | Text returned by the `GET /hello-world` endpoint |

---

## API Reference

### `GET /health-check`


**Response `200 OK`**
```json
{"status": "ok"}
```

---

### `GET /hello-world`

Returns the value of the `SERVER_HELLO` environment variable as plain text.

**Response `200 OK`**
```
Hello, World!
```

**Response `500 Internal Server Error`** — `SERVER_HELLO` is not set.

---

## Running Tests

```bash
uv run pytest
```

With coverage report:

```bash
uv run pytest --cov=app --cov-report=term-missing
```

---

## Docker

**Build the image**

```bash
docker build -t simple-api .
```

**Run the container**

```bash
docker run --rm \
  -e SERVER_HELLO="Hello, World!" \
  -p 8000:8000 \
  simple-api
```

---

## Code Quality

Install [pre-commit](https://pre-commit.com/) hooks:

```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg  # conventional commits
```

Run all checks manually:

```bash
uv run pre-commit run --all-files
```

Checks included:

| Tool | What it checks |
|------|---------------|
| [Ruff](https://docs.astral.sh/ruff/) | Linting and formatting |
| [Bandit](https://bandit.readthedocs.io/) | Security issues in Python code |
| [isort](https://pycqa.github.io/isort/) | Import ordering |
| [uv-lock](https://docs.astral.sh/uv/) | `uv.lock` kept up to date |
| [conventional-pre-commit](https://github.com/compilerla/conventional-pre-commit) | Commit message format |
