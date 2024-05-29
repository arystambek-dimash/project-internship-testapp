from sqlalchemy import Boolean, Column, ForeignKey, Integer, Date, String
from app.database import Base


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(64), nullable=False, index=True)
    last_name = Column(String(64), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    date_of_join = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
