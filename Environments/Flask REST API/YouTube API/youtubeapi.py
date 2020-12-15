from apiclient.discovery import build
from datetime import datetime

api_key = "AIzaSyBotO7j_3SvcNtLrL4bYXOhd075qLI7uDc"
startdate = datetime(year=2020, month=4, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
enddate = datetime(year=2020, month=4, day=15).strftime('%Y-%m-%dT%H:%M:%SZ')

youtube = build('youtube', 'v3', developerKey=api_key)

'''
This commented-out section represents my former code used to identify one of my YouTube videos by checking for the channel which published my video
'''
##request = youtube.search().list(q='Thrills Final Official Audio - tYrone', part='snippet', type='video', maxResults = 100)#, publishedAfter=startdate, publishedBefore=enddate)
###This is a representation of a search for anything including 'unity' in the
###title collects extra data about that video in a snippet. It checks for videos
###and he maximum suggested here are 10 results
##
###request = youtube.search().list(q='Nana', part='snippet', type='channel', maxResults = 10)
##type(request)
##
##response = request.execute()
###print(response)
##
##print("You have searched for and found " + str(len(response['items'])) + " items")
##for item in sorted(response['items'], key=lambda x:x['snippet']['publishedAt']):
##    print(item['snippet']['title'])
##    if item['snippet']['channelTitle'] == "Nana":
##        print("Hooray, I found one of my videos.\nShouldn't have been that difficult to find though\nI should really try to make my channel stand out later on in the future but not now")
##        my_channel_data = item
##        break
##    else:
##        print("\tChannel name: " + item['snippet']['channelTitle'] + "\n")
        
channel_id = my_channel_data['snippet']['channelId']
res = youtube.channels().list(id=channel_id, part='contentDetails')
response = res.execute()
print(response)

def get_channel_videos(channel_ID):
    res3 = youtube.channels().list(id=channel_ID, part='contentDetails')
    rspi = res3.execute()
    playlistId = rspi['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
    while 1:
        res3 = youtube.playlistItems().list(playlistId=playlistId, part='snippet', maxResults=5, pageToken=next_page_token)
        respo = res3.execute()
        videos += respo['items']
        next_page_token = respo.get('nextPageToken')

        if next_page_token is None:
            break
    return videos

videos = get_channel_videos(channel_id)
for video in videos:
    print(video['snippet']['title'])
