#coding=utf-8

import urllib2

# 代理开关，表示是否启用代理
proxyswitch = True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+port
# 私密代理{"http": "用户名:密码@IP:Port"}
httpproxy_handler = urllib2.ProxyHandler({"http":"123.161.16.174:9797"})

# 构建一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 构建一个全局的opener，之后所有的请求都可以用urlopen()方式去发送
# 也附带Handler的功能
urllib2.install_opener(opener)
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()