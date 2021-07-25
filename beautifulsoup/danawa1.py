from logging import info
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 로그인 할 때 보내는 formData
login_info = {
    "redirectUrl" : "http://www.danawa.com/",
    "loginMemberType" : "general",
    "id" : "i03man",
    "isSaveId" : "true",
    "password" : "dudtka@^86"
}

headers = {
    "user-agent" : UserAgent().chrome,
    "Referer" : "https://auth.danawa.com/login/login?url=http%3A%2F%2Fwww.danawa.com%2F"
}

with requests.Session() as s:
    response = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    # print(response.content.decode("utf-8"))

    # 로그인 성공 => 주문 / 배송 조회
    response = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)

    # print(response.text)

    soup = BeautifulSoup(response.content, "html.parser")
    # check_id = soup.find("p", class_="user")
    # print(check_id)

    info_list = soup.select("ul.info_list > li")
    # print(info_list)
    for item in info_list:
        proc, val = item.find("span").string, item.find("strong").string.strip()
        print("{} : {}".format(proc, val))