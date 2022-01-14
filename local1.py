from bs4 import BeautifulSoup

# reading file from local systems
with open("dummy1.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# includes indents
# print(doc.prettify())

tag = doc.title
# prints out the title tag
print(tag)
# prints out the title
print(tag.string)
# prints out the modfied title
tag.string = "hello"
print(tag.string)

#finds first p tags
tags = doc.find("p")
#finds all p tags
tags = doc.find_all("p")
#access things within the tag
tags = doc.find_all("p")[0]
print(tags.find_all("b"))
