import os

from elasticsearch import Elasticsearch

from flask import Flask, jsonify


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

def get_index(client):
    pass