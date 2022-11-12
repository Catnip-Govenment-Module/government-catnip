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

@app.post("/api/v1/election-results")
async def create_election_results(results: List[ElectionResult]):
    result_list = []
    for result in results:
        new_result = collections.OrderedDict()
        new_result['location_id'] = result.location_id
        new_result['location'] = result.location
        new_result['numberOfVotes'] = result.numberOfVotes
        new_result['nameOfParliament'] = result.nameOfParliament
        new_result['nameOfParty'] = result.nameOfParty
        result_list.append(new_result)
    db_election_result.insert_many(result_list)
    return {
        "status": 200
    }

# @app.post("/api/v1/election-result")
# async def create_election_result(result: ElectionResult):
#     db_election_result = {}
#     location_id = result.location_id
#     db_election_result[location_id] = result.dict()
#     return {
#         "status": 200
#         }