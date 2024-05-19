from fastapi import Request, HTTPException
from hashlib import sha256
from hmac import new, compare_digest
import logging
from config import TELEGRAM_SECRET_KEY  # Импорт токена из файла конфигурации
import base64

logging.basicConfig(level=logging.INFO)


async def telegram_auth_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        return await call_next(request)

    if '/auth/telegram' in str(request.url):
        telegram_data = dict(request.query_params)
        telegram_hash = telegram_data.pop('hash', None)

        if not telegram_hash:
            logging.error("Hash parameter is missing in the request")
            raise HTTPException(status_code=400, detail='Invalid Telegram data')

        check_string = '\n'.join(f'{key}={value}' for key, value in sorted(telegram_data.items()))

        # В вашем предыдущем коде не было импорта для hmac, добавляем его
        # Также используем ваш TELEGRAM_SECRET_KEY для создания секрета, а не публичного ключа
        secret_key = sha256(TELEGRAM_SECRET_KEY.encode('utf-8')).digest()
        # Создаем проверочный хеш
        hmac_digest = new(secret_key, msg=(check_string).encode('utf-8'), digestmod=sha256).hexdigest()

        if not compare_digest(hmac_digest, telegram_hash):
            logging.error("Verification failed: computed hash does not match the provided hash")
            raise HTTPException(status_code=400, detail='Invalid Telegram data')

        logging.info("Telegram data verification succeeded")
        response = await call_next(request)
        return response
    else:
        response = await call_next(request)
        return response