import urllib.request as req

# google.com 메인 페이지 소스 다운로드
url = "https://www.google.com/"

# 다운로드 받을 파일 지정
save_url = "d:/google.html"

try:
    file1, header1 = req.urlretrieve(url, save_url)
except Exception as e:
    print(e)
else:
    print(header1)  # HTTPMessage
    print("성공")
