# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from tencentredis.items import TencentredisItem
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


#class TtSpider(CrawlSpider):
class TtSpider(RedisCrawlSpider):
    name = 'tt'
    #allowed_domains = ['hr.tencent.com']
    #start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    redis_key = "ttspider:start_urls"


    def __init__(self, *args, **kwargs):
        domain = kwargs.pop("domain", "")
        self.allowed_domains = filter(None, domain.split(','))
        super(TtSpider,self).__init__(*args, **kwargs)


    # Response里链接的提取规则，返回符合匹配规则的链接对象的列表
    pagelink = LinkExtractor(allow=(r"start=\d+"))
    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定的回调函数
        Rule(pagelink, callback='parse_tencent', follow=True),

    ]

    # 指定的回调函数
    def parse_tencent(self, response):

        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentredisItem()
            # 职位名称
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['position_type'] = each.xpath("./td[2]/text()").extract()
            # 招聘人数
            item['position_num'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
