# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import openpyxl


class Alexa2Pipeline:

    def __init__(self):
        # 엑셀 처리 사전 작업
        self.workbook = openpyxl.Workbook()

        # 기본 시트 활성화
        self.worksheet = self.workbook.active
        self.worksheet.column_dimensions['A'].witdh = 10
        self.worksheet.column_dimensions['B'].witdh = 15
        self.worksheet.column_dimensions['C'].witdh = 15
        self.worksheet.column_dimensions['D'].witdh = 20
        self.worksheet.column_dimensions['E'].witdh = 10
        
        # 엑셀 필드명
        self.worksheet.append(['rank_num', 'site_name', 'daily_time', 'daily_page_view', 'is_pass'])

    def process_item(self, item, spider):

        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True

            # 엑셀 저장
            rank_num = item['rank_num'] # item.get('rank_num')
            site_name = item.get('site_name')
            daily_time = item.get('daily_time_site')
            daily_page_view = item.get('daily_page_view')
            is_pass = item.get('is_pass')

            self.worksheet.append([rank_num, site_name, daily_time, daily_page_view, is_pass])

            return item

        else:
            raise DropItem("순위가 40위 이상임")

    def close_spider(self, spider):
        self.workbook.save("../alexa2/best40.xlsx")

        self.workbook.close()