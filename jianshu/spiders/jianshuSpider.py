import scrapy
import re

from jianshu.items import JianshuItem


class Jianshu(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/img
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/img
    # //*[@id="content"]/div/div[1]/ol/li[3]/div/div[1]/a/img
    # //*[@id="content"]/div/div[1]/ol/li[7]/div/div[1]/a/img
    # //*[@id="content"]/div/div[1]/ol/li[4]/div/div[2]/div[1]/a/span[1]

    def start_requests(self):
        url = 'http://movie.douban.com/top250/'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = JianshuItem()
        for each in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
            # print(each.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract())
            imgurl = each.xpath('./div/div[1]/a/img/@src').extract()
            # imgurl = each.xpath('./div/div[1]/a/img').extract()
            # print(imgurl[0])
            # img=re.findall('src="(.*?)"',imgurl[0])
            # print(img)

            item['img_url'] = imgurl[0]
            yield item
