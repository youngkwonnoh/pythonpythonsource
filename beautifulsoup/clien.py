# clien 사이트의 팁과 강좌 게시판의 1 ~ 5페이지 타이틀 크롤링

# https://www.clien.net/service/board/lecture
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=2

import requests
from bs4 import BeautifulSoup

# range(5) => 0 ~ 4, range(1, 11) => 1 ~ 10
for page_num in range(5):
    if page_num == 0: # 팁과 강좌 첫 페이지
        response = requests.get("https://www.clien.net/service/board/lecture")
    else: # 2 ~ 5 page
        response = requests.get("https://www.clien.net/service/board/lecture?&od=T31&category=0&po=" + str(page_num))

    soup = BeautifulSoup(response.content, 'html')

    # 타이틀 찾기
    titles = soup.select("span.subject_fixed")

    for title in titles:
        print(title.string.strip())