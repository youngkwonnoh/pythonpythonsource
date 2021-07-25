from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../chromedriver/chromedriver")

driver.get("https://youtube.com/")

element = driver.find_element_by_name("search_query")

element.send_keys("아이유")

element.send_keys(Keys.RETURN)

titles = driver.find_elements_by_tag_name("h3")

for title in titles:
    print(title.text)

time.sleep(2)

driver.close()