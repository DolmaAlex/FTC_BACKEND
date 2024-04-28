from fastapi import FastAPI
from .api.user_router import router as user_router
from .api.booster_router import router as booster_router
from .database.db_init import create_db_tables

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await create_db_tables()  #


app.include_router(user_router, tags=['users'])
app.include_router(booster_router, tags=["boosters"])
