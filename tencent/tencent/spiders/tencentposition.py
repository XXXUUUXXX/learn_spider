# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = "tencentposition"
    allowed_domains = ["tencent.com"]

    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('(//tr[@class="even"]|//tr[@class="odd"])'):
            # 初始化模型对象
            item = TencentItem()
            # 职位名
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

            # 将数据交给管道文件处理
            yield item

        if self.offset < 1680:
            self.offset += 10
        #else:
        #    break
        #每次处理完一页的数据之后，重新发送下一页页面请求
        # 将请求重新发送给调度器入队列，出对列，交给下载器下载，调用self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)


