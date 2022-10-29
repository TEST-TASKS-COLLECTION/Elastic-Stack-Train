import os
from elasticsearch import Elasticsearch

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("ELASTIC_USERNAME", "elastic")
PASSWORD = os.getenv("ELASTIC_PASSWORD", "pass")

client = Elasticsearch(
    # hosts=[{"host": "elasticsearch", "port": 9200, 'scheme': "http"}],
    # http_auth=(USER, PASSWORD),
    hosts=f"http://{USER}:{PASSWORD}@{HOST}:9200/",
    # verify_certs=False # self signed certificates
    
    basic_auth=(USER, PASSWORD)
)


def test_client_object():
    # assert_type(client, <class 'elasticsearch.client.Elasticsearch'>)
    assert type(client) == Elasticsearch

def test_client():
    print(client.info())

if __name__ == "__main__":
    test_client_object()
    test_client()
    print(USER, PASSWORD, HOST)