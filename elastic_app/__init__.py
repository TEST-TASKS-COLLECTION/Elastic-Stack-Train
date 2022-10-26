import os
from elasticsearch import Elasticsearch


HOST = os.getenv("HOST", "localhost")
# print("USING HOST: ", HOST)

client = Elasticsearch(
    hosts=[{"host": HOST, "port": 9200, 'scheme': "http"}],
    # basic_auth=("elastic", ELASTIC_PASSWORD)
)