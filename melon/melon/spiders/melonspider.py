import scrapy


class MelonspiderSpider(scrapy.Spider):
    name = 'melonspider'
    allowed_domains = ['www.melon.com/chart/index.htm']
    start_urls = ['https://www.melon.com/chart/index.htm']

    def parse(self, response):
        # print(response.text)

        songs = response.css("tbody > tr")

        idx = 1

        for song in songs:
            # 노래명
            title = song.css('td:nth-child(4) div.ellipsis a::text').get()
            # 가수명
            singer = song.css('td:nth-child(4) div.rank02 a::text').get()
            # 앨범명
            album = song.css('td:nth-child(5) div.rank03 a::text').get()

            print(idx, singer, title, album)
            idx += 1