from pydantic import BaseModel


class UserBase(BaseModel):
    telegram_id: int
    telegram_username: str
<<<<<<< HEAD
    balance: float
    league: str
=======
>>>>>>> 97c4499afa221f6d85aa424ef6da47003fc496ef


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    telegram_id: int | None = None
    telegram_username: str | None = None
<<<<<<< HEAD
    balance: float | None = None
    league: str | None = None
=======

>>>>>>> 97c4499afa221f6d85aa424ef6da47003fc496ef


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
<<<<<<< HEAD
        orm_mode = True
=======
        orm_mode = True
>>>>>>> 97c4499afa221f6d85aa424ef6da47003fc496ef
