# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComputerworldItem(scrapy.Item):

    title = scrapy.Field()
    contents = scrapy.Field()
    url = scrapy.Field()

