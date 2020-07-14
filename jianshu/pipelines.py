# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class savePicPipeline(object):
    def process_item(self, item, spider):
        print('url============='+item['img_url'])
        return item


from scrapy.pipelines.images import ImagesPipeline  # 用于下载图片的管道
from scrapy import Request
from scrapy.exceptions import DropItem  # 异常库
import scrapy

class savePicPipeline(ImagesPipeline):
    # 用于下载图片的请求
    def get_media_requests(self, item, info):
        print(item['img_url'])
        yield Request(url=item['img_url'])