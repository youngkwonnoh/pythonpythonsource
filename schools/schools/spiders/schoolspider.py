import scrapy


class SchoolspiderSpider(scrapy.Spider):
    name = 'schoolspider'
    allowed_domains = ['www.w3schools.com']
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # menus = response.xpath('//*[@id="nav_tutorials"]/div/div/div[2]/a/text()').extract()
        menus = response.css('div#"nav_tutorials > div > div > div.w3-col a::text').extract()
        for i, menu in enumerate(menus):
            # print("{} : {}".format(i, menu))
            yield{
                "no":i,
                "menu":menu
            }