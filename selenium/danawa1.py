# 다나와 로그인 자동화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("http://www.danawa.com/")
time.sleep(2)

# 로그인 버튼 클릭
login = driver.find_element_by_css_selector("li.my_page_service a")
login.click()

userid = driver.find_element_by_id("danawa-member-login-input-id")
# input 내용 지우기 clear()
userid.clear()
userid.send_keys("i03man")

userpw = driver.find_element_by_id("danawa-member-login-input-pwd")
userpw.clear()
userpw.send_keys("dudtka@^86")
userpw.send_keys(Keys.RETURN)

driver.close()