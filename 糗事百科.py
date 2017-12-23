#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import json
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/2/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

request = urllib2.Request(url, headers = headers)

html = urllib2.urlopen(request).read()

# 响应返回的是字符串，解析为HTML DOM 模式
text = etree.HTML(html)

# 返回所有段子的节点位置，contains()模糊查询方法,第一个参数为要匹配的标签，第二个参数为标签名部分内容
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

items = {}
for node in node_list:
    # 用户
    username = node.xpath('./div/a/h2/text()')
    # 图片
    image = node.xpath('.//div[@class="thumb"]//@src')
    # 取出标签下的内容段子内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    # 点赞数量
    zan = node.xpath('.//i')[0].text
    # 评论数量
    comments = node.xpath('.//i')[1].text

    items = {
        "username" : username,
        "image" : image,
        "content" : content,
        "zan" : zan,
        "comments" : comments
    }

    with open("qiushi.json", "a") as f:
        f.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")
