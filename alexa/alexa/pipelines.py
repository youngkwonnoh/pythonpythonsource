# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class AlexaPipeline:
    def process_item(self, item, spider):

        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem("순위가 40위 이상임")
