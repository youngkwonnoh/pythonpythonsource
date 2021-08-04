import scrapy


class Gspider3Spider(scrapy.Spider):
    # 스파이더 명(중복은 안됨)
    name = 'gspider3'

    def start_requests(self):
        yield scrapy.Request('http://www.gmarket.co.kr', self.parse)
        yield scrapy.Request('https://www.naver.com', self.parse)
        yield scrapy.Request('https://www.daum.net', self.parse)

    def parse(self, response):
        # print(response.url)

        if response.url.find('gmarket'):
            yield {
                'sitemap' : response.url,
                'contents' : response.text[:1000]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
