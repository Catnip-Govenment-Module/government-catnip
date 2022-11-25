import mongomock
import pytest
from fastapi.testclient import TestClient
from main import app, get_db

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
            "locationID": 1,
            "location": "Amphawa",
            "population": 10000,
            "numberOfVoters": 9995
        },
        {
            "locationID": 2,
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
            "citizenID": 4569871354123,
            "title": "Mr.",
            "firstName": "Anuman",
            "lastName": "Saengthong",
            "sex": "Male",
            "locationID": 557,
            "rightToVote": True,
            "blacklist": False
        },
        {
            "citizenID": 1234567898765,
            "title": "Ms.",
            "firstName": "Achara",
            "lastName": "Sukkasem",
            "sex": "Female",
            "locationID": 231,
            "rightToVote": True,
            "blacklist": False
        }])


@pytest.fixture()
def db_election_result():
    yield db["election_result"]


@pytest.fixture()
def db_district():
    yield db["district"]


@pytest.fixture()
def mock_district(db_district):
    db_district.insert_many([
        {
            "districtID": 1,
            "district": "Amphawa",
            "districtTH": "อัมพวา",
            "province": "Samut Songkhram",
            "provinceTH": "สมุทรสงคราม",
            "region": "Centre"
        },
        {
            "districtID": 2,
            "district": "Bang Len",
            "districtTH": "บางเลน",
            "province": "Nakhon Pathom",
            "provinceTH": "นครปฐม",
            "region": "Centre"
        }
    ])


@pytest.fixture()
def db_personal_cvv():
    yield db["personal_cvv"]


@pytest.fixture()
def mock_person_cvv(db_personal_cvv):
    db_personal_cvv.insert_many([
        {
            "citizenID": 440556794906,
            "citizenCVV": "$2b$12$xFOUTVJjht350Ik7D1eQhOB1yB0/yog4etgEbn4aDk3Jf3CT65rm."
        },
        {
            "citizenID": 173518749711,
            "citizenCVV": "$2b$12$UHsLQtJ5hit1XZyEYHo9IO.61aDeJV/rdc1/mp35OwJKcISe.hN0W"
        }
    ])


@pytest.fixture()
def client():
    yield TestClient(app)

