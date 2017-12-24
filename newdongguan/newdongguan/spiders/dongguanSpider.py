# -*- coding: utf-8 -*-
import scrapy

from newdongguan.items import NewdongguanItem


class DongdongSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 每一页里所有帖子的链接集合
        links = response.xpath('//div[@class="greyframe"]//a[@class="news14"]/@href').extract()
        # 迭代取出集合里的链接
        for link in links:
            # 提取列表里每个帖子里的链接，发送请求放到请求队列里，并调用parse_item来处理
            yield scrapy.Request(link, callback = self.parse_item)

        #页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 70000:
            self.offset += 30
            # 发送请求放到请求队列里，调用self.paese处理response
            yield scrapy.Requst(self.url + str(self.offset), callback = self.parse)


    # 处理每个帖子的response的内容
    def parse_item(self, response):
        item = NewdongguanItem()
        #标题
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        #编号
        item['num'] = item['title'].split(' ')[-1].split(":")[-1]
        # 内容,先使用有图片情况下的匹配规则，如果有内容，返回所有内容列表集合
        # 如果没有内容，返回空列表，则使用无图片情况下的匹配规则
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            # 列表格式变为字符串格式
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        #链接
        item['url'] = response.url

        # 交给管道
        yield item

