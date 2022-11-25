from pydantic import BaseModel


class PersonCVV(BaseModel):
    citizenID: int
    citizenCVV: str


response_person_cvv = {
    200: {"content": {
        "application/json": {
            "example": {"detail": True}
        }
    }},
    401: {"content": {
        "application/json": {
            "example": {"detail": False}
        }
    }},
    404: {"content": {
        "application/json": {
            "example": {"detail": False}
        }
    }}
}
