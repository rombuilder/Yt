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
    # Download the video from YouTube
    # ...

    # Upload the video to YouTube
    # ...


