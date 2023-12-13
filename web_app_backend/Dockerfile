# Dockerfile for web_app_backend app
FROM python:3.8

WORKDIR /app

COPY web_app_backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY web_app_backend /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

