import urllib.request as requset


movie_info = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20210711"

# 다운로드 받아서 파일로 저장하는 코드
try:
    data = requset.urlopen(movie_info).read().decode("utf-8")
except:
    print("에러 발생")
else:
    with open("c:/test/movie.txt", "w") as f:
        f.write(data)
