from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver/chromedriver")

driver.get("https://python.org")

print(driver.current_url)
print(driver.title)

# 화면크기 제어
# driver.maximize_window()

# 소스 가져오기
print(driver.page_source)

time.sleep(3)

driver.quit()