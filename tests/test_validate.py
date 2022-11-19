def test_check_validate_valid(client, mock_person_cvv, mock_mongo):
    """Correct params"""
    test_check_validate_valid = {
        "citizen_id": 440556794906,
        "cvv": "EC1-3610374-20"
    }
    response = client.post("/validate_cvv/", json=test_check_validate_valid)
    assert response.status_code == 200
    assert response.json() == {"detail": True}

def test_check_validate_incorrect_cvv(client, mock_mongo):
    response = client.post("/validate_cvv/")
    test_check_validate_incorrect_cvv = {
        "citizen_id": 440556794906,
        "cvv": "EC1-3610374-46"
    }
    response = client.post("/validate_cvv/", json=test_check_validate_incorrect_cvv)
    assert response.status_code == 401
    assert response.json() == {"detail": False}

def test_check_validate_not_found_user(client, mock_mongo):
    response = client.post("/validate_cvv/")
    test_check_validate_not_found_user = {
        "citizen_id": 440556794456,
        "cvv": "EC1-3610374-46"
    }
    response = client.post("/validate_cvv/", json=test_check_validate_not_found_user)
    assert response.status_code == 404
    assert response.json() == {"detail": False}
