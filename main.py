from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.declarative import declarative_base
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

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
    column_list = ["id", "title", "description", "cost"]


class TaskAdmin(ModelView, model=Task):
    column_list = ["id", "title", "description", "price"]


admin.add_view(UserAdmin)
admin.add_view(BoosterAdmin)
admin.add_view(TaskAdmin)

origins = ["https://firsttapbeta.web.app", "https://ftc-coin-bot.onrender.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Добавляем созданный класс middleware


# Включение роутеров
app.include_router(user_router, tags=["users"])
app.include_router(booster_router, tags=["boosters"])
app.include_router(task_router, tags=["tasks"])
