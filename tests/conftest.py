import mongomock
import pytest
from fastapi.testclient import TestClient
from app.main import app, get_db

mongo_client = mongomock.MongoClient()
db = mongo_client["government_catnip"]


@pytest.fixture()
def mock_mongo(db_location):
    def fake_db():
        return db

    app.dependency_overrides[get_db] = fake_db


@pytest.fixture()
def db_location():
    yield db["location_information"]


@pytest.fixture()
def client():
    yield TestClient(app)
