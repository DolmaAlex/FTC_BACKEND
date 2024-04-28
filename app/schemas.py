from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    telegram_id: int
    telegram_username: str
    balance: float
    league: str
    experience: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class BoosterBase(BaseModel):
    title: str
    description: str
    price: float
    locked: bool


class BoosterCreate(BoosterBase):
    pass


class Booster(BoosterBase):
    id: int

    class Config:
        orm_mode = True


class PurchaseBase(BaseModel):
    user_id: int
    booster_id: int


class PurchaseCreate(PurchaseBase):
    pass


class Purchase(PurchaseBase):
    id: int
    purchase_date: datetime

    class Config:
        orm_mode = True
