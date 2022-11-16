from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from pymongo.database import Database
from fastapi.encoders import jsonable_encoder

from app.models.location import Location
from app.models.election_result import ElectionResult

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


@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


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
