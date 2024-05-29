from pydantic import BaseModel


class ScoreBase(BaseModel):
    score: int
    subject: str


class ScoreCreate(ScoreBase):
    student_id: int


class ScoreInDB(ScoreBase):
    id: int
    student_id: int

    class Config:
        from_attributes = True
