def test_get_location(client, mock_location):
    test_get_all_location = [
        {"locationID": 1,
         "location": "Amphawa",
         "population": 10000,
         "numberOfVoters": 9995
         },
        {"locationID": 2,
         "location": "Bang Len",
         "population": 20000,
         "numberOfVoters": 18995
         }
    ]

    response = client.get("/api/v1/locations")
    assert response.status_code == 200
    assert response.json() == test_get_all_location


def test_get_all_location_but_not_data(client, db_location):
    test_get_location_no_data = {"detail": "No data"}
    response = client.get("/api/v1/locations")
    assert response.status_code == 404
    assert response.json() == test_get_location_no_data
