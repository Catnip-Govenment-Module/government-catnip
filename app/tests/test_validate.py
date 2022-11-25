def test_check_validate_valid(client, mock_person_cvv, mock_mongo):
    """Correct params"""
    test_check_validate_valid = {
        "citizenID": 440556794906,
        "citizenCVV": "EC1-3610374-20"
    }
    response = client.post("/api/v1/validate-cvv", json=test_check_validate_valid)
    assert response.status_code == 200
    assert response.json() == {"detail": True}


def test_check_validate_incorrect_cvv(client, mock_mongo):
    response = client.post("/api/v1/validate-cvv")
    test_check_validate_incorrect_cvv = {
        "citizenID": 440556794906,
        "citizenCVV": "EC1-3610374-46"
    }
    response = client.post("/api/v1/validate-cvv", json=test_check_validate_incorrect_cvv)
    assert response.status_code == 401
    assert response.json() == {"detail": False}


def test_check_validate_not_found_user(client, mock_mongo):
    test_check_validate_not_found_user = {
        "citizenID": 440556794456,
        "citizenCVV": "EC1-3610374-46"
    }
    response = client.post("/api/v1/validate-cvv", json=test_check_validate_not_found_user)
    assert response.status_code == 404
    assert response.json() == {"detail": False}
