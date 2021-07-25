import requests

with requests.Session() as s:
    r = s.get('https://jsonplaceholder.typicode.com/users')
    
    # print("json : {}".format(r.json()))
    for line in r.json():
        for k, v in line.items():
            print("{} : {}".format(k,v))
        print()
