from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.score import Score
from app.schemas.score import ScoreInDB, ScoreCreate


class ScoresCRUD:
    @staticmethod
    async def get(db: AsyncSession, score_id: int = None, student_id: int = None) -> ScoreInDB | List[ScoreInDB] | None:
        if student_id is not None and score_id is None:
            result = await db.execute(select(Score).filter(Score.student_id == student_id))
            scores = result.scalars().all()
            return [ScoreInDB.from_orm(score) for score in scores]
        elif score_id is not None and student_id is None:
            result = await db.execute(select(Score).filter(Score.id == score_id))
            score = result.scalars().first()
            return ScoreInDB.from_orm(score) if score else None
        return None

    @staticmethod
    async def create(db: AsyncSession, score: ScoreCreate) -> int:
        try:
            new_score = Score(**score.dict())
            db.add(new_score)
            await db.commit()
            await db.refresh(new_score)
            return new_score.id
        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def update(db: AsyncSession, score_id: int, score: ScoreCreate) -> ScoreInDB:
        try:
            result = await db.execute(select(Score).filter(Score.id == score_id))
            db_score = result.scalars().first()
            if db_score:
                for key, value in score.dict().items():
                    setattr(db_score, key, value)
                await db.commit()
                await db.refresh(db_score)
                return ScoreInDB.from_orm(db_score)
            return None
        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def delete(db: AsyncSession, score_id: int) -> int:
        try:
            result = await db.execute(select(Score).filter(Score.id == score_id))
            db_score = result.scalars().first()
            if db_score:
                await db.delete(db_score)
                await db.commit()
                return db_score.id
            return None
        except Exception as e:
            await db.rollback()
            raise e


scores_crud = ScoresCRUD()
