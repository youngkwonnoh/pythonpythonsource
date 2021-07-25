from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver/chromedriver")

# 페이지 요청
driver.get("https://www.python.org/")

# 특정 요소 찾기
ele = driver.find_element_by_name('q')

# 검색어 넣기
ele.send_keys("python")

# 엔터 입력
ele.send_keys(Keys.RETURN)


time.sleep(3)

driver.close()