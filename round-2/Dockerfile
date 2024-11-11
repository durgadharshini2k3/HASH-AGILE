FROM python:3.9-slim

RUN apt-get update\
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app

