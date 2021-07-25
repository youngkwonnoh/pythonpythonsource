import requests

with requests.Session() as s:
    r = s.get('https://jsonplaceholder.typicode.com/todos/1')
    print("headers : {}".format(r.headers))
    print("json : {}".format(r.json()))
    print("json key : {}".format(r.json().keys()))
    print("json values : {}".format(r.json().values()))
