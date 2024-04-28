# api/user_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.db_init import get_db_session
from ..repositories.repositories import UserRepository
from ..schemas import UserCreate, User, UserUpdate

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
