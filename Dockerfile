# Использование базового образа Python 3.12
FROM python:3.12

# Определение рабочего каталога в контейнере
WORKDIR /app

# Копирование файла `requirements.txt` из корневой директории вашего проекта в рабочую директорию контейнера
COPY ./requirements.txt /app/requirements.txt

# Установка зависимостей из файла `requirements.txt`
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование директории `app` вашего приложения в рабочий каталог контейнера
COPY ./app /app

# Команда для запуска приложения, использует Uvicorn с указанием хоста (внутри контейнера)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]