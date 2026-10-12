import re
# 1.正则表达式
# 字符串处理工具
# 注意：需要导入re模块
# 1.2特点：
# 语法比较复杂，可读性较差
# 通用性很强，适用于多种编程语言
# 1.3步骤：
# 1.导入re模块
# 2.使用match方法进行匹配操作
#   re.match()能匹配出以xxx开头的字符串
#   如果起始位置没有匹配成功，返回None
# re.match(pattern,string)
# pattern 匹配的正则表达式
# string 要匹配的字符串
res = re.match('姝彤','姝彤是最棒的')
# print(res)
  # 3.如果上一步数据匹配成功，使用group()提取数据
print(res.group())
# 注意：match是从开始位置匹配的，匹配不到就没有，且匹配的是表达式整理

# 二、匹配单个字符
# 1. . 匹配任意一个字符，除\n以外  --常用
res = re.match('.e','\\ello')
print(res.group())
# 2. [] 匹配[]中列举的字符        --常用
res = re.match('[he]','hello')   #一个[]对应一个字符
print(res.group())
# 匹配0-9第一种方式
# res = re.match('[0123456789]','97362')
# 匹配0-9第er种方式
res = re.match('[0-9]','5379')
# res = re.match('[0-46-9]','5379')  #报错
res = re.match('[a-zA-Z][a-zA-Z]','Hello')  #[a-zA-Z]代表列举出所有大小写字母
print(res.group())
# 3. \d 匹配数字0-9              --常用
res = re.match(r'.\d\d\d.','s321s')
print(res.group())
# 4. \D 匹配非数字               --常用
res = re.match(r'\D','<321s')
print(res.group())
# 5. \s 匹配空白，即空格和tab键    --常用
res = re.match(r'\s\s\s\sh','    hello')
print(res.group())
# 6. \S 匹配非空白
res = re.match(r'\S','！hello')
print(res.group())
# 7. \w 匹配单词字符，即a-z，A-Z，0-9，_，汉字      --常用
res = re.match(r'\w','A_我shutong')
print(res.group())
# 8. \W 匹配非单词字符
res = re.match(r'\W','|tong')
print(res.group())

# 三、匹配多个字符
# 1. * 匹配前一个字符出现0次或者无数次，即可有可无  ---常用
res = re.match(r'\d*','shu。')
print(res.group())
# 2. + 匹配前一个字符出现1次或者无数次，即至少一次  ---常用
res = re.match(r'\d+','1我身高188')
print(res.group())
# 3. ？ 匹配前一个字符出现1次或者0次              ---常用
res = re.match(r'\s?\d',' 12hello')
print(res.group())
# 4. {m} 匹配前一个字符出现m次
res = re.match(r'\d{3}','112py')
print(res.group())
# 5. {m,n} 匹配前一个字符出现从m次到n次
# 注意：必须符合m<n的条件
res = re.match(r'\w{3,9}','python')
# res = re.match(r'\w{9,3}','python')   #报错
print(res.group())

# 四、匹配开头和结尾
# 1. ^ ：表示以...开头；表示对...取反
res = re.match('^py','python')
print(res.group())
# 注意：^在[]中表示不匹配
res = re.match('[^py]','1234python')   #[^py]表示匹配除了p、y以外的字符
print(res.group())
# 2. $ ：匹配以...结尾
res = re.match('.{7}g$',"bingbing")
print(res.group())
