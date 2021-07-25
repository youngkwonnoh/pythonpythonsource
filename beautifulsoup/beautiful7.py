import requests
from bs4 import BeautifulSoup

with open("./beautiful/dormouse.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# title 가져오기
title = soup.select_one("p.title > b")
print(title)
print(title.string)
print(title.text)

#
link1 = soup.select_one("#link1")
print(link1)
print(link1.text)

#
link2 = soup.select_one("a[data-io='link3']")
print(link2)
print(link2.text)

# select : 리스트로 반환됨
link3 = soup.select("p.story > a")
print(link3)

#
link4 = soup.select("p.story")
print(link4)

for item in link4:
    temp = item.find_all("a")

    if temp:
        for v in temp:
            print(">>>>> ", v)
            print(">>>>> ", v.string)
    else:
        print(">>>>> ", item)
        print(">>>>> ", item.string)
