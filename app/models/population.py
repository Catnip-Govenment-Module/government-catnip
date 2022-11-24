from pydantic import BaseModel


class Population(BaseModel):
    citizenID: int
    title: str
    firstName: str
    lastName: str
    sex: str
    locationID: int
    rightToVote: bool
    blackList: bool


response_population = {404: {"content": {
    "application/json": {
        "example": {"detail": "No data"}
    }
}}}
