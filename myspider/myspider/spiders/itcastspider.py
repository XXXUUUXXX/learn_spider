# -*- coding: utf-8 -*-

import scrapy
from myspider.items import ItcastItem

# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcastspider'
    # 允许爬虫作用的范围
    allowed_domains = ["http://www.itcast.cn/"]
    # 爬虫从这里开始抓取数据
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        #with open("teacher.html", "w") as f:
        #    f.write(response.body)
        # 通过scrapy自带的xpath匹配出所有老师打根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 所有老师信息打列表集合
        #teacher_item = []

        # 遍历根节点集合
        for each in teacher_list:

            # Item对象用来保存数据
            item = ItcastItem()
            # name, extract()将匹配出来的结果转换为unicode字符串
            # 不加extract()结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            #item['name'] = name[0].encode("gbk")
            #item['title'] = title[0].encode("gbk")
            #item['info'] = info[0].encode("gbk")

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            #将获取打数据交给pipelines
            yield item

            #teacher_item.append(item)

            #print(name[0])
            #print(title[0])
            #print(info[0])

        # 返回数据,不经过pipeline
        #return teacher_item



