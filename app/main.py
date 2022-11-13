#from typing import List
#from uuid import UUID
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

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

@app.post("/api/v1/validate/{citizen_id}/{cvv}")
async def check_cvv(citizen_id: int, cvv: str):
    ID_LENGTH = 13
    CVV_LENGTH = 64
    if len(str(citizen_id)) > ID_LENGTH or len(cvv) > CVV_LENGTH:
        return {"validate": False}
    user = db_cvv.find_one({"_id": citizen_id})
    if user:
        get_cvv = db_cvv.find_one({"_id": citizen_id, "cvv": cvv})
        if get_cvv:
            return {"validate": True}
    return {"validate": False}
