from fastapi import FastAPI
from pymongo import MongoClient
from typing import List
from pydantic import BaseModel
import collections

app = FastAPI()

client = MongoClient("db")
db = client["government_catnip"]
db_election_result = db["election_result"]

@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


class ElectionResult(BaseModel):
    location_id: int
    location: str
    numberOfVotes: int
    nameOfParliament: str 
    nameOfParty: str

# @app.post("/api/v1/election-result")
# async def create_election_result(result: ElectionResult):
#     db_election_result = {}
#     location_id = result.location_id
#     db_election_result[location_id] = result.dict()
#     return {
#         "status": 200
#         }