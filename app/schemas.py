from pydantic import BaseModel


class UserBase(BaseModel):
    telegram_id: int
    telegram_username: str

    balance: float
    league: str



class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    telegram_id: int | None = None
    telegram_username: str | None = None

    balance: float | None = None
    league: str | None = None





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


class TaskBase(BaseModel):
    title: str
    description: str
    price: float


class TaskCreate(TaskBase):
    title: str
    price: float


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class Admin(BaseModel):
    login: str
    password: str
    class Config:
        orm_mode = True