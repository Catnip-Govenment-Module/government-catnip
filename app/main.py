#from typing import List
#from uuid import UUID
from fastapi import FastAPI, HTTPException
#from pymongo import MongoClient

#from models.models import Gender, Role, User

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

@app.get("/api/v1/populations",description='populations information')
async def all_pop():
    try:
        population = db_populations.find()
        list_population = [l for l in population]
        return list_population
    except:
        raise HTTPException(status_code=422)