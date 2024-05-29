from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.score import scores_crud
from app.depends import get_db
from app.schemas.score import ScoreInDB
from app.schemas.student import StudentInDB, StudentCreate
from app.crud.student import students_crud

router = APIRouter()


@router.get("/", response_model=List[StudentInDB])
async def get_students(db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    try:
        students = await students_crud.get(db)
        return students[skip:skip + limit]
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/", response_model=StudentInDB)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    try:
        inserted_id = await students_crud.create(db, student)
        student = await students_crud.get(db, inserted_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found after creation")
        return student
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


class StudentWithScores(StudentInDB):
    scores: List[ScoreInDB]


@router.get("/{student_id}", response_model=StudentWithScores)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    try:
        student = await students_crud.get(db, student_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

        scores = await scores_crud.get(db, student_id=student_id)
        return StudentWithScores(**student.dict(), scores=scores)
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.patch("/{student_id}", response_model=StudentInDB)
async def update_student(student_id: int, student: StudentCreate, db: AsyncSession = Depends(get_db)):
    try:
        updated_student = await students_crud.update(db, student_id, student)
        if not updated_student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return updated_student
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{student_id}", response_model=int)
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    try:
        deleted_id = await students_crud.delete(db, student_id)
        if not deleted_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return deleted_id
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
