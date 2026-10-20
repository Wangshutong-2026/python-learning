# 1.网络请求
# https://www.baidu.com   -- url统一资源定位符
from email.quoprimime import body_check
from nturl2path import url2pathname
from urllib import request, response

# 请求过程：
# 客户端，指web浏览器向服务器发送请求
#
# 请求-分为四部分：
# 1.请求网址 --request url
# 2.请求方法 --request methods
# 3.请求头 --request header
# 4.请求体 --request body
#
# F12查看请求响应
#
# 2.爬虫概念
# 模拟浏览器，发送请求，获取响应
# 只能获取客户端所展示出来的数据
#
# 特点：知识碎片化
# 在写爬虫的时候会面对各种各样的网站，每个网站都是有区别的
#
# 模拟客户端，操作者是正常的用户
# 作为一个爬虫身份，服务器不欢迎我们的，尽可能的去模拟正常的用户发送请求
#
# 爬虫 -- 模拟客户端访问，抓取数据
# 反爬 -- 保护重要数据，防止恶意网络攻击
# 反反爬 -- 针对反爬做的措施
#
# 3.爬虫分类
# 根据爬取网站的数量：通过爬虫、聚焦爬虫（主要学习）
# 根据获取数据的目的：功能性爬虫，数据增量爬虫

# 4.爬虫的基本流程
# 1.确认目标：目标url：https://www.baidu.com
# 2.发送请求：发送网络请求，获取到特定的服务端给你的响应
# 3.提取数据：从响应中提取特定的数据 jsonpath/xpath/re
# 4.保存数据：本地（html、json、txt）、数据库
#
# 获取到的响应中，有可能会提取到还需要继续发送请求的url，可以拿着解析到的url继续发送请求
#
# 5.robots协议
# robots协议并不是一个规范，只是约定俗成
#
# 1.网络通信步骤：
# 电脑（浏览器）： url -- https://www.baidu.com 域名
# DNS服务器：ip地址标注服务器  -- 1.1.1.1 IP地址
# DNS服务器返回ip地址给浏览器
# 浏览器拿到ip地址去访问服务器，返回响应
# 服务器返回给我们的响应数据，html/css/js/jpg...
#
# 百度首页：实际上有很多部分组成起来
# html：文本
# css：样式，控制文字大小、颜色
# js：行为，包括鼠标点击
# jpg：图片
#
# 网络通信的实际原理：
# 一个请求https://www.baidu.com只能对应一个数据包（文件）
# 之后抓包可能会有很多个数据包，共同组成了这个页面

# 2.http协议和https协议
# http协议：规定了服务器和客户端互相通信的规则
#
# 概念和区别
# http协议：超文本传输协议，默认端口号是80
# 超文本：不仅仅限于文本，还包括图片、音频、视频
# 传输协议：指使用共用约定的固定格式来传递换成字符串的超文本内容
#
# https协议：http + ssl（安全套接字层） 默认端口号是443
# 带有安全套接字层的超文本传输协议
# ssl对传输的内容进行加密
#
# https比http更安全，但是性能更低
#
# http请求/相应的步骤：
# 1.客户端连接到web服务器
# 2.发送http请求
# 3.服务器接受请求返回响应
# 4.释放连接tcp连接
# 5.客户端解析html内容

# 3.请求头
# 请求方式：get 和 post
# get向服务器要资源
# post向服务器提交资源
#
# User-Agent ： 模拟正常用户
# cookie ： 登录保持
# referer ：当前这一次请求是由哪个请求过来的
#
# 抓包得到的响应内容才是判断依据，elements中的源码是渲染之后的源码，这个不能作为判断标准

# requests的使用
# 1.安装 -- pip install requests
# 2.基本使用 --百度
import requests
from zope.interface.common.collections import IValuesView

# 找到目标url
# url = 'https://www.baidu.com/'
# 发送请求
# response = requests.get(url)
# print(response)   #<Response [200]>  200是状态码
#
# # 打印响应
# 将其编码设置为utf-8
# response.encoding = 'utf-8'
# print(response.text)   #响应内容有乱码，requests模块会自动寻求一种解码方式去解码

# print(response.content.decode())  #默认utf-8解码
# print(len(response.content.decode()))   #2349
# with open('baidu.html','w', encoding='utf-8') as f:
#     f.write(response.content.decode())

# 3.使用requests库保存图片
# # 确定url
# url = 'https://pic.nximg.cn/file/20220924/27583647_110242211103_2.jpg'
# headers = {
#     'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# # 发送请求，获取响应
# res = requests.get(url,headers=headers)
# # print(res.content)
#
# # 打印响应的url
# print(res.url)
# # 打印响应对象的请求头
# print(res.request.headers)
# # 打印响应头
# print(res.headers)
#
# print(res.apparent_encoding)   #这个网页是什么编码，用来解决中文乱码问题。
# # 保存响应
# with open('1.jpg','wb') as f:
#     f.write(res.content)

# 4.其他属性
# response.text 和response.content的区别：
# text:   str类型， requests模块自动根据http头部对响应的编码作出有根据的推测
# content: bytes类型， 可以通过decode()解码

# 5.用户代理
# 百度首页代码爬取到的比较少
# url = 'https://www.baidu.com/'
# # 构建请求头
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# # 发送请求
# # 带上user-agent发送请求
# # headers参数接收字典形式的请求头，请求头字段名为key，值为values
# response = requests.get(url,headers=headers)
# # print(response.content.decode())
# print(len(response.content.decode()))   #731271

#添加user-agent的目的是为了上服务器认为是浏览器在发送请求，而不是爬虫程序在发送请求

# user-agent池   -- 防止反爬
# 随机调用

# 第一种：构建user-agent池
# import random
# UAlist = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1'
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15'
# ]
# print(random.choice(UAlist))
#
# # 第二种：fake_useragent   可能会出现异常
# from fake_useragent import UserAgent
# print(UserAgent().random)

# 2.浏览器发送请求原理
# 1.构建请求
# 2.查找缓存
# 3.准备ip地址和端口
# 4.等待tcp队列
# 5.建立tcp连接
# 6.发送http请求

# 浏览器会向服务器发送请求行，包括了请求方法，请求url，http协议

# 3.url传参
#https://cn.bing.com/search?q=%E5%AD%A6%E4%B9%A0&qs=n&form=QBRE&sp=-1&lq=0&pq
# 字符串被当作url提交时会被自动进行url编码处理
# 输入 --- 学习          明文
# 发送请求的时候 --- %E5%AD%A6%E4%B9%A0   密文

# from urllib.parse import quote,unquote
# # quote()    # 明文转密文       传入参数类型：字符串
# # unquote()  # 密文转明文       传入参数类型：%xx%xx
#
# print(quote('参数'))        # %E5%8F%82%E6%95%B0
# print(unquote('%E5%8F%82%E6%95%B0'))  # 参数

# wd=参数
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8F%82%E6%95%B0

# 4.发送带参数的请求
# import requests
# name = input('请输入关键字：')
# url = f'https://www.baidu.com/s?wd={name}'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
#
# res = requests.get(url,headers=headers)
# print(res.content.decode())

# 通过params携带参数字典
# 1.构建请求参数字典
# 2.发送请求的时候带上请求参数字典

# url = 'https://www.baidu.com/s?'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
#
# # 构建请求参数字典
# name = input('请输入关键字：')
# kw = {'wd':name}
# requests.get(url,headers=headers,params=kw)