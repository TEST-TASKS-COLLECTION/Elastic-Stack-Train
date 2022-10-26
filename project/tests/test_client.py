from elasticsearch import Elasticsearch

client = Elasticsearch(
    hosts=[{"host": "elasticsearch", "port": 9200, 'scheme': "http"}],
    # basic_auth=("elastic", ELASTIC_PASSWORD)
)

def test_client_object():
    # assert_type(client, <class 'elasticsearch.client.Elasticsearch'>)
    assert type(client) == Elasticsearch


if __name__ == "__main__":
    test_client_object()