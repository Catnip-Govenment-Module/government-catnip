from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_population_endpoint():
    response = client.get("/api/v1/populations")
    assert response.status_code == 200

def test_invalid_id1():
    response = client.get("/fruit/99")
    assert response.status_code == 404
    
