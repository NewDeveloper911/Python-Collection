import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 112, "name": "Epic Flask website", "views": 180147017810947})
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())

'''
A JSON serialisable object, such as a Python dictionary, is needec
to be dealt with by the REST API
'''
