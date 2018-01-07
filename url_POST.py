# coding=utf-8

import urllib
import urllib2

# url为Fiddler中Raw里POST
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

headers = {
    "Host" : "fanyi.youdao.com",
    "Connection" : "keep-alive",
    "Content-Length" : "205",
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Cookie" : "OUTFOX_SEARCH_USER_ID=-1202414317@10.169.0.84; JSESSIONID=aaa0-lwOULfyggBjyIEbw; OUTFOX_SEARCH_USER_ID_NCOO=1528356411.8541896; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1513426624892",
    }

key = raw_input("输入需要翻译的文字 : ")

#Fiddler中WebForms
formdata = {
    "i" : key,
    "from" : "AUTO",
    "to" : "AUTO",
    "smartresult" : "dict",
    "client" : "fanyideskweb",
    "salt" : "1515207904777",
    "sign" : "a516df7f772a7e76563f8c3ea0cb3142",
    "doctype" : "json",
    "version" : "2.1",
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_REALTIME",
    "typoResult" : "false",
}

#对formdata进行编码
data = urllib.urlencode(formdata)
request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request).read()

print(response)