import scrapy
from ..items import ZyteItem

class Zytespider2Spider(scrapy.Spider):
    name = 'zytespider2'
    allowed_domains = ['www.zyte.com']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        # print(response.url)
        for url in response.css("div.oxy-posts > div > div.oxy-post-wrap div a::attr('href')").extract():
            # print(url)
            # 상대경로 -> 절대경로 (urljoin)
            # print(response.urljoin(url))

            # 재귀 순회
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_article)

    def parse_article(self, response):
        # print("parse_article ", response.url)
        # 블로그 기사 내용 추출
        contents = response.css("#blog-body span p::text").getall()
        # print(contents[:1000])

        item = ZyteItem()
        item['contents'] = ''.join(contents)

        yield item