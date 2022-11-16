def test_get_election_result(mock_mongo, mock_election_result, client):
    test_get_election_result = [
        {
            "location_id": 1,
            "location": "Bang Len",
            "numberOfVoters": 200,
            "nameOfParliament": "Chananya Photan", 
            "nameOfParty": "Catnip"
        },
        {
            "location_id": 2,
            "location": "Amphawa",
            "numberOfVoters": 200,
            "nameOfParliament": "Jakarin Chujan", 
            "nameOfParty": "Catnip"
        }
    ]


    response = client.get("/api/v1/election-results")
    assert response.status_code == 200
    assert response.json() == test_get_election_result

def test_get_no_election_result(mock_mongo, db_election_result, client):
    db_election_result.delete_many({})
    response = client.get("/api/v1/election-results")
    test_get_no_election_result = {"detail": "No data"}
    assert response.status_code == 404
    assert response.json() == test_get_no_election_result