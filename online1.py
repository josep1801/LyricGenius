from bs4 import BeautifulSoup
import requests

url = "https://realpython.com/beautiful-soup-web-scraper-python/"

result = requests.get(url)
# gets html document
# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())

# finds all text that includes dollar sign
prices = doc.find_all(text="$")
print(prices)

# BeytifulSoup tree structure (parent and descendent)
parent = prices[0].parent
print(parent)
strong = parent.find("strong")
print(strong)

