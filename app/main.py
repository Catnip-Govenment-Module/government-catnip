from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from passlib.context import CryptContext

from pymongo.database import Database
from fastapi.encoders import jsonable_encoder

from app.models.location import Location
from app.models.election_result import ElectionResult
from app.models.population import Population

from app.models.election_result_voter import ElectionResultForVoter
from app.models.person_cvv import Person_cvv


from pydantic import BaseModel

app = FastAPI()

async def get_db():
    client = await check_connect_mongodb()
    db = client["government_catnip"]
    return db


async def check_connect_mongodb():
    try:
        client = MongoClient(host="db")
        client.server_info()
    except Exception:
        raise HTTPException(status_code=500, detail=f"Unable to connect to the server")
    return client


async def get_district(db):
    db_district = db["district"]
    dt = db_district.find({}, {"_id": 0})
    dt_list = [q for q in dt]
    return dt_list

@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


async def verify_password(cvv, hashed_cvv):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(cvv, hashed_cvv)

async def authenticate_user(collection_users, citizen_id: str, cvv: str):
    user = collection_users.find_one({"citizen_id": citizen_id}, {"_id":0})
    if not user:
        raise HTTPException(status_code=404, detail=False)
    if not await verify_password(cvv, user["cvv"]):
        raise HTTPException(status_code=401, detail=False)

@app.post("/validate_cvv/", summary="Return response code matching cvv and citizen_id or not")
async def check_cvv(person_cvv:Person_cvv, db: Database=Depends(get_db)):
    db_cvv = db["personal_cvv"]
    await authenticate_user(db_cvv, person_cvv.citizen_id, person_cvv.cvv)
    return {"detail": True}
    
@app.get("/api/v1/election-results", summary="Return the election results", response_model=List[ElectionResultForVoter])
async def election_result(db: Database = Depends(get_db)):
  db_election_result = db["election_result"]
  # Check that the election results are empty or not
  if db_election_result.count_documents({}) > 0:
    list_district =  await get_district(db)
    new_election_result = []
    list_results = list(db_election_result.find({}, {"_id": 0}))
    for election in list_results:
        for district in list_district:
            # Check location_id from election result and district_id from district
            if district["district_id"] == election["location_id"]:
                # Create new election results for voter
                new_result = {
                    "district": district["district"],
                    "districtTH": district["districtTH"],
                    "province": district["province"],
                    "provinceTH": district["provinceTH"],
                    "region": district["region"],
                    "nameOfParliament": election["nameOfParliament"],
                    "nameOfParty": election["nameOfParty"],
                }
                new_election_result.append(new_result)
    if new_election_result:
        return new_election_result
  raise HTTPException(status_code=404, detail=f"No data")

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
