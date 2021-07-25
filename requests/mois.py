import requests

# urlparse3.py 변경
api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []  # list()

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))  # dict(키=value)

with requests.Session() as s:

    for param in params:
        # 요청
        r = s.get(api, params=param)

        # 출력
        print("-" * 100)
        print(r.text)