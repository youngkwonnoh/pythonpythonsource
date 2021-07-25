from selenium import webdriver
import time

# 드라이버 로드
driver = webdriver.Chrome("./chromedriver/chromedriver")

# google.com => 새 창으로 naver.coms
driver.get("https://google.com")
print("현재 창 : ", driver.title)

# 자바스크립트로 새 창 열기
driver.execute_script("window.open('https://www.naer.com')")

# 현재 브라우저에 열린 모든 창의 정보
all_windows = driver.window_handles

# 자식 창 정보 가져오기
# for window in all_windows:
#       if window != parent_window
#           list.append()
child_window = [window for window in all_windows if window != parent_window][0]
print("child window ", child_window)

# 자식 창으로 제어권 이동
driver.switch_to.window(child_window)
print("현재 창 : ", driver.title)

driver.close()

# 부모 창으로 제어권 이동
driver.switch_to.window(parent_window)
print("제어권 이동 후 : ", driver.title)

time.sleep(2)

# 부모창 닫기
driver.close()