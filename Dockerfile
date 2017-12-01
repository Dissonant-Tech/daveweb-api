FROM python:latest

ENV PYTHONUNBUFFERED 1
MAINTAINER David Rodriguez

RUN mkdir -p /usr/src/app
RUN mkdir -p /srv/media
RUN mkdir -p /srv/static
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN python manage.py collectstatic --noinput

EXPOSE 8000
VOLUME ["/srv/static", "/srv/media"]
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
