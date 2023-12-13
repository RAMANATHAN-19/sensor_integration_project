# Dockerfile for data_processing app
FROM python:3.8

WORKDIR /app

COPY data_processing/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY data_processing /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

