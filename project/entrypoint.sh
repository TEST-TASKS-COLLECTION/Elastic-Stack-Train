#!/bin/sh

echo "Waiting for elasticsearch..."

while ! nc -z elasticsearch 9200; do
    sleep 0.1
done

echo "ElasticSearch Started..."

python manage.py run -h 0.0.0.0