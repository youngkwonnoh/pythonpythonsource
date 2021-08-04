# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlexaItem(scrapy.Item):
    # 순위
    rank_num = scrapy.Field()
    # 사이트명
    site_name = scrapy.Field()
    # 페이지 머문 시간
    daily_time_site = scrapy.Field()
    # 페이지 뷰
    daily_page_view = scrapy.Field()
    # 파이프라인을 통과하는 item Field 저장
    is_pass = scrapy.Field()

