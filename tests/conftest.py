import mongomock
import pytest
from fastapi.testclient import TestClient
from app.main import app, get_db

mongo_client = mongomock.MongoClient()
db = mongo_client["government_catnip"]


@pytest.fixture()
def mock_mongo(db_location):
    mock_location = [
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
    db_location.insert_many(mock_location)

    def fake_db():
        return db

    app.dependency_overrides[get_db] = fake_db


@pytest.fixture()
def db_location():
    yield db["location_information"]
