from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.maximize_window()
driver.get("https://sll.seoul.go.kr")

time.sleep(2)

# 팝업창 닫기
popup = driver.find_element_by_name("btn_layer_popup_close")
popup.click()

# 통합 검색 클릭
search = driver.find_element_by_class_name("srh-in")
search.click()

# 큰 검색창 찾기
element = driver.find_element_by_id("query")
# 검색어 입력
element.send_keys("영어")
# 엔터
element.send_keys(Keys.ENTER)

print(driver.current_url) # https://sll.seoul.go.kr/main/MainView.dunet

# 새 창을 제어할 수 있도록 제어권 이동
driver.switch_to.window(driver.window_handles[-1])
# 제어권 확인
print("제어권 이동 {}".format(driver.current_url))
time.sleep(2)
# 온라인학습 더 많은 결과 보기 클릭
# driver.find_element_by_class_name("btn-more-result").click()
more = driver.find_element_by_class_name("btn-more-result")
more.click()

# 온라인 강좌명 출력
titles = driver.find_elements_by_css_selector("div.search-result-list > ul > li a")
for title in titles:
    print(title.text)

time.sleep(2)
# 부모 창 닫기
driver.close()