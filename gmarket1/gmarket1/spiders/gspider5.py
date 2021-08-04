import scrapy
from ..items import Gmarket1Item

class Gspider5Spider(scrapy.Spider):
    name = 'gspider5'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        # 제품명
        titles = response.css('div.best-list ul:not(.plus) li a::text').getall()

        # 가격
        prices = response.css('div.item_price div.s-price strong span::text').getall()
        for idx, title in enumerate(titles, 0):
            # print("{} {}".format(title, prices[idx]))
            items = Gmarket1Item()
            items['title'] = title
            items['price'] = int(prices[idx].strip().replace("원", "").replace(",",""))
            yield items
