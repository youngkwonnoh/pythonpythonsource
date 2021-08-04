import scrapy


class Gspider1Spider(scrapy.Spider):
    name = 'gspider1'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        # titles = response.css('div.best-list li a::text').getall()
        titles = response.css('div.best-list ul:not(.plus) li a::text').getall()

        for idx, title in enumerate(titles, 1):
            print("{}. {}".format(idx, title))
            yield {
                "no": idx,
                "title": title
            }
