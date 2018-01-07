# coding=utf-8

import urllib

url = "http://www.baidu.com/s?"
wd = {"wd": "百度"}
#编码
urlencode = urllib.urlencode(wd)

print urlencode
#解码
print(urllib.unquote(urlencode))