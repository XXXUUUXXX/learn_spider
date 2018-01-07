# -*- coding:utf-8 -*-

#通常使用这个方法编写深度聚焦爬虫
#支持分布式爬取

#遵守Rule规则，callback不能写parse()方法
#不需要写allowd_domains和start_urls,使用redis_key
#执行方式：
#1.通过runspider方法执行爬虫的py文件（也可以分次执行多条），爬虫（们）将处于等待准备状态：
#scrapy runspider mycrawler_redis.py
#2.在Master端的redis-cli输入push指令，参考格式：
#$redis > lpush mycrawler:start_urls http://www.dmoz.org/
#3.爬虫获取url，开始执行。


from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
