import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

weather_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

# data = req.urlopen(weather_url).read()

# text = data.decode("utf-8")

text = req.urlopen(weather_url).read().decode("utf-8")
print(text[:1000])
