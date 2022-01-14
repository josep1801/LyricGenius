from bs4 import BeautifulSoup
import re

# reading file from local systems
with open("dummy3.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.find_all(class_="inneri"))

# for tag in doc.find_all():
#     print(tag.name, tag.attrs)

tag2 = doc.find(class_="inner1")
print(tag2.get("id"))

tags = doc.find_all()
for tag in tags:
    if "id" in tag.attrs:
        print(tag.name, tag["id"], sep="->")
