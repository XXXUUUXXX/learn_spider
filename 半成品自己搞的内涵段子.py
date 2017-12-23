# -*- coding:utf-8 -*-

import urllib2
import re

class Spider(object):
    """dtring for Spider"""
    def __init__(self ):
        super(Spider, self).__init__()
        # 初始化起始页位置
        self.page = 1
        # 爬取开关，如果为True继续爬取
        self.switch = True

    def loadPage(self):
        """下载页面"""
        if self.page != 1:
            url_index = "http://www.neihan8.com/article/index_" + str(self.page) + ".html"
        else:
            url_index = "http://www.neihan8.com/article/"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        request_index = urllib2.Request(url_index, headers = headers)
        response_index = urllib2.urlopen(request_index)

        # 获取每页HTML源码字符串
        html_index = response_index.read()

        # 正则表达式匹配具体段子URL
        pattern = re.compile(r'/article/\d*\.html', re.S)
        url_list = pattern.findall(html_index)
        # 具体段子的URL
        for ulist in url_list:
            url_duanzi = "http://www.neihan8.com" + ulist
            #print url_duanzi

            request_duanzi = urllib2.Request(url_duanzi, headers = headers)
            response_duanzi = urllib2.urlopen(request_duanzi)

            # 获取每页HTML源码字符串
            html_duanzi = response_duanzi.read()

            pattern = re.compile(ur'<div\sid="con_all">(.*?)</div>',re.S)
            content_list = pattern.findall(html_duanzi)
            #print content_list

        self.dealPage(content_list)

    def dealPage(self, content_list):
        """处理每页段子"""
        for item in content_list:
            item = item.replace("&amp;", "")
            #print item

    def writePage(self):
        """把每条段子逐个写入文件"""

    def startWork(self):
        """控制爬虫运行"""


if __name__ == '__main__':
    duanzi_spider = Spider()
    duanzi_spider.loadPage()