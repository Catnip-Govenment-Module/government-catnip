import asyncio
import uvicorn
import os

from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from passlib.context import CryptContext

from fastapi.encoders import jsonable_encoder
from pymongo.collection import Collection
from pymongo.database import Database

from models.location import Location, response_location
from models.election_result import ElectionResult, response_election_results_ec
from models.person_cvv import PersonCVV, response_person_cvv
from models.population import Population, response_population
from models.election_result_voter import ElectionResultForVoter, response_election_results_voter

app = FastAPI()
port = int(os.environ.get("PORT", 5000))

async def get_db():
    client = await check_connect_mongodb()
    db = client["government_catnip"]
    return db


async def check_connect_mongodb():
    try:
        client = MongoClient(host="mongodb+srv://catnip:catnip2022@governmentcatnip.6loikcf.mongodb.net/test")
        client.server_info()
    except Exception:
        raise HTTPException(status_code=500, detail=f"Unable to connect to the server")
    return client


async def get_district(db: Database):
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


async def verify_password(cvv: str, hashed_cvv: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(cvv, hashed_cvv)


async def authenticate_user(collection_users: Collection, citizen_id: int, cvv: str):
    user = collection_users.find_one({"citizen_id": citizen_id}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail=False)
    if not await verify_password(cvv, user["cvv"]):
        raise HTTPException(status_code=401, detail=False)


@app.post("/api/v1/validate-cvv", summary="Return response code matching cvv and citizen_id or not",
          responses=response_person_cvv)
async def check_cvv(person_cvv: PersonCVV, db: Database = Depends(get_db)):
    db_cvv = db["personal_cvv"]
    await authenticate_user(db_cvv, person_cvv.citizen_id, person_cvv.cvv)
    return {"detail": True}


@app.get("/api/v1/election-results", summary="Return the election results", response_model=List[ElectionResultForVoter],
         responses=response_election_results_voter)
async def election_result(db: Database = Depends(get_db)):
    db_election_result = db["election_result"]
    # Check that the election results are empty or not
    if db_election_result.count_documents({}) > 0:
        list_district = await get_district(db)
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
    raise HTTPException(status_code=404, detail="No data")


@app.post("/api/v1/election-results", summary="Create Election results", responses=response_election_results_ec)
async def create_election_results(results: List[ElectionResult], db: Database = Depends(get_db)):
    db_election_result = db["election_result"]
    result_list = jsonable_encoder(results)
    if result_list:
        db_election_result.insert_many(result_list)
        return {"detail": "Complete"}
    raise HTTPException(status_code=404, detail="The information sent is an empty list")


@app.get("/api/v1/locations", summary="Return all location with detail", response_model=List[Location],
         responses=response_location)
async def locations(db: Database = Depends(get_db)):
    db_locations = db["location_information"]
    location = db_locations.find({}, {"_id": 0})
    list_location = [l for l in location]
    if list_location:
        return list_location
    raise HTTPException(status_code=404, detail="No data")


@app.get("/api/v1/populations", description='populations information', response_model=List[Population],
         responses=response_population)
async def all_population_info(db: Database = Depends(get_db)):
    db_population = db["personal_information"]
    populations = db_population.find({}, {"_id": 0})
    list_population = [population for population in populations]
    if list_population:
        return list_population
    raise HTTPException(status_code=404, detail="No data")


async def main():
    config = uvicorn.Config("main:app", log_level="info", host="0.0.0.0", port=port)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
