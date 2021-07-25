# gmarket 전체 카테고리 출력
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.gmarket.co.kr/")
soup = BeautifulSoup(response.content, "html.parser")

ul = soup.find("ul", class_="list__category-all")

# print(ul)

category_list = ul.find_all("span", class_="link__1depth-item")
# print(category_list)

for category in category_list:
    print(category.string)

    # 2차 카테고리
    print("\n")
    category_list_2depth = ul.find_all("li", class_="list-item__2depth")
    # print(category_list_2depth)
    for item in category_list_2depth:
        print(item.string)