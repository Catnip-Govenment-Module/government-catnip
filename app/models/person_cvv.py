from pydantic import BaseModel


class Person_cvv(BaseModel):
    citizen_id: int
    cvv: str
