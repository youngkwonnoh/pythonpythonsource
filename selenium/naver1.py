from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver/chromedriver")

# 페이지 요청
driver.get("https://www.naver.com/")

# 검색 창 찾기
element = driver.find_element_by_name("query")

element.send_keys('안드로이드')
element.send_keys(Keys.RETURN)

time.sleep(3)

driver.close()