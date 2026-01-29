#!/bin/bash

set -e

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Running tests..."
python manage.py test

echo "Running migrations..."
python manage.py migrate --noinput

echo "Importing suppliers..."
python manage.py import_fornecedor

echo "Importing invoices..."
python manage.py import_notafiscal

echo "Data import completed!"

echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000