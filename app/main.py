from fastapi import FastAPI

from app.database.db_init import create_db_tables

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await create_db_tables()
