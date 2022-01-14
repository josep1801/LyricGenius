from bs4 import BeautifulSoup
import requests

url = "..."
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
# search for all content within tbody (list tags within tbody)
trs = tbody.contents

# search next_sibling/siblings
print(trs[1].previous_sibling)
# or
print(list(trs[1].previous_sibling))
# also gives name of tag
print(trs[1].parent.name)
# descendents pf the tag
print(trs[1].descendents)
print(trs[1].children)
print(trs[1].content)
