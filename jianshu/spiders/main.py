# _*_ coding: utf-8 _*_

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('D:\jianshu\jianshu\spiders\jianshuSpider.py'))) #设置工程目录
print(os.path.dirname(os.path.abspath('D:\jianshu\jianshu\spiders\jianshuSpider.py')))

execute(["scrapy","crawl","movie"]).strip()