# coding=utf-8

import urllib
import urllib2

def load_page(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url：爬取的url地址
        filename：处理的文件名
    """
    print "正在下载" + filename
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    request = urllib2.Request(url,headers = headers)
    return urllib2.urlopen(request).read()

def write_page(html,filename):
    """
        作用：将html内容写入本地
        html：服务器响应文件内容
    """
    print "正在保存" + filename
    # 文件写入
    with open(filename, "a") as f:
        f.write(html)
    print "-"*30

def tieba_spider(url, begin_page, end_page):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url：贴吧url的前部分
        begin_page：起始页
        end_page：结束页
    """
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        html = load_page(fullurl, filename)
        #print html
        write_page(html, filename)

if __name__ == '__main__':
    kw = raw_input("输入要爬取的贴吧名字：")
    begin_page = int(raw_input("输入起始页："))
    end_page = int(raw_input("输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    print fullurl
    tieba_spider(fullurl, begin_page, end_page)