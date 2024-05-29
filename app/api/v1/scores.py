from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.depends import get_db
from app.schemas.score import ScoreCreate, ScoreInDB
from app.crud.score import scores_crud
from app.crud.student import students_crud

router = APIRouter()


@router.get("/{score_id}", response_model=ScoreInDB)
async def get_score(score_id: int, db: AsyncSession = Depends(get_db)):
    try:
        score = await scores_crud.get(db, score_id)
        if not score:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
        return score
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/", response_model=ScoreInDB)
async def create_score(score: ScoreCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_student = await students_crud.get(db, score.student_id)
        if not db_student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        inserted_id = await scores_crud.create(db, score)
        score = await scores_crud.get(db, inserted_id)
        if not score:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found after creation")
        return score
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{score_id}", response_model=ScoreInDB)
async def update_score(score_id: int, score: ScoreCreate, db: AsyncSession = Depends(get_db)):
    try:
        updated_score = await scores_crud.update(db, score_id, score)
        if not updated_score:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
        return updated_score
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{score_id}", response_model=int)
async def delete_score(score_id: int, db: AsyncSession = Depends(get_db)):
    try:
        deleted_id = await scores_crud.delete(db, score_id)
        if not deleted_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
        return deleted_id
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
