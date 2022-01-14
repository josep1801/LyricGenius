import os
from dotenv import load_dotenv
import requests

# Using genius api
load_dotenv()
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")
GENIUS_CLIENT_ID = os.getenv("GENIUS_CLIENT_ID")
GENIUS_CLIENT_SECRET = os.getenv("GENIUS_CLIENT_SECRET")

baseUrl = "http://api.genius.com"

headers = {"Authorization": "Bearer" + GENIUS_CLIENT_ACCESS_TOKEN}
searchUrl = baseUrl + "/search"
songTitle = "Shelter"
data = {"q": songTitle}
response = requests.get(searchUrl, params=data, headers=headers)
json = response.json()
print(json)
