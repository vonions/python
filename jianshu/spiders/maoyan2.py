import scrapy
import re

from jianshu.items import JianshuItem


class Jianshu(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['http://movie.douban.com/top250/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'channel': 'notification:user: 219500769',
        'auth': '219500769_1594891656:5deda819983d322877d01d20bc46b3a73ceda73f'
    }

    def start_requests(self):
        url = 'http://movie.douban.com/top250/'

        yield scrapy.FormRequest(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        baseurl = 'https://movie.douban.com/top250/'
        # for i in range(0, 250, 25):
        #     print(url + str(i))
        #     yield scrapy.Request(url + str(i), headers=self.headers)
        # item = JianshuItem()
        for each in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
            title = each.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()
            imgurl = each.xpath('./div/div[1]/a/img/@src').extract()

            # item['img_url'] = imgurl[0]
            # item['name'] = name[0]
            url = imgurl[0]
            name = title[0]
            # print(imgurl[0])
            # print(name)
            # 详情链接
            detail = each.xpath('./div/div[2]/div[1]/a/@href').extract()[0]
            # detail=each.xpath('//div[@class="pic"]/a/@href').get()
            # print(detail)

            yield scrapy.Request(url=detail, callback=self.parse_detail, dont_filter=True, headers=self.headers,
                                 meta={'name': name, 'url': url})
            # yield item

        # 获取下一页的链接
        #
        next_url = response.xpath('//span[@class="next"]/a/@href').get()
        yield scrapy.Request(baseurl + str(next_url), callback=self.parse, dont_filter=True, headers=self.headers)

    # 进入详情页
    def parse_detail(self, response):
        item = JianshuItem()
        item['name'] = response.meta['name']
        item['img_url'] = response.meta['url']
        summer = response.xpath('//*[@id="link-report"]/span[1]/text()').extract()[0]
        # //*[@id="link-report"]/span[1]
        # 查看全文
        # //*[@id="link-report"]/span[1]/span/text()
        title = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/h2/i/text()').extract()
        print(title)
        print(item['name'])
        print(response)
        print(summer)
        item['name2'] = summer
        yield item
