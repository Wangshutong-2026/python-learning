# 导入re模块
import re
from dataclasses import replace
from re import search

# 一、匹配分组
# 1. | 匹配左右任意一个表达式      ---常用
res = re.match('abc|def','def')
print(res.group())
res = re.match(r'\d|\S','s234')
print(res.group())

# 2.(ab)将括号中字符作为一个分组
res = re.match(r'\w*@(163|qq|126).com','123@126.com')
print(res.group())

# 3.\num 匹配分组num匹配到的字符串   ---经常在匹配标签是被使用
# res = re.match(r'<(\w*)>\w*</\1>','<html>login</html>')
res = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><body>login</body></html>')
print(res.group())
# 注意：从外到内排序，编号从1开始

# 4.(?P<name>)   分组起别名
# 5.(?P=name)    引用别名为name分组匹配到的字符串
res = re.match(r'<(?P<L1>\w*)><(?P<L2>\w*)>.*</(?P=L2)></(?P=L1)>','<html><body>login</body></html>')
print(res.group())

# 匹配网址 前缀一般是www，后缀：.com、.cn、.org
li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cb']
# res = re.match(r'www(\.)\w*\1(com|cn|org)','www.baidu.com')
# print(res.group())   #\是转义字符，\.就是作为普通的.
for i in li:
    res = re.match(r'www(\.)\w*\1(com|cn|org)', i)
    if res != None:
        print(res.group())
    else:
        print(f"{i}这个网址有错误")

# 二、高级用法
# 1.search():扫描整个字符串并返回第一个成功匹配的对象，如果过匹配失败，就返回None
res = re.search(r'\d','py1thon1th')
print(res.group())

# 2.findall():从头到尾匹配，找到所有匹配成功的数据，返回一个列表
res = re.findall(r'\d','py123thon1th')
print(res)
print(type(res))

# 总结：
# match():从头开始匹配，匹配成功返回match对象，通过group()进行提取，匹配失败就返回None，只匹配一次
# search():从头开始匹配，匹配成功返回第一个成功匹配的对象，通过group()进行提取，匹配失败返回None，只匹配一次
# findall():从头到尾匹配，匹配成功返回一个列表，匹配所有匹配成功的数据，不需要通过group()进行提取，没有group()

# 3.sub(pattern,repl,string,count)
# pattern  正则表达式（代表需要被替换的，也就是字符串里面的旧内容）
# repl     新内容
# string   字符串
# count    指定替换的次数
res = re.sub('su','u','hello,susu')
print(res)
res = re.sub(r'\d','2','这是这个月的第30天',count=1)
print(res)

# 4.split(pattern,string,maxsplit)
# pattern  正则表达式
# string   字符串
# maxsplit 指定最大分割次数
res = re.split(',','hello,python,123,hhh',maxsplit=2)   #没有设置次数就默认全部分割
print(res)

# 三、贪婪与非贪婪
# 1.贪婪匹配（默认）：在满足匹配时，匹配尽可能长的字符串
res = re.match('em*','emmmmm...')
print(res.group())

# 2.非贪婪匹配：在满足匹配时，匹配尽可能短的字符串，使用?来表示非贪婪匹配
#大概就是取交集最小的次数
res = re.match('em+?','emmmmm...')
print(res.group())
res = re.match('m{3,5}?','mmmmmmm...')
print(res.group())

# 四、原生字符串
print(r'sixs\tar')   #r取消转义
res = re.match(r'\\\\\\',r'\\\game')
print(res.group())
res = re.match('\\\\',r'\game')
print(res.group())
# 正则表达式，匹配字符串中的字符\需要\\\\，加入原生字符串，\\代表\