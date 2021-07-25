from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org/"

# url = api + "?" + "format=json"
values = {"format": "json"}

url = api + "?" + urlencode(values)
print("요청 URL ", url)

response = urlopen(url).read().decode("utf-8")
print(response)
