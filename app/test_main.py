from django.http import response
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }

def test_check_validate():
    response = client.post("/api/v1/validate/4569871354123/267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3")
