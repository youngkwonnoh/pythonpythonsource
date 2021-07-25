import requests

# 다음쇼핑 best100 제품 요청하기

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1626140588318"

with requests.Session() as s:
    r=s.get(url)

    # 전체 보기
    # for product in r.json():
    #     for k, v in product.items():
    #         print("{} : {}".format(k,v))
    #     print()
    
    
    # for product in r.json():
    #     print("{} : {}".format(product.get("docid"), product.get("product_name")))

    for idx, product in enumerate(r.json()):
        print("{}:{}-{}".format(idx+1, product.get("product_name"), product['price_max']))
        # product.get("product_name") : 값이 없으면 None 푯기
        # product['price_max'] : 값이 없으면 에러남