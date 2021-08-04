import scrapy


class Gspider4Spider(scrapy.Spider):
    name = 'gspider4'
    allowed_domains = ['corners.gmarket.co.kr']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06']

    def parse(self, response):
        # 컴퓨터/저자 1 ~ 100위 까지 제품의 url 추출
        # print(response.text)
        best_list = response.css("div.best-list ul li")[1]
        for url in best_list.css("li div a::attr('href')").getall():
            # print(idx, item)
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        print("parse_item", response.url)
        print("price : {}".format(response.css("p.price strong.price_real::text").get()))