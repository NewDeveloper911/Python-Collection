from googleapiclient.discovery import build
from datetime import datetime
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')
api_key = client.run(os.getenv('API_KEY'))
channel = client.run(os.getenv('CHANNEL'))
startdate = datetime(year=2020, month=4, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
enddate = datetime(year=2022, month=4, day=15).strftime('%Y-%m-%dT%H:%M:%SZ')

youtube = build('youtube', 'v3', developerKey=api_key)

'''
This commented-out section represents my former code used to identify one of my YouTube videos by checking for the channel which published my video
'''
request = youtube.search().list(q='What is love', part='snippet', type='video', maxResults = 100)#, publishedAfter=startdate, publishedBefore=enddate)
###This is a representation of a search for anything including 'unity' in the
###title collects extra data about that video in a snippet. It checks for videos
###and he maximum suggested here are 10 results

#Posts first 10 channels with channel name similar to mine
request = youtube.search().list(q='Biblically based.', part='snippet', type='channel', maxResults = 1000)
##type(request)

response = request.execute()
##
print("You have searched for and found " + str(len(response['items'])) + " items")
for item in sorted(response['items'], key=lambda x:x['snippet']['publishedAt']):
    print(item['snippet']['title'])
    if item['snippet']['channelTitle'] == "Biblically based.":
        print("Hooray, I found one of my videos.\nShouldn't have been that difficult to find though\nI should really try to make my channel stand out later on in the future but not now")
        my_channel_data = item
        channel_id = my_channel_data['snippet']['channelId']
        res = youtube.channels().list(id=channel_id, part='contentDetails')
        response = res.execute()
        break
    else:
        print("\tChannel name: " + item['snippet']['channelTitle'] + "\n")        


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
