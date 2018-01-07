# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentredisItem(scrapy.Item):
    # 职位名
    position_name = scrapy.Field()
    # 详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    position_num = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()