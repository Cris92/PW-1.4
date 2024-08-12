#!/bin/bash
cd /home/site/wwwroot/hotel_pegaso
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind=0.0.0.0 --timeout 600 hotel_pegaso.wsgi
