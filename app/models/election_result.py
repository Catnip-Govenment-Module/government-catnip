from pydantic import BaseModel


class ElectionResult(BaseModel):
    location_id: int
    location: str
    numberOfVoters: int
    nameOfParliament: str
    nameOfParty: str


response_election_results_ec = {
    200: {"content": {
        "application/json": {
            "example": {"detail": "Complete"}
        }
    }}
    , 404: {"content": {
        "application/json": {
            "example": {"detail": "Empty list"}
        }
    }}
}

