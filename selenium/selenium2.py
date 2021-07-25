from selenium import webdriver

driver = webdriver.Chrome("./chromedriver/chromedriver")
driver.implicitly_wait(3)

# 접속할 사이트
driver.get("https://www.daum.net")

print("session id ", driver.session_id)
print("title ", driver.title)
print("url ", driver.current_url)
print("cookies ", driver.get_cookies())

driver.close()