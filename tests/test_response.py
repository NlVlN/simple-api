from fastapi.testclient import TestClient

from app import main


def test_hello_world_plaintext():
    SERVER_HELLO = "Hello, World!"
    main.hello_msg = SERVER_HELLO
    client = TestClient(main.app)
    resp = client.get("/hello-world")
    assert resp.status_code == 200
    # content-type may include charset, check main type
    assert resp.headers.get("content-type", "").split(";")[0] == "text/plain"
    assert isinstance(resp.text, str)


def test_health_check_json():
    client = TestClient(main.app)
    resp = client.get("/health-check")
    assert resp.status_code == 200
    assert resp.headers.get("content-type", "").split(";")[0] == "application/json"
    data = resp.json()
    assert isinstance(data, dict)
