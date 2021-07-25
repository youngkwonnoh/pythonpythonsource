import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

# 파일 URL
url = "https://news.v.daum.net/v/20210709130546178"

try:
    response = req.urlopen(url).read().decode("utf-8")
except:
    print("에러발생")
else:
    print(response)
