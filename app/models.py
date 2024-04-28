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
    balance: Mapped[float] = mapped_column()
    league: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column()
    referral_link: Mapped[str] = mapped_column(String, nullable=True)


class Booster(Base):
    __tablename__ = "boosters"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    locked: Mapped[bool] = mapped_column()


class Purchase(Base):
    __tablename__ = "purchases"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    booster_id: Mapped[int] = mapped_column()
    purchase_date: Mapped[datetime] = mapped_column()
