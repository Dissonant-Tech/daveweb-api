#!/bin/bash

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn daveweb.wsgi:application \
    --name splyttr \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    "$@"
