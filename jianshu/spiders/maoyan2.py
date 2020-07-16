import scrapy
import re

from jianshu.items import JianshuItem



class Jianshu(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['douban.com/']
    start_urls = ['http://movie.douban.com/top250/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    def start_requests(self):
        url = 'http://movie.douban.com/top250/'

        yield scrapy.FormRequest(url, headers=self.headers,callback=self.parse)
    def parse(self, response):
        baseurl = 'https://movie.douban.com/top250/'
        # for i in range(0, 250, 25):
        #     print(url + str(i))
        #     yield scrapy.Request(url + str(i), headers=self.headers)
        item = JianshuItem()
        for each in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
            name = each.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()
            imgurl = each.xpath('./div/div[1]/a/img/@src').extract()

            item['img_url'] = imgurl[0]
            item['name'] = name[0]
            print(imgurl[0])
            print(name)
            yield item

        # 获取下一页的链接
        #
        # next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        next_url = response.xpath('//span[@class="next"]/a/@href').get()
        # print(baseurl+str(next_url))
        yield scrapy.Request(baseurl+str(next_url),callback=self.parse,dont_filter=True,headers=self.headers)
