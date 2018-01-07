#coding=utf-8

import urllib2
import ssl

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"

}
context = ssl._create_unverified_context()
url = "https://www.12306.cn/mormhweb/"

request = urllib2.Request(url, headers = headers,)
response = urllib2.urlopen(request,context = context)
print response.read()