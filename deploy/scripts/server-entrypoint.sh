#!/bin/sh

until cd /app/server; do
  echo "Waiting for server volume..."
done

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8100
#gunicorn server.wsgi:application --bind 0.0.0.0:8100
exec "$@"