import requests

res = requests.get("https://www.naver.com")

print(res.text)
print(res.encoding)  # UTF-8
print(res.status_code)
print(res.headers["content-type"])
