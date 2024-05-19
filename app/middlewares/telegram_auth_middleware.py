from fastapi import Request, HTTPException
from hashlib import sha256
from hmac import new, compare_digest
import logging
from config import TELEGRAM_SECRET_KEY  # Импорт токена из файла конфигурации

logging.basicConfig(level=logging.INFO)


async def telegram_auth_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        # Предварительный запрос CORS пропускаем без изменений
        return await call_next(request)

    if '/auth/telegram' in str(request.url):
        try:
            data_check_arr = []

            # Извлекаем данные из запроса
            for key, value in sorted(request.query_params.items()):
                if key == "hash":
                    telegram_hash = value
                else:
                    data_check_arr.append(f"{key}={value}")

            # Создаем строку в формате 'ключ=значение\n' для каждой пары кроме 'hash'
            data_check_string = "\n".join(data_check_arr)

            # Создаем секретный хеш-ключ из токена бота
            secret_key = sha256(TELEGRAM_SECRET_KEY.encode('utf-8')).digest()

            # Вычисляем HMAC шифрование данных
            hmac_digest = new(secret_key, msg=data_check_string.encode('utf-8'), digestmod=sha256).hexdigest()

            # Сравниваем наш вычисленный хеш с переданным от Telegram
            if not compare_digest(hmac_digest, telegram_hash):
                raise ValueError("Data is NOT from Telegram")

            # Записываем в лог успешную верификацию
            logging.info("Successful Telegram data verification.")

            # Передаем обработку следующему миддлварю или эндпойнту
            response = await call_next(request)
            return response
        except Exception as e:
            # Логируем ошибку при неудачной верификации
            logging.error(f"Failed to verify Telegram data: {str(e)}")
            raise HTTPException(status_code=400, detail='Invalid Telegram data')

    # Пропускаем запросы, которые не связаны с эндпоинтом аутентификации Telegram
    response = await call_next(request)
    return response