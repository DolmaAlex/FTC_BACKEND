from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Float, Boolean, BigInteger, ForeignKey, DateTime
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    telegram_username: Mapped[str] = mapped_column(String)
<<<<<<< HEAD
    balance: Mapped[float] = mapped_column()
    league: Mapped[str] = mapped_column()
=======
>>>>>>> 97c4499afa221f6d85aa424ef6da47003fc496ef


class Booster(Base):
    __tablename__ = "boosters"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
