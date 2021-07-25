from fake_useragent import UserAgent

# 객체 생성
userAgent = UserAgent()

# 브라우저 생성
print(userAgent.ie)
print(userAgent.msie)
print(userAgent.chrome)
print(userAgent.safari)
print(userAgent.opera)
print(userAgent.firefox)
print(userAgent.random)
