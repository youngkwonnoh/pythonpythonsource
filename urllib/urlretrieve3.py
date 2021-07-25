import urllib.request as req

# 사진 가져오기

url = "https://postfiles.pstatic.net/MjAyMDA0MTFfMjM2/MDAxNTg2NTkyNzM2NTM4.GlmJibi5_ZwdXWRdt6i5MqdrMpfygipFCONH-zK2My4g.F9nTe-5GEV1JNUoJ728CrLlLkXVPCXAmcMoLDj_RBYUg.JPEG.bosspass70/1586592735483.jpg?type=w966"


# 다운로드 받을 경로
save_path = "d:/dog.jpg"

try:
    file1, header1 = req.urlretrieve(url, save_path)
except Exception as e:
    print(e)
else:
    print(header1)
    print("다운로드 성공")
