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
    name = 'newsspider2'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 크롤링 규칙(정규표현식 사용 추천)
    rules = [
        # 2 ~ 9 페이지까지 크롤링
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline')
    ]

    # start_irls는 무조건 parse() 호출하도록 되어 있어서 변경
    def parse_start_url(self, response):
        return self.parse_parent(response)

    def parse_parent(self, response):
        print("response url {}".format(response.url))
    
        # 타이틀 / 약간의 내용 추출
        for news in response.css("ul.list_news2.list_allnews > li > div"):
            # 주소 추출
            article_url = news.css("strong > a::attr(href)").get().strip()

            # meat : 다른 메소드로 넘겨줘야 할 파라메터 작성
            # dont_filter:True => self.parse_child를 동작시켜줄 때 필요
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url':response.url}, dont_filter=True)

    def parse_child(self, response):
        print("Parent Response URL : %s" % response.meta['parent_url'])
        print("Child Response URL : %s" % response.url)
