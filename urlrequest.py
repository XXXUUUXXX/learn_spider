import urllib2

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
request = urllib2.Request("http://www.baidu.com/", headers=ua_headers)
response = urllib2.urlopen(request)
html = response.read()
print response.getcode()
print response.geturl()
print response.info()
# print(html)