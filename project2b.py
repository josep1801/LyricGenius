from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import re

# Using genius api
load_dotenv()
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")

search_term = input("Search for song lyrics: ")
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={GENIUS_CLIENT_ACCESS_TOKEN}"
response = requests.get(genius_search_url)
search_json_data = response.json()

song = search_json_data["response"]["hits"][0]
artist_name = song["result"]["primary_artist"]["name"]
title = song["result"]["title"]
url = song["result"]["url"]

lyric_url = f"{url}"
page = requests.get(lyric_url).text
doc = BeautifulSoup(page, "html.parser")

# print(doc.prettify())
# lyrics = doc2.find(class_="ringtone").find_next_sibling("div").text

# div = doc.find("div", class_=re.compile("^lyrics$|Lyrics__Root"))
# lyrics = div.get_text()
# print(lyrics)

# for tag in doc.body.find_all():
#     print(tag.name, tag.attrs)

# for tag in doc.body.find_all():
#     if "id" in tag.attrs:
#         print(tag.name, tag["id"], sep="->")

# fail
# for tag in doc.body.find_all():
#     if "id" in tag.attrs:
#         if tag["id"] == "lyrics-root":
#             for span in tag.find_all("span"):
#                 for i in span.contents:
#                     if type(i) == bs4.element.NavigableString":
#                         print(span.contents)
#                     else:
#                         continue


# for tag in doc.body.find_all():
#     if "id" in tag.attrs:
#         if tag["id"] == "lyrics-root":
#             for content in tag.a.span:
#                 print(content)
# print(tag.a.span.contents)

# doesnt work ;< no idea why
# div = doc.find_all("div").name
# print(div)

# some odd reasons the url does not accept the access token
# id = song["result"]["id"]
# genius_song_url = (
#     f"http://api.genius.com/songs/{id}?access_token={GENIUS_CLIENT_ACCESS_TOKEN}"
# )
# response2 = requests.get(genius_song_url)
# song_json_data = response2.json()

# lyrics = song_json_data["response"]

# print(lyrics)

# print(
#     f"""{title} by {artist_name}

# {song_lyrics}

# ---powered by lyricgenius---"""
# )

