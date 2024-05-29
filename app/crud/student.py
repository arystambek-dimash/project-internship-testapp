from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.student import Students
from app.schemas.student import StudentInDB, StudentCreate


class StudentsCRUD:
    @staticmethod
    async def get(db: AsyncSession, student_id: int = None) -> StudentInDB | List[StudentInDB]:
        if student_id:
            result = await db.execute(select(Students).filter(Students.id == student_id))
            student = result.scalars().first()
            return StudentInDB.from_orm(student) if student else None
        else:
            result = await db.execute(select(Students))
            students = result.scalars().all()
            return [StudentInDB.from_orm(student) for student in students]

    @staticmethod
    async def create(db: AsyncSession, student: StudentCreate) -> int:
        try:
            new_student = Students(**student.dict())
            db.add(new_student)
            await db.commit()
            await db.refresh(new_student)
            return new_student.id
        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def update(db: AsyncSession, student_id: int, student: StudentCreate) -> StudentInDB:
        try:
            result = await db.execute(select(Students).filter(Students.id == student_id))
            db_student = result.scalars().first()
            if db_student:
                for key, value in student.dict().items():
                    setattr(db_student, key, value)
                await db.commit()
                await db.refresh(db_student)
                return StudentInDB.from_orm(db_student)
            return None
        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def delete(db: AsyncSession, student_id: int) -> int:
        try:
            result = await db.execute(select(Students).filter(Students.id == student_id))
            db_student = result.scalars().first()
            if db_student:
                await db.delete(db_student)
                await db.commit()
                return db_student.id
            return None
        except Exception as e:
            await db.rollback()
            raise e


students_crud = StudentsCRUD()
