# api-guess-the-color
Тестовое задание для БО-Энерго. Сервис по угадыванию цвета


# Клонирование репозиотрия

```
git clone https://github.com/cianoid/api-guess-the-color.git
```

# Создание .env-файла

Создайте .env-файл и заполните его

Путь к файлу:
```
api-guess-the-color/guess_the_color/.env
```

Пример заполнения файла:
```
SECRET_KEY=djtre-raskljdio2ango-seee3452asdo3R$@TG%$
DEBUG=1
ALLOWED_HOSTS=localhost
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db/db.sqlite3 # файл должен лежать в папке db, если необходимо сохранять данные в volume Docker
```

# Запуск проекта

Предусмотрено три варианта запуска сервиса. 
* [сервер разработки Django](#запуск-в-dev-режиме)
* [контейнер Docker](#запуск-в-контейнере-docker)
* [с помощью docker-compose](#запуск-через-docker-compose)

# Доступ к данным

После запуска будут доступны следующие ресурсы: 
* [эндпоинт решения квадратных уравнений](http://localhost:8000/api/v1.0/guess/)
* [документация к API](http://localhost:8000/redoc/)

## Запуск в dev-режиме

### Установка venv с зависимостями

```
cd api-guess-the-color

# для Linux, MacOS
python3 -m venv venv
source venv/bin/activate

# для Windows
python -m venv venv
venv/Scripts/activate

python -m pip install --upgrade pip
cd guess_the_color
pip install -r requirements.txt
```

### Запуск тестов

```
python manage.py test
```

### Миграции БД и запуск сервиса 

```
python manage.py migrate
python manage.py runserver localhost:8000
```

## Запуск в контейнере Docker

```
docker build -t guess_the_color .
docker run --env-file .env --name guess_the_color -it -p 8000:8000 guess_the_color
```

## Запуск через docker-compose

В проекте подготовлен образ сервиса и загружен на Docker Hub. Проект запускается в двух контейнерах (backend, nginx) и слушает запросы на порту 8000

Для запуска необходимо скопировать файл .env в директорию **guess_infra** и выполнить в ней же следующую команду

Перед запуском проекта можно заменить значение DEBUG на **0** в файле .env

```
docker-compose up -d
```

# Автор
Шатава Игорь, Python-разработчик
