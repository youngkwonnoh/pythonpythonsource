# 다음 뉴스 댓글 가져오기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("https://news.v.daum.net/v/20210723110513150")

loop, count = True, 0

while loop and count < 3:
    try:
        # 더보기 버튼이 위치할 때까지 driver가 5초 기다리기
        # EC.presence_of_element_located((By.CSS_SELECTOR,""))  튜플로 넘겨주기 위해 located를 두 번 괄호 사용
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.alex_more > button")))
        element.click()

        count += 1
    except TimeoutException:
        loop = False

# 댓글 내용 출력하기
comment_list = driver.find_elements_by_css_selector("ul.list_comment li")

for num, comment in enumerate(comment_list):

    content = comment.find_element_by_css_selector("div p")

    print("[{}] : {}".format(num, content.text))

time.sleep(3)

driver.close()