# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanCrawlItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #编号
    num = scrapy.Field()
    #内容
    content = scrapy.Field()
    #链接
    url = scrapy.Field()
