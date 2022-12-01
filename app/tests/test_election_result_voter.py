def test_get_election_result(mock_election_result, mock_district, client):
    test_get_election_result = [
        {
            "district": "Amphawa",
            "districtTH": "อัมพวา",
            "province": "Samut Songkhram",
            "provinceTH": "สมุทรสงคราม",
            "region": "Centre",
            "nameOfParliament": "Jakarin Chujan",
            "nameOfParty": "Catnip"
        },
        {
            "district": "Bang Len",
            "districtTH": "บางเลน",
            "province": "Nakhon Pathom",
            "provinceTH": "นครปฐม",
            "region": "Centre",
            "nameOfParliament": "Chananya Photan",
            "nameOfParty": "Catnip"
        }
    ]

    response = client.get("/api/v1/election-results")
    assert response.status_code == 200
    assert response.json() == test_get_election_result


def test_get_no_election_result(db_election_result, client):
    response = client.get("/api/v1/election-results")
    test_get_no_election_result = {"detail": "No data"}
    assert response.status_code == 404
    assert response.json() == test_get_no_election_result
