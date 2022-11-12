from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_election_result_bad_request():
    response = client.post(
        "/api/v1/election-results",
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 422

def test_post_election_result_single_json_request():
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

def test_post_form_no_body():
    response = client.post("/api/v1/election-results")
    assert response.status_code == 422

def test_post_election_result_pass_request():
    data = [
            {
                "location_id": 1,
                "location": "Amphawa",
                "numberOfVotes": 9900,
                "nameOfParliament": "Jakarin Chujan",
                "nameOfParty": "Catnip"
                
            }
            # {
            #     "location_id": 2,
            #     "location": "Bang Len",
            #     "numberOfVotes": 9900,
            #     "nameOfParliament": "Chananya Photan", 
            #     "nameOfParty": "Catnip"
            # }
        ]
    response = client.post(
        "/api/v1/election-results",
        data=data
    )
    assert response.status_code == 200