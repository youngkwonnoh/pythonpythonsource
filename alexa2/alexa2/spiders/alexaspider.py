import scrapy
from ..items import AlexaItem


class AlexaspiderSpider(scrapy.Spider):
    name = 'alexaspider'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://alexa.com/topsites/']

    def parse(self, response):
        for site in response.css("div.listings.table > div.tr.site-listing"):
            items = AlexaItem()
            # 순위
            items['rank_num'] = site.css("div.td::text").get()
            # 사이트명
            items['site_name'] = site.css("div.td.DescriptionCell > p > a::text").get()
            # daily_time_site
            items['daily_time_site'] = site.css("div.td.right > p::text").getall()[0]
            # daily_page_view
            items['daily_page_view'] = site.css("div.td.right > p::text").getall()[1]

            yield items
