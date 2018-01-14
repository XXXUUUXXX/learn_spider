# -*- coding: utf-8 -*-
import scrapy

# 只要是需要提供post数据的，就可以用这种方法，
# 下面示例：post数据是账户密码

class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    #start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://renren.com/PLogin.do"
        yield scrapy.FormRequest(
                url = url,
                formdata = {"email": "xxx", "password": "xxx"},
                callback = self.parse_page
            )

    def parse_page(self, response):
        with open("ren1.html", "w") as filename:
            filename.write(response.body)