from pydantic import BaseModel


class ElectionResultForVoter(BaseModel):
    district: str
    districtTH: str
    province: str
    provinceTH: str
    region: str
    nameOfParliament: str
    nameOfParty: str


response_election_results_voter = {404: {"content": {
    "application/json": {
        "example": {"detail": "No data"}
    }
}}}
