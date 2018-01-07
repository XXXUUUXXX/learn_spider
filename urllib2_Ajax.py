# coding=utf-8

import urllib
import urllib2

url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

formdata ={
    "sort" : "T",
    "range" : "0,10",
    "tags"  : "电影",
    "start" : "0",
}
data = urllib.urlencode(formdata)
request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)
print(response).read()