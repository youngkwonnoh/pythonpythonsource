import requests

from fake_useragent import UserAgent

userAgent = UserAgent()

headers = {
    'user-agent':userAgent.chrome
}

with requests.Session() as s:
    r = s.get("https://httpbin.org/get", headers=headers)
    print(r.text)