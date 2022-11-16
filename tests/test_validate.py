def test_check_validate(client):
    """Correct params"""
    response = client.post("/api/v1/validate/5432167890123/123")
    assert response.status_code == 200
    assert response.json() == {"validate": True}