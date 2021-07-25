import urllib.request as request
from fake_useragent import UserAgent
import json
import csv

# 객체 생성
UserAgent = UserAgent()

# 헤더 생성
headers = {
    "User-agent": UserAgent.chrome,
    "referer": "https://finance.daum.net/",  # 이전페이지에 대한 정보
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

response = request.urlopen(request.Request(url, headers=headers)).read().decode("utf-8")

# print(response)

rank_json = json.loads(response)["data"]

# csv 저장

data = []
for item in rank_json:
    print(
        "순위 : {}, 금액 : {}, 회사명 : {}".format(
            item["rank"], item["tradePrice"], item["name"]
        )
    )
    data.append(item)

    # txt, csv 저장
    with open("c:/test/finance.txt", "a") as f1, open(
        "c:/test/finance.csv", "w", newline=""
    ) as f2:
        f1.write(
            "순위 : {}, 금액 : {}, 회사명 : {}\n".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )
        output = csv.writer(f2)
        output.writerow(data[0].keys())  # header 명
        for row in data:
            output.writerow(row.values())
