from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError

# ctxCd=1001 or ctxCd=1012 or ctxCd=1013 or ctxCd=1014
# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012

api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []  # list()

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))  # dict(키=value)

# 확인
# print(params)

for c in params:
    param = urlencode(c)

    # url 완성
    api = api + "?ctxCd" + param

    # 요청
    data = urlopen(api).read().decode("utf-8")

    # 출력
    print("-" * 100)
    print(data)
