from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError

search_url = (
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&"
)

param = {"query": "영화"}

search_url = search_url + urlencode(param)

try:
    data = urlopen(search_url).read().decode("utf-8")
except URLError as e:
    print("URL Error")
else:
    print(data[150000:200000])
