import scrapy


class ZytespiderSpider(scrapy.Spider):
    name = 'zytespider'
    allowed_domains = ['www.zyte.com/blog/']
    start_urls = ['http://www.zyte.com/blog/']

    def parse(self, response):
        # print(response.text)
        print(response.css('head > title::text').get())

        print(response.css("#_posts_grid-98-2233 > div > div > div.oxy-post-wrap > div > a::attr('href')").getall())
        print(response.css("#_posts_grid-98-2233 > div > div > div.oxy-post-wrap > div > a::text").getall())