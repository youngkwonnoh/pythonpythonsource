from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver/chromedriver")

driver.get("https://www.daum.net")

# 검색 창에 검색어를 넣고 결과 페이지 받기
# find_~~~() : 원하는 요소 찾기

# 검색 창 요소 찾기
element = driver.find_element(By.NAME, "q")
print(element)

# 검색어 넣기
element.send_keys("안드로이드")
# 엔터 넣기
element.send_keys(Keys.RETURN)

# 스크린 샷
driver.save_screenshot("d:/andorid.jpg")


time.sleep(3)

driver.close()