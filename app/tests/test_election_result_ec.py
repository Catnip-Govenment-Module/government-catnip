def test_post_json_with_wrong_format(db_election_result, client):
    response = client.post(
        "/api/v1/election-results",
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 422


def test_post_json(db_election_result, client):
    response = client.post(
        "/api/v1/election-results", json={
            "locationID": 1,
            "location": "Amphawa",
            "numberOfVoters": 9900,
            "nameOfParliament": "Jakarin Chujan",
            "nameOfParty": "Catnip"

        }
    )
    assert response.status_code == 422


def test_post_form_no_body(db_election_result, client):
    response = client.post("/api/v1/election-results")
    assert response.status_code == 422


def test_post_election_result(db_election_result, client):
    data = [
        {
            "locationID": 1,
            "location": "Amphawa",
            "numberOfVoters": 9900,
            "nameOfParliament": "Jakarin Chujan",
            "nameOfParty": "Catnip"

        },
        {
            "locationID": 2,
            "location": "Bang Len",
            "numberOfVoters": 9900,
            "nameOfParliament": "Chananya Photan",
            "nameOfParty": "Catnip"
        }
    ]
    response = client.post(
        "/api/v1/election-results",
        json=data
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Complete"}


def test_post_empty_list(db_election_result, client):
    response = client.post(
        "/api/v1/election-results",
        json=[]
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'The information sent is an empty list'}
