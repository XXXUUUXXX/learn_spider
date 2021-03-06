# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItcastPipeline(object):
    # __init__方法是可选的，作为类的初始化方法
    def __init__(self):
        super(ItcastPipeline, self).__init__()
        # 创建一个文件
        self.filename = open("teacher.json", "w")

    # process_item方法必须写，用来处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii = False) + '\n'
        self.filename.write(jsontext.encode("utf-8"))
        return item

    # close_spider方法是可选的，结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()