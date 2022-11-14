def test_get_location(mock_mongo, client):
    response = client.get("/api/v1/locations")
    assert response.status_code == 200
    assert response.json() == [
        {
            "location_id": 1,
            "location": "Amphawa",
            "population": 10000,
            "numberOfVoters": 9995
        },
        {
            "location_id": 2,
            "location": "Bang Len",
            "population": 20000,
            "numberOfVoters": 18995
        }
    ]


def test_get_all_location_but_not_data(mock_mongo, client, db_location):
    db_location.delete_many({})
    test_get_location_no_data = {"detail": "No data"}
    response = client.get("/api/v1/locations")
    assert response.status_code == 404
    assert response.json() == test_get_location_no_data
