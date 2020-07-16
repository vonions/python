# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

import sqlite3


class savePicPipeline(object):

    #   保存json 格式
    #     def __init__(self):
    #         # 保存json
    #         self.file = open('novel.json', 'wb')
    #
    #     def process_item(self, item, spider):
    #         line = json.dumps(dict(item)) + "\n"
    #         self.file.write(line.encode('utf-8'))
    #         sqlite3.connect('test.db')
    #         print("Opened database successfully")
    #         return item
    #
    #  下载图片
    # from scrapy.pipelines.images import ImagesPipeline  # 用于下载图片的管道
    # from scrapy import Request
    # from scrapy.exceptions import DropItem  # 异常库
    # import scrapy
    #
    #
    # class savePicPipeline(ImagesPipeline):
    #     # 用于下载图片的请求
    #     def get_media_requests(self, item, info):
    #         print(item['img_url'])
    #         yield Request(url=item['img_url'])

    # 保存sqlite
    def __init__(self):
        print('------------------------')
    def open_spider(self,spider):
        self.db_conn=sqlite3.connect('swt.db')
        self.db_cur=self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self,spider):
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self,item,spider):
        self.insert_db(item)
        return item
    # 插入数据
    def insert_db(self,item):
        values=(item['name'],item['img_url'])
        print(values)
        # sql = '''INSERT INTO MOVIE('name','url') VALUES(?,?)'''
        # self.db_conn.execute("INSERT INTO MOVIE VALUES (?,?)",(item['name'],item['img_url']));
        self.db_conn.execute("INSERT INTO MOVIE('name','url') VALUES (?,?)",values);
        # self.db_cur.execute(sql, values)

        self.db_conn.commit()
