#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd sensors; python manage.py createsuperuser --no-input)
fi
(cd sensors; gunicorn sensors.wsgi:application --user www-data --bind 0.0.0.0:8010 --workers 50) &
nginx -g "daemon off;"