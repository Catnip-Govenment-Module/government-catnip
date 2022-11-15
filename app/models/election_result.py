from pydantic import BaseModel

class ElectionResult(BaseModel):
    location_id: int
    location: str
    numberOfVotes: int
    nameOfParliament: str 
    nameOfParty: str