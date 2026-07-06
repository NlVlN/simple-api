import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

hello_msg = os.getenv("SERVER_HELLO")

app = FastAPI()


@app.get("/health-check")
def health_check():
    return {"status": "ok"}


@app.get("/hello-world", response_class=PlainTextResponse)
def hello_world():
    if not hello_msg:
        raise HTTPException(
            status_code=500, detail="SERVER_HELLO environment variable is not set"
        )

    return hello_msg
