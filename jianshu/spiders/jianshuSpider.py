import scrapy
import re

from jianshu.items import JianshuItem


# 删除废弃
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

        yield scrapy.FormRequest(url, headers=self.headers,callback=self.parse)
    # //*[@id="content"]/div/div[1]/ol/li[23]/div/div[2]/div[1]/a/span[1]
    # //*[@id="content"]/div/div[1]/ol/li[23]/div/div[2]/div[1]/a/span[2]
    # //*[@id="content"]/div/div[1]/div[2]/span[3]/a

    def parse(self, response):
        baseurl = 'https://movie.douban.com/top250/'
        # for i in range(0, 250, 25):
        #     print(url + str(i))
        #     yield scrapy.Request(url + str(i), headers=self.headers)
        item = JianshuItem()
        for each in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
            name = each.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()
            imgurl = each.xpath('./div/div[1]/a/img/@src').extract()
            # imgurl = each.xpath('./div/div[1]/a/img').extract()
            # print(imgurl[0])
            # img=re.findall('src="(.*?)"',imgurl[0])
            # print(img)

            item['img_url'] = imgurl[0]
            item['name'] = name
            # print(name)
            # yield item

        # //*[@id="content"]/div/div[1]/div[2]/span[3]/a
        # //*[@id="content"]/div/div[1]/div[2]/span[3]/a

        #//*[@id="content"]/div/div[1]/div[2]/a[1]
        # 获取下一页的链接
        #
        # next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        next_url = response.xpath('//span[@class="next"]/a/@href').get()

        # print(111)
        # nexturl=response.xpath()
        # yield scrapy.Request(url + str(i), headers=self.headers)
        # if next_url:
        #     return
        # else:
        # tmp_url = baseurl+next_url

        # print('tmp_url=',tmp_url)

        # meta = {'url': tmp_url}
        print(baseurl+str(next_url))
        yield scrapy.FormRequest(baseurl+str(next_url), headers=self.headers, callback=self.parse,dont_filter=True)

    # def parseItem(self,response):
    #     print('parseItem')

        # print('item_url=',response.meta['url'])