# Hello API

Simple REST API built with **FastAPI**.

## Endpoints

* `GET /health-check` → `{"status":"ok"}`
* `GET /hello-world` → returns the value of the `SERVER_HELLO` environment variable

## Quality checks

```bash
uv run pre-commit run --all-files
```
