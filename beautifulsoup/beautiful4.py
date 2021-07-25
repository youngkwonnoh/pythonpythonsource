from bs4 import BeautifulSoup

with open("dormouse.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
print("-- find()로 찾기 --")

title = soup.find("title")

# print("title >> {}".format(title))
# print("title 내용 >> {}".format(title.string))
# print("title 부모 태그 >> {}".format(title.find_parent("head")))

h1 = soup.find("h1")
# print("h1 >> {}".format(h1))
# print("h1 내용 >> {}".format(h1.string))

# print("p >> {}".format(soup.p))
# print("p 내용 >> {}".format(soup.p.string))


# 첫번째 p
# p1 = soup.find("p")
# print("p >> {}".format(p1))
# print("p 내용 >> {}".format(p1.get_text()))
# print("p 클래스명 >> {}".format(p1['class']))

# 두번째 p
# p2 = soup.find("p", class_="story")
# print("p >> {}".format(p2))
# print("p 내용 >> {}".format(p2.get_text()))
# print("p 클래스명 >> {}".format(p2['class']))

# a1 = soup.find("a")
# print("a >> {}".format(a1))
# print("a 태그 내용 >> {}".format(a1.string))

# a2 = soup.find("a", id="link2")
# print("a >> {}".format(a2))
# print("a 태그 내용 >> {}".format(a2.string))

# a3 = soup.find("a", id="link3")
# print("a >> {}".format(a3))
# print("a 태그 내용 >> {}".format(a3.string))
# print("a href >> {}".format(a3['href']))

# find_all() : 조건이 맞는 요소 모두 찾아오기
# a = soup.find_all("a", limit=2)
# print(a)

# h1 = soup.find_all("h1")
# print(h1)

# 클래스 명으로 제한
# a = soup.find_all("a", class_="sister")
# print(a)

# 텍스트 노드 값으로 제한 => Elsie
link = soup.find_all("a", string=["Elsie"])
print(link)