# 다나와 로그인 / 상품명 / 관심상품 / 관심상품 출력
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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

# 제품명 입력 => 제품 정보 => 원하는 제품 선택 후 관심상품
# 관심상품 페이지로 이동 => 관심상품 목록 출력하기(제품명, 제품상세정보, 가격)

# 검색상품 입력
# 검색어를 입력할 요소 찾기
search = driver.find_element_by_id("AKCSearch")
search.clear()
search.send_keys("TV")
search.send_keys(Keys.RETURN)

# 제품이 보여질 때까지 기다리기
time.sleep(3)

# 제조사 클릭 - 삼성전자
driver.find_element_by_css_selector("#SearchOption_Maker_Rep > div:nth-child(2) span.ico").click()
# time.sleep(2)
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#SearchOption_Maker_Rep > div:nth-child(2) span.ico")))

# 화면기술 클릭 - QLED TV
driver.find_element_by_css_selector("div.so_cont_area > div:nth-child(3) div.cate_cont > div.basic_cate_list div:nth-child(5) span.ico").click()
# time.sleep(2)
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.so_cont_area > div:nth-child(3) div.cate_cont > div.basic_cate_list div:nth-child(5) span.ico")))

# 화면 크기 출력
driver.find_element_by_css_selector("div.so_cont_area > div:nth-child(4) div.cate_cont > div.basic_cate_list div:nth-child(3) span.ico").click()
# time.sleep(2)
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.so_cont_area > div:nth-child(4) div.cate_cont > div.basic_cate_list div:nth-child(3) span.ico")))

driver.close()