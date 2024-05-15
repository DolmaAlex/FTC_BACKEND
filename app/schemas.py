from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    telegram_id: int
    telegram_username: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    telegram_id: int | None = None
    telegram_username: str | None = None



class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class BoosterBase(BaseModel):
    title: str
    description: str
    price: float


class BoosterCreate(BoosterBase):
    title: str
    description: str
    price: float


class Booster(BoosterBase):
    id: int

    class Config:
        orm_mode = True
