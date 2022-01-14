import os
from dotenv import load_dotenv
import lyricsgenius

# Using lyricgenius library
load_dotenv()
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")
genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)

# Turn off status messages
genius.verbose = False

search = input("Search bar: ")

# Getting the lyrics for all songs of a search
songs = genius.search_songs(search)
song = songs["hits"][0]
id = song["result"]["id"]
song_lyrics = genius.lyrics(id)
artist_name = song["result"]["primary_artist"]["name"]
title = song["result"]["title"]

song_lyrics = song_lyrics.replace("EmbedShare URLCopyEmbedCopy", "")

list_lyrics = list(song_lyrics)
for i in range(len(song_lyrics) - 1, -1, -1):
    if song_lyrics[i].isdigit() == True:
        list_lyrics[i] = ""
    else:
        break
print("".join(list_lyrics))

# removing end numbers from string
# lyrics = list("fhee34ohgekwpe6921")

# for i in range(len(lyrics) - 1, -1, -1):
#     # print(lyrics[i], i)
#     if lyrics[i].isdigit() == True:
#         lyrics[i] = ""
#     else:
#         break
# print("".join(lyrics))


# for i in range(len(song_lyrics)):
#     print(-i)


# -21 to remove extra words (URL EMBEDDED etc.)
# print(
#     f"""
# -----------------------------
# {title} by {artist_name}
# -----------------------------

# {song_lyrics}

# ---powered by lyricgenius---"""
# )
