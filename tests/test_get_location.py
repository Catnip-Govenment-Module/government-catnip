def test_get_location(mock_mongo, client, mock_location):
    test_get_all_location = [
        {
            "location": "Amphawa",
            "location_id": 1,
            "population": 10000,
            "numberOfVoters": 9995
        },
        {
            "location": "Bang Len",
            "location_id": 2,
            "population": 20000,
            "numberOfVoters": 18995
        }
    ]
    
    response = client.get("/api/v1/locations")
    assert response.status_code == 200
    assert response.json() == test_get_all_location


def test_get_all_location_but_not_data(mock_mongo, client, db_location):
    db_location.delete_many({})
    test_get_location_no_data = {"detail": "No data"}
    response = client.get("/api/v1/locations")
    assert response.status_code == 404
    assert response.json() == test_get_location_no_data
