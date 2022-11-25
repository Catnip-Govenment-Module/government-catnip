def test_get_population_endpoint(mock_mongo, mock_population, client):
    response = client.get("/api/v1/populations")
    assert response.status_code == 200
    assert response.json() == [
   {
        "citizen_id": 4569871354123,
        "title": "Mr.",
        "firstName": "Anuman",
        "lastName": "Saengthong",
        "sex": "Male",
        "locationID": 557,
        "rightToVote": True,
        "blackList": False
    },
    {
        "citizen_id": 1234567898765,
        "title": "Ms.",
        "firstName": "Achara",
        "lastName": "Sukkasem",
        "sex": "Female",
        "locationID": 231,
        "rightToVote": True,
        "blackList": False
    }
    ]

def test_get_all_population_but_not_data(mock_mongo, client, db_population):
    db_population.delete_many({})
    test_get_population_no_data = {"detail": "No data"}
    response = client.get("/api/v1/populations")
    assert response.status_code == 404
    assert response.json() == test_get_population_no_data
