from bs4 import BeautifulSoup
import requests
import re

# https://genius.com/The-weeknd-here-we-go-again-lyrics
# https://genius.com/search?q=blinding%20lights

input = input("song name? ")
split_input = input.split()
search_term = "+".join(split_input)
# print(search_term)


def lyric_scrap():
    url = f"https://search.azlyrics.com/search.php?q={search_term}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    class_tags = doc.find_all(class_="text-left visitedlyr")
    best_result = class_tags[0].find("a")
    # print(best_result["href"])
    best_link = best_result["href"]

    url2 = f"{best_link}"
    page2 = requests.get(url2).text
    doc2 = BeautifulSoup(page2, "html.parser")

    lyrics = doc2.find(class_="ringtone").find_next_sibling("div").text
    song_name = doc2.find(class_="ringtone").find_next_sibling("b").text
    band_name = doc2.find(class_="lyricsh").find("b").text

    # for e in lyrics.find_all("br"):
    #     e.extract()

    print(
        f"""
{band_name}-{song_name}
{lyrics}"""
    )


try:
    lyric_scrap()
except:
    print(
        "Sorry, your search returned no results. Try to compose less restrictive search query or check spelling."
    )

