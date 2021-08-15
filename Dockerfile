FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

CMD ["python3", "main.py"]

