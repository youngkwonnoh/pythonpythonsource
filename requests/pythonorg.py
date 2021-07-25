# python.org
import requests

with requests.Session() as s:
        # 요청
        r = s.get("https://www.python.org/")
        # 출력
        print(r.text)
