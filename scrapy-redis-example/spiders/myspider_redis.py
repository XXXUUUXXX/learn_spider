# -*- coding:utf-8 -*-

#支持分布式抓取

#采用basic spider，需要写parse函数
#不再有start_urls，取代用redis_key,scrapy-redis将key从Redis里pop出来，成为请求的url地址
#不需要写allowed_domains和start_urls，__init__方法里动态定义了爬虫爬取域范围，也可直接写allowed_domains
#必须指定redis_key
#start_urls将在Master端的redis-cli里lpush到Redis数据库中，RedisSpider 将在数据库里获取start_urls。
#执行方式：
#1.通过runspider方法执行爬虫的py文件（也可以分次执行多条），爬虫（们）将处于等待准备状态：
#scrapy runspider myspider_redis.py
#2.在Master端的redis-cli输入push指令，参考格式：
#$redis > lpush myspider:start_urls http://www.dmoz.org/
#3.Slaver端爬虫获取到请求，开始爬取。

from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    # 启动所有slave端爬虫的指令，下面的格式是参考格式，建议采用这种格式
    redis_key = 'myspider:start_urls'

    # 指定爬去域范围
    #allowed_domains = ["dmoz.org"]

    # 动态获取爬取域范围
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
