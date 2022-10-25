import os

from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "pw"

username = "username"
password = "password"
host_ip = "host_ip"
host_port = "host_port"

ES_URL = "elasticsearch://{username}:{password}@{host_ip}:{host_port}"

client = Elasticsearch(
    hosts=[{"host": "elasticsearch", "port": 9200, 'scheme': "http"}],
    # basic_auth=("elastic", ELASTIC_PASSWORD)
)
# client = Elasticsearch("http://localhost:9200")

HOST = os.getenv("HOST", "localhost")
print("USING HOST: ", HOST)


# Successful response!
print(client.info())
