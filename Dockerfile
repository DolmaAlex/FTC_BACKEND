
FROM python:3.12


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r /app/requirements.txt


COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]