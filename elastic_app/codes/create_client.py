import os

from elasticsearch import Elasticsearch

import elastic_app

# ELASTIC_PASSWORD = "pw"

# username = "username"
# password = "password"
# host_ip = "host_ip"
# host_port = "host_port"

# ES_URL = "elasticsearch://{username}:{password}@{host_ip}:{host_port}"

HOST = os.getenv("HOST", "localhost")
# print("USING HOST: ", HOST)

client = Elasticsearch(
    hosts=[{"host": HOST, "port": 9200, 'scheme': "http"}],
    # basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
# print(client.info())