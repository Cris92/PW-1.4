#!/bin/bash
cd /home/site/wwwroot/hotel_pegaso
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --bind=0.0.0.0 --timeout 600 hotel_pegaso.wsgi
