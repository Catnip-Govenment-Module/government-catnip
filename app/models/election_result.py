from pydantic import BaseModel

class ElectionResult(BaseModel):
    location_id: int
    location: str
    numberOfVoters: int
    nameOfParliament: str 
    nameOfParty: str
