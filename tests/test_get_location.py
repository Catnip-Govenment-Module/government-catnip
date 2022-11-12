def test_get_location(client):
    response = client.get("/api/v1/locations")
    assert response.status_code == 200

