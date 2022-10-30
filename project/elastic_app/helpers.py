INDEX_SETTING = {
    "settings": {
        "index": {
            "number_of_shards": 4
        }
    }
}



# def get_index(client, index, id):
#     pass
#     client.get()

def create_data(client, index, id, data):
    """
    Create a document with the provided id in the index
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index (string): index for the document where it shall belong
        id (string): id of the document
        data (_type_): data that the document should have
    send_data_as:
        client.create("test-index-2", id="420", body={
        "title": "man",
        "feed": "back lol"
    # })
    """
    print("----------------CREATING DOCUMENT--------------------")
    return client.create(index=index, id=id, body=data)

def delete_document(client, index, id):
    """
    Delete a document with the provided id in the index
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index (string): index for the document where it shall belong
        id (string): id of the document
    send_data_as:
        client.delete("test-index-2", id="420")
    """
    print("----------------DELETING DOCUMENT--------------------")
    res = client.delete(index=index, id=id)
    if res['result']:
        print(res['result'])
    return res

def check_doc_exists(client, index, id):
    """
    Check if a document with the provided id in the index exists
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index (string): index for the document where it shall belong
        id (string): id of the document
    send_data_as:
        client.exists("test-index-2", id="420")
    """
    print("----------------CHECKING IF DOCUMENT EXISTS--------------------")
    res = client.exists(index=index, id=id)
    return res


def get_doc(client, index, id):
    """
    Returns a document with the provided id in the index
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index (string): index for the document where it shall belong
        id (string): id of the document
    send_data_as:
        client.create("test-index-2", id="420", body={
        "title": "man",
        "feed": "back lol"
    # })
    """
    print("----------------GETTING A DOCUMENT--------------------")
    res = client.get(index=index, id=id)
    return res

def create_index(client, index_name="test", index_setting=None):
    """
    Creates an index with following setting
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index_name (string): name for the index we want to create
        index_setting (dict): setting for the index creation
    send_data_as:
        client.create("test-index-2", body = {
                    "settings": {
                        "index": {
                            "number_of_shards": 4
                                }}
                    })
    """
    print("----------------GETTING A DOCUMENT--------------------")
    if not index_setting:
        res = client.indices.create(index_name, body=index_setting)
    else:
        res = client.indices.create(index_name, body=INDEX_SETTING)
    return res

def search_query(client, index_name, query):
    """
    Get result according to the query
    Args:
        client (Elasticsearch Object): client (ElasticSearch object) 
        index_name (string): name for the index we want to create
        query (dict): query for the elastic search
    send_data_as:
        client.search("test-index-2", body = {
                    'size': 5,
                    'query': {
                        'multi_match': {
                        'query': "Miller,
                        'fields': ['title^2', 'director']
                        }}}
                    )
    """
    print("----------------SEARCHING A DOCUMENT--------------------")
    res = client.search(
        body = query,
        index = index_name
    )
    return res