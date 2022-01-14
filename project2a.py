from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
import lyricsgenius

# Using lyricgenius library
load_dotenv()
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")
GENIUS_CLIENT_ID = os.getenv("GENIUS_CLIENT_ID")
GENIUS_CLIENT_SECRET = os.getenv("GENIUS_CLIENT_SECRET")
# print(GENIUS_CLIENT_SECRET)

genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)

# Turn off status messages
genius.verbose = False
# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True

# example
# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
# # print(artist.songs)
# song = genius.search_song("To you", artist.name)
# print(song.lyrics)

search = input("Search bar: ")
request = genius.search_all(search)
# for hit in request["sections"][2]["hits"]:
#     print(hit["result"]["title"], "-", hit["result"]["artist_names"])


# Getting the lyrics for all songs of a search
songs = genius.search_songs(search)
song = songs["hits"][0]
id = song["result"]["id"]
song_lyrics = genius.lyrics(id)
artist_name = song["result"]["primary_artist"]["name"]
title = song["result"]["title"]

# song_lyrics.replace("EmbedShare URLCopyEmbedCopy", "")

result = re.sub(r"[0-9]+", "", song_lyrics)

print(
    f"""{title} by {artist_name}

{result[:-27]}

---powered by lyricgenius---"""
)


# input = input("song name? ")
# split_input = input.split()
# search_term = "%20".join(split_input)
# print(search_term)

# unable to happen as api is needed instead
# url = f"https://www.musixmatch.com/search/{search_term}"
# page = requests.get(url).text
# doc = BeautifulSoup(page, "html.parser")

# print(doc.prettify())

