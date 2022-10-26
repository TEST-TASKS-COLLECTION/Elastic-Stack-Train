from elastic_app import client


print(type(client))
print(client.info())

print(client.delete("test-index-2", id="420"))

