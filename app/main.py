#from typing import List
#from uuid import UUID
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

#from models.models import Gender, Role, User

app = FastAPI()

# fake_election_db = [
#     {
#      "location": "Location 1",	#  เขตพื้นที่
#      "location_id": 1, 
#      "numberOfVoters": 150,  # จำนวนของคนที่มีสิทธิ์ Vote
#      "nameOfParliament": "", # name of MP
#      "nameOfParty": "",
#     },
# ]

# fake_election_db = [

# ]

client = MongoClient(host="db")
db = client["government_catnip"]
db_election_result = db["election_result"]
# db_election_result = fake_election_db


#db: List[User] = [
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
#]

@app.get("/")
async def root():
    return {
        "message": "Sup for our documentation go to link variable",
        "link": "https://catnip-govenment-module.github.io/government-catnip"
    }
    
@app.get("/election-results")
async def election_result():
  if db_election_result.count() > 0:
    election = db_election_result.find()
    list_election_result = [i for i in election]
    return list_election_result
  else:
    raise HTTPException(
           status_code=404,
           detail=f"The election results were empty."
    )

#@app.get("/api/v1/users")
#async def fetch_users():
#    return db;
#
#@app.post("/api/v1/users")
#async def register_user(user: User):
#    db.append(user)
#    return {"id": user.id}
#
#@app.delete("/api/v1/users/{user_id}")
#async def delete_user(user_id: UUID):
#        for user in db:
#            if user.id == user_id:
#                db.remove(user)
#                return
#        raise HTTPException(
#            status_code=404,
#            detail=f"user with id: {user_id} does not exists"
#        )
#