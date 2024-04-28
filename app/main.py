from fastapi import FastAPI
from .api.user_router import router as user_router
from .database.db_init import create_db_tables

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await create_db_tables()  #


app.include_router(user_router, tags=['users'])
