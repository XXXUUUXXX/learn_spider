# -*- coding:utf-8 -*-

import threading # 线程
from Queue import Queue # 队列
from lxml import etree # 解析库
import requests # 请求处理
import json # json处理
import time

class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName# 线程名
        self.pageQueue = pageQueue# 页码队列
        self.dataQueue = dataQueue# 数据队列
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

    def run(self):
        print("启动" + self.threadName)
        while not CARWL_EXIT:
            try:
                # 取出一个数字，先进先出
                # 可选参数block默认值为True
                # 1.如果队列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                # 2.如果队列为空，block为False的话，就弹出一个Queue.empty()异常
                page = self.pageQueue.get(False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                #print url
                content = requests.get(url, headers = self.headers).text
                time.sleep(1)
                self.dataQueue.put(content)
                #print len(content)
            except:
                pass
        print("结束" + self.threadName)

class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename, lock):
        super(ThreadParse, self).__init__()
        self.threadName = threadName# 线程名
        self.dataQueue = dataQueue# 数据队列
        self.filename = filename# 保存解析后的数据文件名
        self.lock = lock# 锁

    def run(self):
        print("启动" + self.threadName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print("退出" + self.threadName)

    def parse(self, html):
        # 解析为HTML DOM
        html = etree.HTML(html)

        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

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

            # with后面有两个必须执行的操作：__enter__和__exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with self.lock:
                # 写入存储的解析后的数据
                self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")

CARWL_EXIT = False
PARSE_EXIT = False

def main():
    # 页码的队列，表示10个页面
    pageQueue = Queue(20)
    # 放入1~20的数字，先进先出
    for i in range(1, 21):
        pageQueue.put(i)

    # 采集结果（每页的HTML源码）的数据队列，参数为空表示不限制
    dataQueue = Queue()

    filename = open("duanzi.json", "a")
    # 创建锁
    lock = threading.Lock()

    # 三个采集线程的名字
    crawlList = ["采集线程1号", "采集线程2号", "采集线程3号"]
    # 存储三个采集线程的列表集合
    threadcrawl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)

    # 三个解析线程名字
    parseList = ["解析线程1号","解析线程2号", "解析线程3号"]
    # 存储三个解析线程
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName, dataQueue, filename, lock)
        thread.start()
        threadparse.append(thread)

    # 等待pageQueue队列为空，也就是等待之前的操作执行完毕
    while not pageQueue.empty():
        pass

    # 如果pageQueue为空，采集线程退出循环
    global CARWL_EXIT
    CARWL_EXIT = True

    print "pageQueue为空"

    for thread in threadcrawl:
        thread.join()
        print("----采集----")

    while not dataQueue.empty():
        pass

    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in threadparse:
        thread.join()
        print("----解析----")

    with lock:
        # 关闭文件
        filename.close()
    print("谢谢使用")


if __name__ == '__main__':
    main()