from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch(hosts="http://elasticsearch:9200")
# es = Elasticsearch(hosts="http://localhost:9200", verify_certs=False)

doc = {
    'author': 'Mikeyy',
    'text': 'Trying Elasticsearch',
    'timestamp': datetime.now(),
}

try:
    # providing our id to a index
    resp = es.index(index="test-index", id=1, document=doc)
    print(resp['result'])

    resp = es.get(index="test-index", id=1)
    print(resp['_source'])

    es.indices.refresh(index="test-index")

    resp = es.search(index="test-index", query={"match_all": {}})
    print(f"Got {resp['hits']['total']['value']} Hits:")

    for hit in resp['hits']['hits']:
        print(hit)
        print()
        
        print(hit["_source"])
        print("*"*20)
        # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


except Exception as e:
    print("Getting this exception man", e)

finally:
    input()