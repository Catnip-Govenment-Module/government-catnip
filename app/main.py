from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27018/")
db = client["GovernmentCatnip"]
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
    
@app.get("/api/v1/populations", summary="Return all population with detail", response_model=List[Population])

# async def population(results: Populations):
#      try:
#          db_election_result = results
#          return {
#              "status_code": 200
#          }
#      except:
#          raise HTTPException(status_code=422, detail="Unprocessable Entity")

def populations():
    population = db_populations.find()
    list_population = [l for l in population]
    return list_population

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)