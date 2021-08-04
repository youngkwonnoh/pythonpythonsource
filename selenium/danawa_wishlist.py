# 다나와 로그인 / 상품명 / 관심상품 / 관심상품 출력
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("http://www.danawa.com/")
time.sleep(2)

# 로그인 버튼 클릭
login = driver.find_element_by_css_selector("li.my_page_service a")
login.click()

userid = driver.find_element_by_id("danawa-member-login-input-id")
# input 내용 지우기 clear()
# 다나와 아이디
userid.clear()
userid.send_keys("")

# 다나와 비밀번호
userpw = driver.find_element_by_id("danawa-member-login-input-pwd")
userpw.clear()
userpw.send_keys("")
userpw.send_keys(Keys.RETURN)
###----------------------------------- 로그인 자동화


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

# 화면 크기 출력 - 60 ~ 69인치
# driver.find_element_by_css_selector("div.so_cont_area > div:nth-child(4) div.cate_cont > div.basic_cate_list div:nth-child(3) span.ico").click()
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.so_cont_area > div:nth-child(4) div.cate_cont > div.basic_cate_list div:nth-child(3) span.ico")))
time.sleep(3)

# 첫번째 제품 클릭 후 관심상품 등록
driver.find_element_by_css_selector("#productItem13517876 > div > div.prod_info > p > a").click()
time.sleep(3)

# 새 창으로 제어권 이동
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# 관심상품 클릭
WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#interest > span.ico.ico_interest"))).click()

# 저장할 폴더 지정
WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "dl.wish_folder > dd > ul > li > a.folder_name"))).click()

# 관심상품 리스트로 가기
driver.find_element_by_css_selector("ul.my_serv_ul > li.interest_goods_service > a > span").click()
time.sleep(3)

# 관심상품 목록 출력
soup = BeautifulSoup(driver.page_source, "html.parser")

# 모든 관심상품 가져오기
wish_list = soup.select("table.wish_tbl > tbody > tr")

for idx, item in enumerate(wish_list, 1):
    product_name = item.select_one("td.info > div.tit > a").text
    # product_spec = item.select_one("td.spec > dd > a").text
    product_price = item.select_one("td.lowest > dl span.price").text

    print("[{}] {}".format(idx, product_name))
    # print("{}".format(product_spec))
    print("{}".format(product_price))
    print()

time.sleep(3)

driver.close()