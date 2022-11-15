from pydantic import BaseModel


class Population(BaseModel):
    _id: int
    title: str
    firstName: str
    lastName: str
    sex: str
    locationID: int
    rightToVote: bool
    blackList: bool