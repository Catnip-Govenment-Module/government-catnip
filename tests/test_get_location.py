def test_get_location(test_app):
    response = test_app.get("/api/v1/locations")
    assert response.status_code == 200

