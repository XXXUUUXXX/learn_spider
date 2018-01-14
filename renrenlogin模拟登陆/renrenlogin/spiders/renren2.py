# -*- coding: utf-8 -*-
import scrapy

# 正统模拟登录方法：
# 首先发送登录页面的get请求，获取到页面里的登录必须的参数
# 然后和账户密码一起post到服务器，登录成功

class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {'email': 'xxx', 'password': 'xxx'},
                callback = self.parse_page
            )

    def parse_page(self, response):
        url = "http://www.renren.com/882946828/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    def parse_newpage(self, response):
        with open("ren2.html", "w") as filename:
            filename.write(response.body)

