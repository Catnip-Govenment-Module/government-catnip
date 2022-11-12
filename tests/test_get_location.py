from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_location(test_app):
    response = client.get("/api/v1/locations")
    assert response.status_code == 200

