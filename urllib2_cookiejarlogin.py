# -*- coding:utf-8 -*-

import urllib
import urllib2

import cookielib

# 通过CookieJar类构建一个CookieJar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)

# 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")]

# renren网登陆接口
url = "http://www.renren.com/PLogin.do"

# 通过谷歌浏览器在用户名和密码出点右键检查
# 需要登陆的账户密码
data = {"email":" ","password":" "}

#通过urlencode()编码转换
data = urllib.urlencode(data)

# 第一次是post请求，发送登录需要的参数，获取cookie
request = urllib2.Request(url, data = data)

# 发送第一次的post请求，生成登录后的cookie（如果登录成功）
response = opener.open(request)

# 第二次可以使get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
response_deng = opener.open("http://www.renren.com/882943860/profile")

# 获取登陆后才能访问的页面信息
print response_deng