# -*- coding:utf-8 -*-

import urllib2

user = "test"

password = "123456"

webserver = "192.168.21.52"

# 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，第一个参数realm如果没有指定就写None后三个分别是站点IP，账户，密码
passwordMgr.add_password(None, webserver, user, password)

# HTTPBasicAuthHandler() HTTP基础验证处理器类
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)

# 构建自定义opener
opener = urllib2.build_opener(httpauth_handler)

request = urllib2.Request("http://"+webserver)
#response = opener.open(request)
#urllib2.install_opener()
response = urllib2.urlopen(request)

print response.read()