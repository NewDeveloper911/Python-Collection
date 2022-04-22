from flask import request
import requests

#Exploring in a little bit more detail what really happens in the background of my FLASK requests
BASE = "http://127.0.0.1:5000/"

#Can make a response when restapi.py is running as a server and edit an existing video file in the database
response = requests.patch(BASE + "video/2", {"name": "Your boi is back","views": 93, "likes": 74})
print("Video name:", response.json()['name'])
print("Views on the video:", response.json()['views'])
print("Likes of the video:", response.json()['likes'])

#Can make a response when restapi.py is running as a server and create a new video file in the database
response = requests.put(BASE + "video/3", {"name": "This code kind of makes sense even a year later","views": 4654, "likes": 1354})
print(response.json())

#Getting the information from an existing file on the database
get_video = requests.get(BASE+"video/2")
print(get_video.json())

#Deleting the video with the id specified
delete_video = requests.delete(BASE + "video/1")

'''
A JSON serialisable object, such as a Python dictionary, is needed
to be dealt with by the REST API
'''
