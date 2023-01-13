FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

# Install dependencies

COPY ./productCatalogue/.env /app/productCatalogue/.env

# Install dependencies

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app 