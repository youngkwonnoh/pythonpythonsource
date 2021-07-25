# 네이버 증권 해외 증시
import requests 
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify)

# #container > div.aside > div > div.aside_area.aside_sotck > table > tbody > tr
global_stock = soup.select("div.aside_stock > table.tbl_home tr")
# print(global_stock)

for item in global_stock:
    # 증시명 가져오기
    stock_name = item.find("a")
    # 지수 인덱스 가져오기
    stock_index = item.select_one("td")
    # 지수 포인트 가져오기
    stock_point = item.select_one("td:nth-of-type(2)")

    print(stock_name.string, stock_index.string, stock_point.string)