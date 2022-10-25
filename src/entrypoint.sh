#!/bin/sh

echo "Waiting for elasticsearch..."

while ! nc -z kibana 5601; do
    sleep 0.1
done

echo "ElasticSearch Started..."

python main.py