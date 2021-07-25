import requests
from bs4 import BeautifulSoup
import xlsx_write as excel


response = requests.get("https://www.clien.net/service/board/lecture")
soup = BeautifulSoup(response.content, 'html.parser')

# 타이틀 찾기
titles = soup.select("span.subject_fixed")

# 비어있는 리스트 생성
board_list = list()

for title in titles:
    # print(title.string.strip())
    board_title = [title.string.strip()]
    print(board_title)

    board_list.append(board_title)

excel.write_excel_template("clien1.xlsx", "팁과강좌", board_list)
