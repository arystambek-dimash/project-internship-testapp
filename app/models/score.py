# app/models/score.py
from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    subject = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))
