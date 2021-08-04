import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ItnewsItem

# CrawlSpider : 특정 규칙 집합을 정의하여 링크를 따라가는 매커니즘 제공
#               일반 웹 사이트를 크롤링 할 때 많이 사용됨
# http://news.daum.net/breakingnews/digital
# http://news.daum.net/breakingnews/digital?page=2
# http://news.daum.net/breakingnews/digital?page=3
class NewsspiderSpider(CrawlSpider):
    name = 'newsspider'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 크롤링 규칙(정규표현식 사용 추천)
    rules = [
        # 2 ~ 9 페이지까지 크롤링
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline')
    ]

    # start_irls는 무조건 parse() 호출하도록 되어 있어서 변경
    def parse_start_url(self, response):
        return self.parse_headline(response)

    def parse_headline(self, response):
        print("response url {}".format(response.url))
    
        # 타이틀 / 약간의 내용 추출
        for news in response.css("ul.list_news2.list_allnews > li > div"):
            # 타이틀
            headline = news.css("strong > a::text").get().strip()

            # 약간의 본문
            contents = news.css("div > span::text").extract_first().strip()

            yield ItnewsItem(headline=headline, contents=contents)
