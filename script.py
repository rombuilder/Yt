import io
import os
import requests

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with the URL for the client secrets file
client_secrets_file_url = "https://github.com/rombuilder/Yt/blob/main/client_secret.json"

# Download the client secrets file
response = requests.get(client_secrets_file_url)
if response.status_code != 200:
    raise Exception("Failed to download client secrets file")

# Load the client secrets file into memory
creds = Credentials.from_authorized_user_info(info=response.json())

# Authenticate and build the YouTube API client
youtube = build("youtube", "v3", credentials=creds)

# Replace with the video links
video_links = ["https://youtu.be/42v9nCf5gzM", "https://www.youtube.com/watch?v=efgh5678"]

for video_link in video_links:
    # Get the video ID from the link
    video_id = video_link.split('v=')[1]
    
    # Get the video details from the YouTube Data API
    request = youtube.videos().list(
        part='snippet,status,statistics,contentDetails',
        id=video_id
    )
    response = request.execute()
    
    # Get the video title, description, tags, and category ID
    video_title = response['items'][0]['snippet']['title']
    video_description = response['items'][0]['snippet']['description']
    video_tags = response['items'][0]['snippet']['tags']
    video_category_id = response['items'][0]['snippet']['categoryId']
    
    # Upload the video to YouTube
    request = youtube.videos().insert(
        part='snippet,status,statistics,contentDetails',
        body={
            'snippet': {
                'title': video_title,
                'description': video_description,
                'tags': video_tags,
                'categoryId': video_category_id
            },
            'status': {
                'privacyStatus': 'public'
            }
        },
        media_body=f'/path/to/video/{video_id}.mp4'
    )
    response = request.execute()
    print(f'Uploaded video with ID: {response["id"]}')
