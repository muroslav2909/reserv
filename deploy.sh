#!/bin/sh
export C_FORCE_ROOT=1
python manage.py migrate vamiko
python manage.py syncdb --noinput
# Note that Django 1.8 has no '--all' param #--all

python manage.py collectstatic --clear --noinput

python manage.py supervisor --daemonize
python manage.py supervisor status
tail -f logs/gunicorn.log