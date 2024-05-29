from fastapi import FastAPI
from app.database import engine, Base, database
from app.api.v1 import scores, students

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(scores.router, prefix="/scores", tags=["scores"])
