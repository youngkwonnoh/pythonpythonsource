import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/서울_지하철"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup.prettify)

# 첫번째 이미지 태그 가져오기
# mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
img1 = soup.select_one("div.mw-parser-output > table img")
print(img1)

# 두번째 이미지 태그
# #mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img
img2 = soup.select_one("div.thumbinner img")
print(img2)

# src 속성 값 출력
print("img1 src ", img1["src"])
print("img2 src ", img1["src"])

# a 링크의 갯수?
links = soup.select("a")
print("link count : ", len(links))