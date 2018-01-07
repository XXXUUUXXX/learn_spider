# coding=utf-8

import urllib
import urllib2

url = "http://www.baidu.com/s?"

keyword = raw_input("请输入要查询的字符串:")

wd = {"wd": keyword}
headers = {"User-Agent": "Chorme...."}
wd = urllib.urlencode(wd)

fullurl = url + wd

print(fullurl)

request = urllib2.Request(fullurl,headers=headers)
response = urllib2.urlopen(request)
print response.read()