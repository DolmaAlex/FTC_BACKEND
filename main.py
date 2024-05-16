from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.declarative import declarative_base

from app.admin_auth import AdminAuth
from app.database.db_init import engine, create_db_tables
from app.models import User, Booster, Task
from app.api.user_router import router as user_router
from app.api.booster_router import router as booster_router
from app.api.task_router import router as task_router

app = FastAPI(title="Your Project Title")

authentication_backend = AdminAuth(secret_key="verysecretkey")
admin = Admin(app, engine, authentication_backend=authentication_backend)


class UserAdmin(ModelView, model=User):
    column_list = ["id", "telegram_id", "telegram_username", "balance", "league"]


class BoosterAdmin(ModelView, model=Booster):
    column_list = ["id", "title", "description", "price"]


class TaskAdmin(ModelView, model=Task):
    column_list = ["id", "title", "description", "price"]


admin.add_view(UserAdmin)
admin.add_view(BoosterAdmin)
admin.add_view(TaskAdmin)


@app.on_event("startup")
async def startup_event():
   await create_db_tables()  # Это вызовет создание таблиц на старте приложения


app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(booster_router, prefix="/boosters", tags=["boosters"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])