# Dockerfile for sensor_integration app
FROM python:3.8

WORKDIR /app

COPY sensor_integration/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY sensor_integration /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

