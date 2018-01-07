# -*- coding:utf-8 -*-

import urllib2
import re

class Spider(object):
    def __init__(self):
        # 初始化起始页位置
        self.page = 1
        # 爬取开关，如果为True继续爬取
        self.switch = True

    def loadPage(self):
        """下载页面"""
        print "正在下载数据。。。"
        if self.page != 1:
            url = "http://www.neihan8.com/article/index_" + str(self.page) + ".html"
        else:
            url = "http://www.neihan8.com/article/"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)

        # 获取每页HTML源码字符串
        html = response.read()

        # 创建正则表达式规则对象，匹配每页里面段子内容，re.S表示匹配全部字符串
        pattern = re.compile(r'<div\sclass="desc">(.*?)</div>',re.S)

        # 将正则匹配对象应用到html源码字符串里，返回这个页面所有段子的列表
        content_list = pattern.findall(html)

        # 调用dealPage()处理段子里的符号
        self.dealPage(content_list)

    def dealPage(self, content_list):
        """处理每页段子，content_list为每页段子列表集合"""
        for item in content_list:
            # 处理段子，替换无用数据
            item = item.replace("&amp;", "")
            #print item
            # 调用writePage()将段子写入文件
            self.writePage(item)

    def writePage(self, item):
        """把每条段子逐个写入文件，item:处理后的段子"""
        # 写入文件
        print "正在写入数据。。。"
        with open("duanzi.txt", "a") as f:
            f.write(item)

    def startWork(self):
        """控制爬虫运行"""
        # 循环执行，直到 self.swith == False
        while self.switch:
            # 确定爬取次数
            command = raw_input("如果继续爬取，请按回车（退出输入quit）")
            if command == "quit":
                self.switch = False
            else:
                self.loadPage()
                self.page += 1
        print "使用完毕。。。谢谢使用"


if __name__ == '__main__':
    duanziSpider = Spider()
    #duanziSpider.loadPage()
    duanziSpider.startWork()