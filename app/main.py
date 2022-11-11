import uvicorn
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb://localhost:27018/")
db = client["government_catnip"]
db_populations = db["personal_information"]

@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }


class Population(BaseModel):
    _id: int
    title: str
    firstName: str
    lastName: str
    sex: str
    locationID: int
    rightToVote: bool
    blackList: bool

class Population_p(BaseModel):
    detail: List[Population]

@app.get("/api/v1/populations")
async def all_pop():
    try:
        population = db_populations.find()
        list_population = [l for l in population]
        return list_population
    except:
        raise HTTPException()