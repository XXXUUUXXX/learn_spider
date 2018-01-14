# -*- coding: utf-8 -*-

import scrapy

import re

from taobao.items import TaobaoItem
from scrapy_redis.spiders import RedisSpider

class TbSpider(RedisSpider):
    name = 'tb'
    #allowed_domains = ['taobao.com']
    #start_urls = ['http://taobao.com/']
    redis_key = 'TbSpider:start_urls'

    # 搜索网址
    def parse(self, response):
        # https://s.taobao.com/search?q=%E6%98%BE%E5%8D%A1&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=88
        # 删除中间无用部分得到url = https://s.taobao.com/search?q=显卡&s=440
        key = raw_input("请输入要爬取的关键词：")
        pages = int(raw_input("请输入要爬取的页数："))

        print('正在爬取%s....' % key)

        for i in range(0, pages):
            url = 'https://s.taobao.com/search?q=' + key + '&s=' + str(44*i)
            yield scrapy.Request(url = url, callback = self.page)

    #店铺网址
    def page(self, response):
        #https://item.taobao.com/item.htm?spm=a230r.1.14.8.386afdaef9ZX8K&id=556614003310&ns=1&abbucket=7#detail
        #https://detail.tmall.com/item.htm?spm=a230r.1.14.1.386afdaef9ZX8K&id=555996623026&ns=1&abbucket=7
        #删除无用部分，得到最简淘宝url = https://item.taobao.com/item.htm?id=xxxxxx
        #天猫url = https://detail.tmall.com/item.htm?id=xxxxxx
        body = response.body.decode('utf-8', 'ignore')

        # 匹配id
        pattern_id = re.compile('"nid":"(.*?)"')
        all_id = pattern_id.findall(body)
        # 匹配地址
        pattern_address = re.compile('"item_loc": "(.*?)"')
        all_address = pattern_address.findall(body)

        for i in range(0, len(all_id)):
            this_id = all_id[i]
            now_price = all_now_price[i]
            address = all_address[i]
            url ="https://item.taobao.com/item.htm?id=" + str(this_id)
            yield scrapy.Request(url = url, callback = self.next, meta = {'now_price': now_price, 'address': address})

    # 爬取店铺页面的信息
    def next(self, response):
        item = TabobaoItem()

        url = response.url

        pattern_url = re.compile('https://(.*?).com')
        web = pattern_url.findall(url)

        if web[0] != 'item.taobao': # 天猫
            # 商品名称
            title = response.xpath('//div[@class="tb-detail-hd"]/h1/text()').extract()
            # 商品价格
            price = response.xpath('//span[@class="tm-price"]/text()').extract()
            # id
            pattern_id = 'id=(.*?)&'
            this_id = re.compile(pat_id).findall(url)[0]

        else: # 淘宝
            # 商品名称
            title = response.xpath('//h3[@class="tb-main-title"]/text()').extract()
            # 商品价格
            price = response.xpath('//em[@class="tb-rmb-num"]/text()').extract()
            # id
            pattern_id = 'id=(.*?)$'
            this_id = re.compile(pat_id).findall(url)[0]

        # 抓取评论总数
        comment_url = "https://rate.taobao.com/detailCount.do?itemId=" + str(this_id)
        comment_data = urllib2.urlopen(comment_url).read().decode("utf-8", 'ignore')
        each_comment = '"rateTotal":(.*?)'
        comment = re.compile(each_comment).findall(comment_data)

        item['title'] = title[0]
        item['link'] = url
        item['price'] = price[0]
        item['now_price'] = response.meta['now_price']
        item['comment'] = comment[0]
        item['address'] = response.meta['address']

        yield item
