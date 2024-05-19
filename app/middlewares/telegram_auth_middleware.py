# middlewares/telegram_auth_middleware.py

from fastapi import Request, HTTPException
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
from config import TELEGRAM_SECRET_KEY


async def telegram_auth_middleware(request: Request, call_next):
    # Фильтр запросов только для эндпоинта авторизации Telegram
    if '/auth/telegram' in str(request.url):
        telegram_data = request.query_params
        telegram_hash = telegram_data.get('hash')
        check_data = sorted((key, val) for key, val in telegram_data.items() if key != 'hash')

        # Конкатенация данных в строку в порядке возрастания ключей
        check_string = '\n'.join(f'{key}={val}' for key, val in check_data)

        # Конвертация секретного ключа из config.py в формат для верификации
        secret_key = base64.urlsafe_b64decode(TELEGRAM_SECRET_KEY + '=' * (4 - len(TELEGRAM_SECRET_KEY) % 4))

        try:
            # Загрузка открытого ключа для верификации подписи
            public_key = serialization.load_pem_public_key(secret_key)
            # Верификация подписи
            public_key.verify(
                base64.urlsafe_b64decode(telegram_hash + '=' * (4 - len(telegram_hash) % 4)),
                check_string.encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except Exception as e:
            # Если верификация не удалась, выбрасываем исключение
            raise HTTPException(status_code=400, detail='Invalid Telegram data')

        # Если подпись верна, передаем запрос дальше по пайплайну
        response = await call_next(request)
        return response
    # Для несовпадающих путей пропускаем запросы без изменений
    else:
        response = await call_next(request)
        return response
