#from typing import List
#from uuid import UUID
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from passlib.context import CryptContext

#from models.models import Gender, Role, User

app = FastAPI()

client = MongoClient(host="db")
db = client["government_catnip"]
db_cvv = db["personal_cvv"]

async def check_connection_mongodb():
    try:
        client.server_info()
    except Exception:
        raise HTTPException(status_code=500, detail=f"Unable to connect to the server")

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

@app.post("/api/v1/validate/{citizen_id}/{cvv}")
async def check_cvv(citizen_id: int, cvv: str):
    """with given 2 parameters citizen_id and cvv."""
    user = authenticate_user(db_cvv, citizen_id, cvv)
    if not user:
        return False
    return True
