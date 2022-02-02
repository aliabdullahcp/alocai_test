# pull official base image
FROM python:3.8-slim

# set work directory
WORKDIR /code

# install psycopg2 dependencies
RUN apt-get update \
  && apt-get -y --no-install-recommends install \
     gcc g++ curl gettext vim git \
     # python depencies
     python3-dev python3-setuptools \
     # Pandas dependcies
#     libblas3 libblas-dev liblapack3 liblapack-dev gfortran \
     # turicreate deps
#     libgconf-2-4 \
     # Postgres
     libpq-dev \
  && apt-get clean


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install gunicorn

COPY . /code/

RUN pip install -r requirements.txt
