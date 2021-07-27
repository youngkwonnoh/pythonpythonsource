from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome("../chromedriver/chromedriver")
# driver.set_window_size(1080, 1024)
driver.maximize_window()
driver.get("http://prod.danawa.com/list/?cate=112758")

# print(driver.page_source)

# 제조사별 더보기 클릭
# driver.find_element_by_css_selector("div.spec_opt_view button").click()
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.spec_opt_view button"))).click()
time.sleep(3)
# apple 클릭
driver.find_element_by_css_selector("#selectMaker_simple_priceCompare_A > li:nth-child(16)").click()
time.sleep(3)

# 하단의 제품 출력 => 1 ~ 6 page
cur_page, target_crawl_num = 1, 6
idx = 1

while cur_page <= target_crawl_num:
    # 전체 상품 목록 가져오기
    products = driver.find_elements_by_css_selector("div.main_prodlist_list > ul > li:not(.prod_ad_item)")

    # 현재 페이지 출력
    print("***** 현재 페이지 : {}".format(cur_page))


    for product in products:
        # 제품명, 가격, 이미지 주소
        product_name = product.find_element_by_css_selector("div.prod_info p a")
        product_price = product.find_element_by_css_selector("div.prod_pricelist p.price_sect a")
        product_img = product.find_element_by_css_selector("div.thumb_image img")

        if product_img.get_attribute("data-original"):
            img_src = product_img.get_attribute("data-original")
        else:
            img_src = product_img.get_attribute("src")

        # 프로토콜이 없는 경우
        if "http:" not in img_src:
            img_src = "http:" + img_src

        print(product_name.text, product_price.text, product_img.get_attribute("src"))

        idx += 1

    # 현재 페이지 번호 변경
    cur_page += 1

    if cur_page > target_crawl_num:
        print("Crawilng 성공")
        break

    # 다음 페이지 번호 클릭하기
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(cur_page)))).click()

    time.sleep(3)

driver.close()