def test_post_json_with_wrong_format(mock_mongo, client):
     response = client.post(
         "/api/v1/election-results",
         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
     )
     assert response.status_code == 422

def test_post_json(mock_mongo, client):
    response = client.post(
        "/api/v1/election-results", json={
            "location_id": 1,
            "location": "Amphawa",
            "numberOfVotes": 9900,
            "nameOfParliament": "Jakarin Chujan",
            "nameOfParty": "Catnip"

        }
    )
    assert response.status_code == 422

def test_post_form_no_body(mock_mongo, client):
    response = client.post("/api/v1/election-results")
    assert response.status_code == 422

def test_post_election_result(mock_mongo, client):
    data = [
            {
                "location_id": 1,
                "location": "Amphawa",
                "numberOfVotes": 9900,
                "nameOfParliament": "Jakarin Chujan",
                "nameOfParty": "Catnip"

            },
            {
                "location_id": 2,
                "location": "Bang Len",
                "numberOfVotes": 9900,
                "nameOfParliament": "Chananya Photan", 
                "nameOfParty": "Catnip"
            }
        ]
    response = client.post(
        "/api/v1/election-results",
        json=data
    )
    assert response.status_code == 200

def test_post_empty_list(mock_mongo, client):
    response = client.post(
        "/api/v1/election-results",
        json=[]
    )
    assert response.status_code == 200
