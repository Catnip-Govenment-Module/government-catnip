from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient

from passlib.context import CryptContext

from pymongo.database import Database
from fastapi.encoders import jsonable_encoder

from app.models.location import Location
from app.models.election_result import ElectionResult
from app.models.population import Population



app = FastAPI()


client = MongoClient(host="db")
db = client["government_catnip"]
db_cvv = db["personal_cvv"]

async def check_connection_mongodb():
    try:
        client.server_info()
    except Exception:
        raise HTTPException(status_code=500, detail=f"Unable to connect to the server")


@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(collection_users, citizen_id: str, password: str):
    user = collection_users.find_one({"_id": citizen_id}, {"cvv": 1})
    if not user:
        return False
    if not verify_password(password, user["cvv"]):
        return False
    return user

@app.post("/{parameter}")
def simple(parameter: BaseModel, permission: bool = Depends(verify_password)):
async def check_cvv(citizen_id: int, cvv: str):
    """with given 2 parameters citizen_id and cvv."""
    user = authenticate_user(db_cvv, citizen_id, cvv)
    if not user:
        return False
    return True

@app.post("/api/v1/election-results")
async def create_election_results(results: List[ElectionResult], db: Database = Depends(get_db)):
    db_election_result = db["election_result"]
    result_list = jsonable_encoder(results)
    if result_list:
        db_election_result.insert_many(result_list)
        return {"detail": "Complete"}
    return {"detail": "Empty list"}


@app.get("/api/v1/locations", summary="Return all location with detail", response_model=List[Location])
async def locations(db: Database = Depends(get_db)):
    dbLocations = db["location_information"]
    location = dbLocations.find({}, {"_id": 0})
    list_location = [l for l in location]
    if list_location:
        return list_location
    raise HTTPException(status_code=404, detail="No data")


@app.get("/api/v1/populations", description='populations information', response_model=List[Population])
async def all_population_info(db: Database = Depends(get_db)):
    dbpopulation = db["personal_information"]
    populations = dbpopulation.find({}, {"_id": 0})
    list_population = [l for l in populations]
    if list_population:
        return list_population
    raise HTTPException(status_code=404, detail="No data")

