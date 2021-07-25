# 한국경제통계시스템
from selenium import webdriver
import time
driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("http://ecos.bok.or.kr/EIndex.jsp")

# 100대 통계지표 클릭
driver.find_element_by_css_selector("ul.ESsubject_btn > li > a").click()

# 새창으로 제어 넘기기
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)

# 엑셀 다운로드 클릭
driver.find_element_by_css_selector("div.HScontent-header > div > fieldset > a > img")

time.sleep(3)
driver.close()