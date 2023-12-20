FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt-get update && apt-get install -y libgl1-mesa-dev \
    && apt-get install -y libglib2.0-0

RUN python3 -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "-b", "0.0.0.0:8000". "app.wsgi"]