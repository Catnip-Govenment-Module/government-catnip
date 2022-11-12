from typing import List
# from uuid import UUID
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

client = MongoClient(host="db")
db = client["government_catnip"]
dbLocations = db["location_information"]


@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


@app.get("/api/v1/locations", summary="Return all location with detail")
def locations():
    location = dbLocations.find()
    list_location = [l for l in location]
    if list_location:
        return list_location
    raise HTTPException(status_code=404, detail="No data in database")
