from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()

# 브라우저 안 띄우기
options.headless = True

# 그래픽 카드 안  쓰기
options.add_argument("disable-gpu")

# 클라이언트 세팅하기
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")

# 브라우저 크기 지정
options.add_argument("window-size=1920x1080")

# 사용자가 쓰는 언어 지정
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome("../chromedriver/chromedriver")

# 페이지 요청
driver.get("https://www.naver.com/")

# 검색 창 찾기
element = driver.find_element_by_name("query")

element.send_keys('안드로이드')
element.send_keys(Keys.RETURN)

time.sleep(3)

driver.close()