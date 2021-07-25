from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver/chromedriver")

# 페이지 요청
driver.get("https://www.python.org/")

# 특정 요소 찾기
ele = driver.find_element_by_name('q')

# 검색어 넣기
ele.send_keys("python")

# 엔터 입력
ele.send_keys(Keys.RETURN)

# 검색 결과 페이지
# titles = driver.find_elements_by_tag_name("h3")
# print(titles)

# for title in titles:
#     print(title.text)

# BeautifulSoup 이용
soup = BeautifulSoup(driver.page_source,"html.parser")
titles = soup.find_all("h3")

for title in titles:
    print(title.text)

time.sleep(3)

driver.close()