import scrapy
from ..items import GlobalvoicesItem


class GlobalspiderSpider(scrapy.Spider):
    name = 'globalspider'
    allowed_domains = ['globalvoices.org']
    start_urls = ['http://globalvoices.org/']

    def parse(self, response):
        # 기사 제목 추출

        for idx, headline in enumerate(response.css("h3.post-title a::text").getall(), 1):
            items = GlobalvoicesItem()
            items['idx'] = idx
            items['headline'] = headline

            yield items