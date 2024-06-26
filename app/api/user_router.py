# api/user_router.py
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.db_init import get_db_session
from ..repositories.repositories import UserRepository
from ..schemas import UserCreate, User, UserUpdate
import json

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_user(user_create: UserCreate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    new_user = await user_repo.create_user(user_create.dict())
    return new_user


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    user = await user_repo.read_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    update_data = user_update.dict(exclude_none=True)  # exclude_none=True исключит поля со значением None
    user = await user_repo.update_user(user_id, update_data)
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    await user_repo.delete_user(user_id)
    return {"message": "User deleted"}


@router.get("/users/telegram/{telegram_id}")
async def find_user_by_telegram_id(telegram_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    user = await user_repo.find_user_by_telegram_id(telegram_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users/{user_id}/game_state")
async def save_game_state(user_id: int, state_data: dict = Body(...), db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    # Конвертируем словарь обратно в строку JSON для сохранения в базе данных
    json_state_data = json.dumps(state_data)
    await user_repo.save_game_state(user_id, json_state_data)
    return {"message": "Game state saved successfully"}


@router.get("/users/{user_id}/game_state", response_model=str)
async def load_game_state(user_id: int, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)
    state_data = await user_repo.load_game_state(user_id)
    return state_data
