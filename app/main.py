import os

from fastapi import FastAPI

hello_msg = str(os.getenv("SERVER_HELLO"))

app = FastAPI()

if hello_msg is None:
    raise ValueError("SERVER_HELLO environment variable is not set")


@app.get("/health-check")
def health_check():
    return {"status": "ok"}


@app.get("/hello-world")
def hello_world():
    return hello_msg
