import requests

# s = requess.Session() ~ s.close()
with requests.Session() as s:
    param = {"name":"hong"}
    r = s.get("https://httpbin.org/get", params = param)