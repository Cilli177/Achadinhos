from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint_returns_service_metadata() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"service": "Achadinhos API", "version": "0.1.0"}


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
