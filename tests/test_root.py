def test_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }
