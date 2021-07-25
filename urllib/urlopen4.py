import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

# 파일 URL
file_url = [
    "https://www.daum.net/",
    "https://t1.daumcdn.net/blogcolumn/_home/G/R/02NGR/1081242259302_443.jpg",
]

# 저장 경로 지정
path_list = ["d:/daum1.html", "d:/dog1.jpg"]

for i, url in enumerate(file_url):
    try:
        response = req.urlopen(url)
        contents = response.read()

        # 파일 저장 (wb-write byte)
        with open(path_list[i], "wb") as c:
            c.write(contents)
    except:
        print("에러발생")
    else:
        print("headers info-{}:{}".format(i, response.info()))
        print()
        print("-----------------------------------------")

        print(contents.decode("utf-8")[:3000])
