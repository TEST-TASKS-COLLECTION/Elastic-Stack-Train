import json
import os

from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request

from .es_helpers import (
    get_doc, check_doc_exists,
    create_data, delete_document, search_query, bulk_create_data)

# ELASTIC_PASSWORD = "pw"
# username = "username"
# password = "password"
# host_ip = "host_ip"
# host_port = "host_port"


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("ELASTIC_USERNAME", "elastic")
PASSWORD = os.getenv("ELASTIC_PASSWORD", "pass")
# print("USING HOST: ", HOST)

# client = Elasticsearch(hosts=f"http://{USER}:{PASSWORD}@{HOST}:9200/")

client = Elasticsearch(
    # hosts=[{"host": HOST, "port": 9200, 'scheme': "http"}],
    hosts=f"http://{USER}:{PASSWORD}@{HOST}:9200/",
    # http_auth=(USER, PASSWORD),
    basic_auth=(USER, PASSWORD)
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

@app.route("/status", methods=["GET"],)
def api_status():
    return jsonify(**client.info())

@app.route("/document/delete/<string:id>", methods=["DELETE"],)
def del_doc(id):
    try:
        req = request.json
        index= req.get("index")
        if not index:
            return {"err": "Provide an index"}, 400
        res = delete_document(client=client, index=index, id=id)
        print("RESPONSE IS: ", res)
        return jsonify(**res), 200
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
        return jsonify(**res), 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/document/get/<string:id>", methods=["GET",])
def get_document(id):
    try:
        req = request.json
        index= req.get("index")
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
        # print(res, type(res))
        res = {"Doc exists": bool(res)}
        # print(res)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/index/create", methods=["POST"])
def create_index():
    try:
        req = request.json
        index= req.get("index_name")
        index_setting = req.get("index_setting")
        if not index:
            return {"err": "Provide an index"}, 400
        res = create_index(client, index_name=index, index_setting=index_setting)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400

@app.route("/document/search", methods=["GET"])
def search_doc():
    try:
        req = request.json
        index= req.get("index")
        query = req.get("query")
        if not index:
            return {"err": "Provide an index"}, 400
        if not query:
            return {"err": "Provide an query"}, 400
        res = search_query(client, index_name=index, query=query)
        return jsonify(**res), 200
    except Exception as e:
        return {"err": str(e)}, 400



@app.route("/document/bulk_create/", methods=["POST",])
def bulk_create_doc():
    try:
        req = request.json
        index= req.get("index")
        data = req.get("source")
        if not index:
            return {"err": "Provide an index"}, 400
        if not data:
            return {"err": "Provide a document to insert"}, 400
        res = bulk_create_data(client, index=index, data=data, file_path=None)
        print("response is", res)
        return jsonify(res), 200
    except Exception as e:
        return {"err": str(e)}, 400


@app.route("/document/bulk_create/status", methods=["GET",])
def bulk_create_doc_status():
    try:
        req = request.json
        index= req.get("index")
        if not index:
            return {"err": "Provide an index"}, 400

        res = client.count(index=index)
        print(res)
        return jsonify(res.body['count']), 200
    except Exception as e:
        return {"err": str(e)}, 400