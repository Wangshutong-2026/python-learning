import requests
# 图片
# url = 'https://p1.music.126.net/37xBve-YgvZwt9cSZQ932Q==/109951174145226492.jpg?imageView&quality=89'
# 构建请求头
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# 发送请求，获取响应
# res = requests.get(url, headers=headers)
# 保存图片
# with open("music.jpg", "wb") as f:
#     f.write(res.content)  #二进制数

# 音频
# url = 'https://m804.music.126.net/20261022144558/2d01376a07c0ad12523ceae3038de44e/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/83755358668/2f8e/fa5f/f607/66fd10ac8947a25e7cf7824f28c34d74.m4a?vuutv=g9e3M/LCxKmwGbVkb72Ma72IjkZZhCf0pjKHKqFTOZXvNTQxfEsRRRU7pQRC312gzgxtgkqaLOagg88rHLCQxbXiTJCApB2kKxRzs1lH3wY=&authSecret=000001a16245197a17a40ab0c3fe0007&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# res = requests.get(url, headers=headers)
# with open('music.mp3', 'wb') as f:
#     f.write(res.content)

# 视频
# url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/ebf7/core/9e52/09fa2c1c826b9b0fcfc344744ffa7b9b.mp4?wsSecret=39db5375a143619f91985aefdd2ba5b1&wsTime=1792652004'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# res = requests.get(url, headers=headers)
# with open('music.mp4', 'wb') as f:
#     f.write(res.content)

# 贴吧单页
# url = 'https://tieba.baidu.com/f?kw=bilibili&fr=personalize_page'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# res = requests.get(url, headers=headers)
# with open('bilibili.html', 'w',encoding='utf-8') as f:
#     f.write(res.text)

# 贴吧翻页(示例，贴吧如今不再翻页)
# url = 'https://tieba.baidu.com/f?kw=bilibili&fr=personalize_page'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
# }
# word = input('请输入网站：')
# page = int(input('请输入页数：'))
# for i in range(page):
#     params = {
#         'kw':word,
#         'pn':i*50
#     }
# res = requests.get(url, headers=headers, params=params)
# with open(f'{word}{i+1}.html', 'wb') as f:
#     f.write(res.content)

# 6.改写为面向对象

# class Tieba:
#     def __init__(self):
#         self.url = 'https://tieba.baidu.com/f?'
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
#         }
#     #发送请求
#     def send(self,params):
#         res = requests.get(self.url,params = params,headers = self.headers)
#         return res.text
#     #存文件（wb下载资源）--> .content
#     #拿源码解析、交给bs  --> .text
#
#     #保存文件
#     def save(self,page,con):
#         with open(f'{page}.html','w',encoding='utf-8') as f:
#             f.write(con)
#     def run(self):
#         word = input('请输入网站：')
#         pages = int(input('请输入页数：'))
#
#         for page in range(pages)
#             params = {
#                 'kw':word,
#                 'pn':page * 50
#             }
#
#             #循环执行
#             data = self.send(params)
#             self.save(page,data)
# te = Tieba()
# te.run()

# 1.post请求

# post请求：登录注册，传输大文本内容
# requests.post(url, data)
# data参数接收一个字典

# get跟post区别
# get请求---比较多
# post请求 -- 比较少

# get请求直接向服务器发送请求，获取响应内容
# post请求是先给服务器一些数据，然后再获取响应

# get请求携带参数 -- params
# post请求携带参数 -- data

# 2.cookie 模拟登录
# 找到登录后的url

# url='https://www.iciba.com/'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
#     'Cookie':'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoie1widG9rZW5DcmVhdGVUaW1lXCI6XCIyMDI2LTEwLTIyVDE4OjU3OjMxLjg4NlwiLFwidWlkXCI6MzkwNzIxNzd9In0.RGl53XXFqCInIZRADJ4TSetolRaKy0kNKFS--ThiXW4; _ustat=%7B%22s%22%3A%7B%22u%22%3Afalse%2C%22m%22%3Afalse%2C%22e%22%3Afalse%7D%2C%22t%22%3A1792666651%2C%22e%22%3A%22%22%2C%22i%22%3A39072177%2C%22n%22%3A%22139****5193%22%2C%22sid%22%3A%220cd05cb95d699b8272ac3df558c25ac5%22%7D'
# }
# res = requests.get(url,headers=headers)
# print(res.text)



# 好吧，金山词霸更新了，无法爬取
import json
# url='https://dictionary.iciba.com/dictionary/fy/batch?client=6&key=1000006&timestamp=1792666999974&signature=75d461227092061d8b7791cf39b0421b'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
# }
# word = input('请输入你要翻译的内容')
# # 构建data参数字典
# post_data = {
#     'from':'zh',
#     'to':'en',
#     'ciyv':word
# }
# res = requests.get(url,headers=headers,params=post_data)
# print(res.text)
# # 解析数据
# # 将json数据转换为python字典
# dic = json.loads(res.text)
# # print(type(dic))
# print(dic['out'])

# 4.session  -- 自动处理cookie
# session = requests.session()  # 实例化session对象
# response = session.post(url, data=data)
# 使用session访问登录以后的页面
# session.get(url.text)

# 1.对访问登录后才能访问的页面去进行抓包
# 2.确定登录请求的url地址，请求方法和所需的参数
# 3.确定登录才能访问的页面url和请求方法
# 4.利用requests.session完成代码

# 5.cookie池
# user-agent池：短时间内多次发出请求，尽量每一次的请求都用不同的用户代理
# cookie池：每一个cookie就代表一个账号
# cookie有有效期
# session不用担心有效期的问题

# cookie跟session区别：
# 1.cookie数据放在客户的浏览器上，session数据放在服务器上
# 2.cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑到安全应当使用session
# 3.session会在一定时间内保存在服务器上，考虑到减轻服务器性能方面，应当使用cookie
# 4.可以考虑将登录信息等重要信息存放在session，其他信息如果需保留，可以放在cookie中

# 2.代理
# 2.1 正向代理和反向代理
# 正向代理：给客户端做代理，让服务器不知道客户端的真实身份
# 保护自己的ip地址不会被封，要封也是封代理ip
# 反向代理：给服务器做代理，让浏览器不知道服务器的真实地址
# 正向代理保护客户端，反向代理保护服务端

# 2.2实际上理论来说分为三类：
# 1.透明代理：服务器知道我们使用了代理ip，也知道真实ip
# 2.匿名代理：服务器能够检测到使用了代理ip，但是不知道真实ip
# 3.高匿代理：服务器既不能检测到使用代理ip，也不知道真实ip

# 3.代理ip的使用
# proxies的形式：字典
# proxies = {
#     # 以键值对的的形式，固定的语法，IP地址：端口号
#     'http':'http://12.34.56.79:9527',
#     'https':'http://12.34.56.79:9527'
# }
#
# response = requests.get(url,proxies=proxies)

url = 'https://www.baidu.com/'
# 构建请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}
# 构建代理字典
proxies = {
    # 第一种写法：
    'http://12.34.56.79:9527'
    # 第二种写法：
    # 'http':'http://12.34.56.79:9527'
}
res = requests.get(url, headers=headers, proxies=proxies)
print(res.content.decode())

# 代理IP无效，会自动使用本机的真实ip，所以才会访问成功
