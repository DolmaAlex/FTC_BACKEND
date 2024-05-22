from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Float, Boolean, BigInteger, ForeignKey, DateTime
from datetime import datetime

Base = declarative_base()


class GameState(Base):
    __tablename__ = "game_states"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'), unique=True)
    state_data: Mapped[str] = mapped_column()  # JSON-строка с данными состояния игры
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, type_=DateTime)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    telegram_username: Mapped[str] = mapped_column(String)
    telegram_firstame: Mapped[str] = mapped_column(String)
    photo_url: Mapped[str] = mapped_column(String)
    balance: Mapped[float] = mapped_column()
    league: Mapped[str] = mapped_column()


class Booster(Base):
    __tablename__ = "boosters"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    cost: Mapped[int] = mapped_column()


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()


class Admin(Base):
    __tablename__ = "admins"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
