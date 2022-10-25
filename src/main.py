from datetime import datetime
from elasticsearch import Elasticsearch

import os

HOST = os.getenv("HOST", "localhost")
print("USING HOST: ", HOST)

# es = Elasticsearch(hosts="http://localhost:9200", verify_certs=False)
# es = Elasticsearch(
#     "http://elasticsearch:9200",
#     # http_auth=["elastic", "changeme"]
#     verify_certs=False
# )

es = Elasticsearch(
    hosts=[{"host": "elasticsearch", "port": 9200, 'scheme': "http"}],
)

doc = {
    'author': 'Mikeyy',
    'text': 'Trying Elasticsearch',
    'timestamp': datetime.now(),
}

try:
    # providing our id to a index
    # print(1)
    # resp = es.index(index="test-index", id=1, document=doc)
    # print(1.1)
    # print(resp['result'])

    print(2)
    resp = es.get(index="test-index", id=1)
    print(resp['_source'])

    print(3)
    es.indices.refresh(index="test-index")

    print(4)
    resp = es.search(index="test-index", query={"match_all": {}})
    print("3", f"Got {resp['hits']['total']['value']} Hits:")

    print(5)
    for hit in resp['hits']['hits']:
        print(hit)
        print()
        
        print(hit["_source"])
        print("*"*20)
        # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


except Exception as e:
    print("x"*20)
    print("Getting this exception man: \n", e)
    print("x"*20)

finally:
    print("Thanks", input())