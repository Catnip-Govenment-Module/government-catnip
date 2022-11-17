from pydantic import BaseModel

class ElectionResultForVoter(BaseModel):
    district: str
    districtTH: str
    province: str
    provinceTH: str
    region: str
    nameOfParliament: str
    nameOfParty: str
