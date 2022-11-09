# from typing import List
# from uuid import UUID
import uvicorn
from fastapi import FastAPI, HTTPException

from pymongo import MongoClient

# from models.models import Gender, Role, User

app = FastAPI()

client = MongoClient("mongodb://localhost:27018/")
db = client["government_catnip"]
dbLocations = db["location_information"]


# db: List[User] = [
#    User(
#        id="31b6e462-4c9a-4d3d-a00a-e7a8fc43c4e7", 
#        first_name="Jamila", 
#        last_name="Ahmed",
#        gender=Gender.female,
#        roles=[Role.student]
#    ),
#    User(
#        id="03dfb08b-faa6-47fc-b60c-3484a62f8b2a", 
#        first_name="Alex", 
#        last_name="Jones",
#        gender=Gender.male,
#        roles=[Role.admin, Role.user]
#    )
# ]

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
    return list_location


# @app.get("/api/v1/users")
# async def fetch_users():
#    return db;
#
# @app.post("/api/v1/users")
# async def register_user(user: User):
#    db.append(user)
#    return {"id": user.id}
#
# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: UUID):
#        for user in db:
#            if user.id == user_id:
#                db.remove(user)
#                return
#        raise HTTPException(
#            status_code=404,
#            detail=f"user with id: {user_id} does not exists"
#        )
#
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
