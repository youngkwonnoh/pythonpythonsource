import requests
from bs4 import BeautifulSoup

# 구글 뉴스 사이트에서 파이썬과 과련된 기사 추출

# 뉴스 타이틀/기사 링크 주소/기사 작성자/기사 작성 시간

response = requests.get("https://news.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako")
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# 기사 가져오기
articles = soup.find_all("article")
# print(articles)

# h1 ~ h6로 시작하는 모든 태그

# 뉴스 타이틀/기사 링크 주소/기사 작성자/기사 작성 시간
for idx, article in enumerate(articles):
    # 뉴스 타이틀과 링크 추출
    title = article.select_one("h3 > a")
    # 작성자
    writer = article.select_one('div a')
    # 작성시간
    date_time = article.select_one("div time")

    if date_time:
        date_time = date_time['datetime']
    else:
        date_time = ""
    
    print(idx + 1)
    print(title.text)
    print(title['href'])
    print(writer.text, date_time) # date_time.text => 9일전