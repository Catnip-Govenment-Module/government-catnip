def test_check_validate(client):
    """Correct params"""
    response = client.post("/api/v1/validate/4569871354123/267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3")
    assert response.status_code == 200
    assert response.json() == {"validate": True}

def test_none_citizen_id(client):
    response = client.post("/api/v1/validate/267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3")
    assert response.status_code == 404

def test_wrong_citizen_id(client):
    response = client.post("/api/v1/validate/100000000/267d303819c7fa1c19716d44316e8a1d63f4a76fdeca8aa337d5215d60dca0f3")
    assert response.status_code == 200
    assert response.json() == {"validate": False}

def test_wrong_cvv(client):
    response = client.post("/api/v1/validate/1234567898765/e192ab76c7830b54f5d70e09ed920511f5f2f1afc468f5379ded05fdd71ab6a51231wf")
    assert response.status_code == 200
    assert response.json() == {"validate": False}
