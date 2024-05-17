# api/booster_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.db_init import get_db_session
from ..repositories.repositories import UserRepository
from ..schemas import BoosterCreate, Booster
from typing import List

router = APIRouter()


@router.post("/boosters/", response_model=Booster)
async def create_booster(booster: BoosterCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.create_booster(booster.dict())


@router.get("/boosters/{booster_id}", response_model=Booster)
async def get_booster(booster_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.get_booster(booster_id)


@router.put("/boosters/{booster_id}", response_model=Booster)
async def update_booster(booster_id: int, booster: BoosterCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.update_booster(booster_id, booster.dict())


@router.get("/boosters/", response_model=List[Booster])
async def get_all_boosters(db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    return await user_repo.get_all_boosters()
