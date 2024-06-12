FROM python:3.12

COPY wait-for-it.sh /usr/wait-for-it.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN apt-get update && apt-get install -y netcat-openbsd
RUN chmod +x /usr/wait-for-it.sh