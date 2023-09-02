#!/bin/bash

SUPERUSER_EMAIL=${DB_SUPERUSER_EMAIL:-'admin@django.com'}

cd /app/

/opt/venv/bin/python3 manage.py migrate --noinput
/opt/venv/bin/python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true