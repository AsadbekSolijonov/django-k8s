#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/python3 manage.py migrate --noinput
/opt/venv/bin/gunicorn --workdir-tmp-dir dev/shm django-k8s.
wsgi:application --bind "0.0.0.0":${APP_PORT}