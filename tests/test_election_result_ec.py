def test_post_json_with_wrong_format(client):
     response = client.post(
         "/api/v1/election-results",
         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
     )
     assert response.status_code == 422

def test_post_json(client):
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

def test_post_form_no_body(client):
    response = client.post("/api/v1/election-results")
    assert response.status_code == 422

def test_post_election_result_pass_request(client):
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