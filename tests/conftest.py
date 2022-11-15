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
    db_location.insert_many([
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
])

@pytest.fixture()
def db_population():
    yield db["personal_information"]

@pytest.fixture()
def mock_population(db_population):
    db_population.insert_many([
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
    }])


@pytest.fixture()
def client():
    yield TestClient(app)
