def test_population_endpoint(client):
    response = client.get("/api/v1/populations")
    assert response.status_code == 200

def test_invalid_id1(client):
    response = client.get("/fruit/99")
    assert response.status_code == 404
    
