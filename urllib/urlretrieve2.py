import urllib.request as req

# 파일 URL
file_url = "https://t1.daumcdn.net/blogcolumn/_home/G/R/02NGR/1081242259302_443.jpg"

# 다음 메인페이지 URL
html_url = "https://www.daum.net/"

# 다운로드 받을 경로
save_img = "d:/dog.jpg"
save_html = "d:/daum.html"

try:
    file1, header1 = req.urlretrieve(file_url, save_img)
    file2, header2 = req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("다운로드 성공")
