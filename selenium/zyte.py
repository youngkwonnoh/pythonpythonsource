# https://www.zyte.com/blog/
# iframe 구성된 부분을 처리

from selenium import webdriver
import time

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("https://www.zyte.com/blog/")

time.sleep(5)

# 쿠키 수락 여부
driver.find_element_by_id("hs-eu-confirmation-button").click()

time.sleep(5)

# iframe 태그 찾기
iframe = driver.find_element_by_css_selector("div#intercom-container > div > div#intercom-modal-container > iframe")

# iframe 으로 제어권 이동
driver.switch_to.frame(iframe)

# iframe 안에서 x 버튼 클릭
driver.find_element_by_class_name("intercom-post-close").click()

# 원 화면으로 제어권 이동
driver.switch_to.default_content()

time.sleep(3)

# 첫번째 블로그 글 읽어오기
driver.find_element_by_css_selector("#_posts_grid-14-940 div.oxy-post > div > a.oxy-read-more").click()


driver.close()