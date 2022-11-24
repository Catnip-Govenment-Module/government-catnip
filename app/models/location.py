from pydantic import BaseModel


class Location(BaseModel):
    locationID: int
    location: str
    population: int
    numberOfVoters: int


response_location = {404: {"content": {
    "application/json": {
        "example": {"detail": "No data"}
    }
}}}
