import os
from urllib import request

from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request


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



app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>HELLO WORLD</h1>"

@app.route("/ping", methods=['GET',])
def ping_pong():
    return jsonify(
        {
            "status": "success",
            "message": "pong!"
        }
    )

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

@app.route("/status", methods=["GET"],)
def api_status():
    client.info()

@app.route("/document/delete/<string:id>", methods=["DELETE"],)
def del_doc(id):
    try:
        req = request.json
        index= req.get("index")
        if not index:
            return {"err": "Provide an index"}, 400
        res = delete_document(client=client, index=index, id=id)
        print("RESPONSE IS: ", res)
        return res, 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/document/create/<string:id>", methods=["POST",])
def create_doc(id):
    try:
        req = request.json
        index= req.get("index")
        data = req.get("data")
        if not index:
            return {"err": "Provide an index"}, 400
        if not data:
            return {"err": "Provide a document to insert"}, 400
        res = create_data(client, index=index, id=id, data=data)
        print(res)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/document/get/<string:id>", methods=["GET",])
def get_document(id):
    try:
        req = request.json
        index= req.get("index")
        data = req.get("data")
        if not index:
            return {"err": "Provide an index"}, 400
        res = get_doc(client, index=index, id=id)
        print("res", res)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/document/exists/<string:id>", methods=["GET",])
def check_if_doc_exists(id):
    try:
        req = request.json
        index= req.get("index")
        if not index:
            return {"err": "Provide an index"}, 400
        res = check_doc_exists(client, index=index, id=id)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400