# api/auth_router.py
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.repositories import UserRepository
from ..schemas import UserCreate
from ..database.db_init import get_db_session
from hashlib import sha256
from hmac import new, compare_digest
from config import TELEGRAM_SECRET_KEY

router = APIRouter()





@router.post("/auth/telegram")
async def auth_telegram(request: Request, db: AsyncSession = Depends(get_db_session)):
    user_repo = UserRepository(db)

    telegram_data = await request.json()  # Получаем данные из тела запроса
    telegram_auth_data = request.headers.get('Authorization', None)  # Получаем данные из заголовка

    if not telegram_auth_data:
        raise HTTPException(status_code=401, detail="Missing Authorization Header")

    # Предположим, что telegram_auth_data содержит 'telegram_id'
    if "tma" not in telegram_auth_data:  # Проверяем, что Authorization содержит нужный тип аутентификации
        raise HTTPException(status_code=400, detail="Invalid Auth Type")

    # Разделяем значения заголовка на 'tma' и данные
    _, auth_data_raw = telegram_auth_data.split(' ')

    secret_key = sha256(TELEGRAM_SECRET_KEY.encode('utf-8')).digest()
    # Вычисляем HMAC шифрование данных
    hmac_digest = new(secret_key, msg=(auth_data_raw).encode('utf-8'), digestmod=sha256).hexdigest()

    if not compare_digest(hmac_digest, telegram_data['hash']):
        raise HTTPException(status_code=400, detail="Invalid Telegram data")

    # После проверки хеша, структурируем данные полученные от Telegram
    telegram_data_parsed = {**telegram_data}  # TODO: Извлеките нужные данные из telegram_auth_data

    # Предполагаем, что есть метод для поиска пользователя по telegram_id
    existing_user = await user_repo.find_user_by_telegram_id(telegram_data_parsed['telegram_id'])

    if not existing_user:
        user_create = UserCreate(**telegram_data_parsed)  # Преобразование данных в схему создания пользователя
        try:
            new_user = await user_repo.create_user(user_create)
            return {"message": "New user created", "user_id": new_user.id}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    return {"message": "User already exists", "user_id": existing_user.id}