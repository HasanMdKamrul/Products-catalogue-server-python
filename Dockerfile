FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app 

# Install dependencies

COPY ./productCatalogue/.env ./productCatalogue/.env

# Install dependencies