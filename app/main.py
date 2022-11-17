from typing import List, Union
from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from passlib.context import CryptContext

from pymongo.database import Database
from fastapi.encoders import jsonable_encoder

from app.models.location import Location
from app.models.election_result import ElectionResult
from app.models.population import Population
from app.models.personal_cvv import PersonalCVV

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

@app.get("/validate_cvv/{citizen_id}/{cvv}", summary="Return response code matching cvv and citizen_id or not")
def check_cvv(citizen_id: int, cvv: str, db: Database=Depends(get_db)):
    db_cvv = db["personal_cvv"]
    user = authenticate_user(db_cvv, citizen_id, cvv)
    if not user:
        return HTTPException(status_code=404, detail=f"Person information not validated")
    return HTTPException(status_code=200, detail=f"Personal information validated!")
