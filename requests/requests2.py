import requests

s = requests.Session()

res = s.get("https://www.naver.com")

# print(res.text) # text : text 형태의 응답, content : binary 형태의 응답
print(res.encoding)  # UTF-8
print(res.status_code)
print(res.headers["content-type"])

# 세션 종료(브라우저 닫기)
s.close()
