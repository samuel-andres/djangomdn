# Deploy en sv linux con wsgi gunicorn y nginx en docker.

## docker-compose.yml:
```
services:

  web:
    container_name: llmdnweb
    build:
      context: ./app/
#    command: python manage.py runserver 0.0.0.0:8000
    command: gunicorn locallibrary.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./app/:/usr/src/app/
      - static_files:/usr/src/app/staticfiles
      - media_files:/usr/src/app/media
    expose:
     - 8000
#    ports:
#      - 7895:8000
    env_file:
      - ./.env/dev.env
  nginx:
    container_name: llmdnnginx
    build:
      context: ./nginx/
    ports:
      - 7896:80
    volumes:
      - ./nginx/conf.d/:/etc/nginx/conf.d/
      - static_files:/home/app/staticfiles
      - media_files:/home/app/media

volumes:
  static_files:
  media_files:

```

## nginx

### Dockerfile

```
FROM nginx:latest
RUN apt-get update && apt-get install -y procps
RUN mkdir -p /home/app/staticfiles
RUN mkdir -p /home/app/media
```

### default.conf

```
upstream locallibrary {
    server llmdnweb:8000;
}

server {
    listen 80;

    location / {
        proxy_pass http://locallibrary;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }

    location /static/ {
        alias /home/app/staticfiles/;
    }

    location /media/ {
        alias /home/app/media/;
    }

}
```

## django

### Dockerfile

```
FROM python:3.9.0-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
COPY . .
```

### variables de entorno (dev.env)

```
SECRET_KEY = 
ALLOWED_HOSTS = 
DEBUG = 
EMAIL_HOST_PASSWORD = 
DEFAULT_FROM_EMAIL = 
TIME_ZONE = 
PG_NAME = 
PG_USER = 
PG_PWD = 
PG_HOST = 
PG_PORT = 
PUB_DOM_ONE = 
PUB_DOM_TWO = 
```

No subo la config de postgres pq es igual que en la pollsapp de djangoproject que está en el otro repo y en este use uno que ya tenía corriendo.