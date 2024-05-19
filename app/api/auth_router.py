# api/auth_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.repositories import UserRepository  # исправлен импорт
from ..schemas import UserCreate
from ..database.db_init import get_db_session

router = APIRouter()


@router.post("/auth/telegram")
async def auth_telegram(telegram_data: dict, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)

    # Обработка данных от Telegram и их проверка здесь...
    # Например, предположим, что telegram_data содержит 'telegram_id'

    # Проверяем, существует ли уже пользователь с таким telegram_id
    existing_user = await user_repo.find_user_by_telegram_id(telegram_data['telegram_id'])

    if not existing_user:
        # Если пользователя нет, создаем нового
        user_create = UserCreate(**telegram_data)  # Преобразование данных Telegram в схему UserCreate
        new_user = await user_repo.create_user(user_create.dict())
        return {"message": "New user created", "user_id": new_user.id}

    return {"message": "User already exists", "user_id": existing_user.id}