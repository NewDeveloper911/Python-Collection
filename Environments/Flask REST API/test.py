import requests

BASE = "http://127.0.0.1:5000/"

##data = [{"likes": 420, "name": "Snoop Doogg tries cocaine", "views": 6942021969420},
##        {"likes": 69, "name": "Your boy made a tutorial video", "views": 69420},
##        {"likes": 9715138247, "name": "meme", "views": 69709196507420}]
##
##for i in range(len(data)):
##    response = requests.put(BASE + "video/" + str(i), data[i])
##    print(response.json())
##
####input()
####response = requests.delete(BASE + "video/0")
####print(response)
##input()
#response = requests.get(BASE + "video/2")
response = requests.patch(BASE + "video/1", {"name": "Your boi is back","views": 7816488057014679, "likes": 696969696969696969})
print(response.json())

'''
A JSON serialisable object, such as a Python dictionary, is needed
to be dealt with by the REST API
'''
