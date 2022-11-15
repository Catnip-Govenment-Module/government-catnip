import mongomock
import pytest
from fastapi.testclient import TestClient
from app.main import app, get_db

mongo_client = mongomock.MongoClient()
db = mongo_client["government_catnip"]


@pytest.fixture()
def mock_mongo():
    def fake_db():
        return db

    app.dependency_overrides[get_db] = fake_db


@pytest.fixture()
def db_location():
     yield db["location_information"]

@pytest.fixture()
def mock_location(db_location):
    list_mock_location = [
        {
            "location": "Amphawa",
            "location_id": 1,
            "population": 10000,
            "numberOfVoters": 9995
        },
        {
            "location": "Bang Len",
            "location_id": 2,
            "population": 20000,
            "numberOfVoters": 18995
        }
    ]
    db_location.insert_many(list_mock_location)



@pytest.fixture()
def client():
    yield TestClient(app)
