from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main(test_app):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }