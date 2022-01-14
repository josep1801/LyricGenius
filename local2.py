from bs4 import BeautifulSoup
import re

# reading file from local systems
with open("dummy2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# modify tag attributes and document
tag = doc.find("option")
tag["value"] = "new value"
tag["selected"] = "false"
tag["colour"] = "blue"
print(tag)
# printall attributes that tag has
print(tag.attrs)

# find multiple tags
tags = doc.find_all(["p", "div", "li"])
print(tags)
# or ---- a tag that has a text and find specific attributes
tags2 = doc.find_all(["option"], text="Undergraduate", value="Undergraduate")
print(tags2)

# find class names
tags3 = doc.find_all(class_="btn-item")

# find regular expressions
tag4 = doc.find_all(text=re.compile("\$.*"))
for tag in tag4:
    print(tag.strip())

# linit number of result when we search for sth
tag4 = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tag4:
    print(tag.strip())

# save modified file
tags5 = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you"

with open("changed.html","w") as file:
    file.write(str(doc))
