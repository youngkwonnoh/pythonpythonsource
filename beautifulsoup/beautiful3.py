from bs4 import BeautifulSoup

with open("dormouse.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
print("-- 태그로 찾기 --")
# print("title >> {}".format(soup.title))
# print("title 내용 >> {}".format(soup.title.string))
# print("title 부모 태그 >> {}".format(soup.title.parent))

# print("h1 >> {}".format(soup.h1))
# print("h1 내용 >> {}".format(soup.h1.string))


# print("p >> {}".format(soup.p))
# print("p 내용 >> {}".format(soup.p.string))


# 첫번째 p
p1 = soup.p
# print("p >> {}".format(p1))
# print("p 내용 >> {}".format(p1.string))
# print("p 클래스명 >> {}".format(p1['class']))

# 두번째 p
# p2 = p1.find_next_sibling("p")
# print("p >> {}".format(p2))
# print("p 내용 >> {}".format(p2.string))
# print("p 클래스명 >> {}".format(p2['class']))

a1 = soup.a
# print("a >> {}".format(a1))
# print("a 태그 내용 >> {}".format(a1.string))

a2 = a1.find_next_sibling("a")
print("a >> {}".format(a2))
print("a 태그 내용 >> {}".format(a2.string))