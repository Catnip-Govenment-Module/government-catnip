from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    location: str
    population: int
    numberOfVoters: int


response_location = {404: {"content": {
    "application/json": {
        "example": {"detail": "No data"}
    }
}}}
