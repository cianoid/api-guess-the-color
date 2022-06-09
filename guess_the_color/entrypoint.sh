#!/usr/bin/env bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn guess_the_color.wsgi:application --bind 0:8000
