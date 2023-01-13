FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app



COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app 


# FROM python:3-alpine

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver"]