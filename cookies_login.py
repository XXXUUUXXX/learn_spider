# coding=utf-8

import urllib
import urllib2

url = "http://www.renren.com/882943860/profile"

#CookieJar()
headers = {
    "Host" : "www.renren.com",
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    #"Upgrade-Insecure-Requests" : "1",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Cookie" : "anonymid=jb9e2uncg2x8kq; depovince=GW; _r01_=1; JSESSIONID=abcENZIlmSSkI6NLqJFbw; ick_login=bb0d95c0-f5c9-433e-9d4a-cb899a7fe7b7; t=900375d63bb8c9e361730a7d55b597c30; societyguester=900375d63bb8c9e361730a7d55b597c30; id=882943860; xnsid=a0721697; jebecookies=deba795b-66f3-4227-891b-0c4d016a97f8|||||; ver=7.0; loginfrom=null; jebe_key=68064f1a-bf4a-4308-9887-10f387740f33%7Cb041f5d2bc3765df6757b09738184b0a%7C1513431625588%7C1%7C1513431625222; wp_fold=0",

}

#formdata = {}
#data = urllib.urlencode(formdata)
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
print response.read()