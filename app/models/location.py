from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    location: str
    population: int
    numberOfVoters: int
