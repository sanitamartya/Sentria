from fastapi.testclient import TestClient

from sentria.main import app


client = TestClient(app)


def test_health_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "Sentria"
    assert data["environment"] == "development"
