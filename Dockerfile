FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r req.txt

CMD ["python", "main.py"]