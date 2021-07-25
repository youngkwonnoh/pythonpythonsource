import requests

s = requests.Session()

# get 방식
# r = s.get("http://httpbin.org/get")
# print(r.text)

# post 방식
data = {
    "name":"hong"
}
r = s.post("http://httpbin.org/get", data=data)
print(r.text)

# delete 방식
r = s.delete("https://httpbin.org/delete")
print(r.text)

# put 방식(patch)
data = {
    "name":"hong"
}
r = s.put("http://httpbin.org/get", data=data)
print(r.text)

s.close()