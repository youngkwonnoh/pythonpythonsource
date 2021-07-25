import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

url = "http://www.encar.com/index.do"

try:
    response = req.urlopen(url)
    contents = response.read().decode("euc-kr")
except:
    print("에러발생")
else:
    print("type-{}".format(type(response)))  # <class 'http.client.HTTPResponse'>
    print("getUrl-{}".format(response.geturl()))
    print("status-{}".format(response.status))  # 200
    print("headers-{}".format(response.getheaders()))

    print(contents[:3000])
