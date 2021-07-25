# 코로나라는 검색어를 넣고 유사도 순으로 10개 정보 추출

import requests

def main():
    naver_open_api = "https://openapi.naver.com/v1/search/news.json"
    client_id = "leGsP8qRkpbjI0nLpp46"
    client_secret = "scdVFJnVO4"

    headers = {
        "X-Naver-Client-Id" : client_id,
        "X-Naver-Client-Secret" : client_secret
    }

    params = {
        "query" : "코로나",
        "display" : 10,
        "start" : 1,
        "sort" : "sim"
    }

    response = requests.get(naver_open_api, headers = headers, params = params)
    get_news(response.json())

def get_news(data):
    print(data)

if __name__ == "__main__":
    main()