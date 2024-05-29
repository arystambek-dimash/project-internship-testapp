from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    date_of_join: date
    gender: str


class StudentCreate(StudentBase):
    pass


class StudentInDB(StudentBase):
    id: int

    class Config:
        from_attributes = True
