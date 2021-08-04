import scrapy


class Gspider2Spider(scrapy.Spider):
    # 스파이더 명(중복은 안됨)
    name = 'gspider2'
    # 크롤링이 허용된 도메인들(기록이 안되어 있다면 크롤링이 안됨)
    allowed_domains = ['www.gmarket.co.kr', 'naver.com', 'daum.net']
    
    # start_urls에 기록된 url에 대한 요청을 생성하는 start_request()가 호출되어
    # 크롤링을 시작하고 결과에 대해서 parse() 함수가 호출됨
    start_urls = ['http://www.gmarket.co.kr', 'https://www.naver.com', 'https://www.daum.net']

    def parse(self, response):
        print(response)
