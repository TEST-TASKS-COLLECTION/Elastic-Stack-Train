
def get_index(client, index, id):
    pass
    client.get()

def create_data(client, index, id, data):
    """
    Create a document with the provided id in the index
    Args:
        client (_type_): client (ElasticSearch object) 
        index (_type_): index for the document where it shall belong
        id (_type_): id of the document
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
        client (_type_): client (ElasticSearch object) 
        index (_type_): index for the document where it shall belong
        id (_type_): id of the document
    send_data_as:
        client.create("test-index-2", id="420", body={
        "title": "man",
        "feed": "back lol"
    # })
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
        client (_type_): client (ElasticSearch object) 
        index (_type_): index for the document where it shall belong
        id (_type_): id of the document
    send_data_as:
        client.create("test-index-2", id="420", body={
        "title": "man",
        "feed": "back lol"
    # })
    """
    print("----------------CHECKING IF DOCUMENT EXISTS--------------------")
    res = client.exists(index=index, id=id)
    return res


def get_doc(client, index, id):
    """
    Returns a document with the provided id in the index
    Args:
        client (_type_): client (ElasticSearch object) 
        index (_type_): index for the document where it shall belong
        id (_type_): id of the document
    send_data_as:
        client.create("test-index-2", id="420", body={
        "title": "man",
        "feed": "back lol"
    # })
    """
    print("----------------GETTING A DOCUMENT--------------------")
    res = client.get(index=index, id=id)
    return res