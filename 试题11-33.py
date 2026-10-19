# 11、编写一个程序，接收一系列以逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除，可被5整除的数字将以逗号分隔的顺序打印。
#
# value = []
# print('以逗号分隔的4位二进制数')
# items = [i for i in input().split(',')]
# for x in items:
#     intp = int(x,2)   #把二进制转十进制
#     if intp%5 == 0:
#         value.append(x)
#     list = [str(num) for num in value ]
# print(','.join(list))

# 12、编写一个程序，找到1000到3000并且所有位数均为偶数的所有数字；获得的数字都以逗号分隔的顺序，打印在一行上。
#
# values = []
# for i in range(1000,3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)   #利用下标
# print(','.join(values))

# 13、编写一个接受句子并计算字母和数字的程序。
#
# print("请输入")
# s = input()
# d = {'字母':0,'数字':0}
# for i in s:
#     if i.isdigit():  #判断是否为数字
#         d['数字']+=1
#     if i.isalpha():  #判断是否为字母
#         d['字母']+=1
# print('数字',d['数字'])
# print('字母',d['字母'])

# 14、编写一个接收句子的程序，并计算大写字母和小写字母的数量。
#
# print("请输入")
# s = input()
# d = {'大写字母':0,'小写字母':0}
# for i in s:
#     if i.isupper():  #判断是否为大写字母
#         d['大写字母']+=1
#     if i.islower():  #判断是否为小写字母
#         d['小写字母']+=1
# print('大写字母',d['大写字母'])
# print('小写字母',d['小写字母'])

# 15、编写一个程序，计算 a+aa+aaa+aaaa 的值，给定的数字作为a的值。
#
# print("请输入一个数字:")
# a = input()
# n1 = int(a)
# n2 = int(a*2)
# n3 = int(a*3)
# n4 = int(a*4)
# print(n1 + n2 + n3 + n4)
#  * 用法总结
# 两边都是数字：乘
# 一边是字符串 / 列表，一边数字：重复复制
# 变量前面加*：拆包或者收集多个值
# 函数参数里*args：接收不定数量参数。

# 16、使用列表推导输出列表中的每个奇数，该列表由一系列逗号分隔的数字输入。
#
# print("请输入数字：")
# s = input()
# if ',' in s:
#     lst = s.split(',')   # 有逗号，split返回本身就是列表
# else:
#     lst = s
# result = [x for x in lst if int(x) % 2 != 0]
# print(",".join(result))

# 17、您需要编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中 name 是字符串，age 和 height 是数字，元组由控制台输入。
# 排序标准是：
# 1：根据名称排序；
# 2：然后根据年龄排序；
# 3：然后按分数排序。
# 优先级是 name > age > 得分。
#
# from operator import itemgetter
#
# print("请输入：")
# s = input()
# groups = [g for g in s.split(';')]
# lst = []
# for g in groups:
#     name, age, height = g.split(',')
#     # 把年龄、高度转为int，存成元组 (name, age, height)
#     person = (name, int(age), int(height))
#     lst.append(person)
# # 排序：优先级0(name) >1(age) >2(height)
# res = sorted(lst, key=itemgetter(0, 1, 2))  #取元组第 0 项、第 1 项、第 2 项作为排序 key
# print(res)

# 如果给出以下元组作为程序的输入：
# Tom,19,80; John,20,90; Jony,17,91; Jony,17,93; Json,21,85
# 运行结果
# [(' John', 20, 90), (' Jony', 17, 91), (' Jony', 17, 93), (' Json', 21, 85), ('Tom', 19, 80)]

# 18、使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
# 编程题里「在 0 和 n 之间」默认是：[0，n)
#定义函数版：
# def putNumbers(n):
#     i = 0
#     while i < n:
#         if i%7 == 0:
#             yield i
#         i += 1
# for num in putNumbers(100):
#     print(num)
# # 定义类版：
# class PutNumbers:
#     def __init__(self, n):
#         self.n = n
#     # 把外面传进来的值，保存下来，给类里其他方法（比如__iter__）使用
#     def __iter__(self):
#         i = 0
#         while i < self.n:
#             if i % 7 == 0:
#                 yield i
#             i += 1
# for num in PutNumbers(100):
#     print(num)

# 19、编写一个程序，来计算每个单词出现的频率，按字母顺序对键进行排序后输出。
#
# freq = {}
# print("请输入")
# line = input()
# # split() 默认按空白分割，切成一个个单词
# for word in line.split():
#     # get(word,0): 如果字典没有word，默认取0，然后+1计数
#     freq[word] = freq.get(word, 0) + 1
# # sorted() 对字典的所有key按字母升序排序，返回排序后的单词列表
# words = sorted(freq.keys())  #freq.keys()：所有键
# for w in words:
#     print(f"{w}:{freq[w]}")

# 输入
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 运行结果
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# 20、写一个可以计算数字平方值的方法，提示用 ** 运算符。
#
# def square(num):
#     return num ** 2
# print(square(3))
# print(square(4))

# 21、请编写一个程序来打印一些Python内置函数文档，例如abs()，int()，input()，并为你自己的功能添加文档。
#
# def add(a,b):
#     """计算两个数字相加
#     参数a：第一个数
#     参数b：第二个数
#     返回：a+b"""
#     return a+b
# print(add.__doc__)
# # print(int.__doc__)
# # print(abs.__doc__)
# # print(input.__doc__)

# 22、定义一个类，它具有类参数并具有相同的实例参数。
#
# class Person:
#     name = "Person"   # 类属性（类参数）
#     def __init__(self, name =None):   #name=None：给参数 name 设置默认值
#         self.name = name  # 实例属性（实例参数，和类属性同名name）
# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))
# nico = Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))

# 23、定义一个可以计算两个数之和的函数。
#
# def func(num1, num2):
#     return num1 + num2
# print(func(1,2))

# 24、定义一个可以将整数转换为字符串并在控制台中打印的函数。
#
# def funa(n):
#     print(str(n))
# funa(10)

# 25、定义一个函数，它可以接收两个字符串形式的整数并计算它们的和，然后在控制台中输出。
#
# def funb(num1, num2):
#     print(int(num1) + int(num2))
# funb('1','2')

# 26、定义一个函数，它可以接受两个字符串作为输入，并将它们连接起来，然后在控制台中输出。
#
# def funb(num1, num2):
#     print(num1 + num2)
# funb('1','2')

# 27、定义一个函数，它可以接受两个字符串作为输入，并在控制台中以最大长度打印字符串。如果两个字符串长度相同，则函数应逐行打印所有字符串。
#
# def prictvale(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1 > len2:
#         print(s1)
#     elif len2 > len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# prictvale("one", "two")

# 28、定义一个函数，它可以接受一个整数作为输入，如果这个数字是偶数，则输出“它是偶数”，否则输出“它是奇数”。
#
# def func(n):
#     if n%2==0:
#         print('它是偶数')
#     else:
#         print('它是奇数')
# func(7)

# 29、定义一个函数，它可以打印一个字典，其中键是1到3之间的数字(包括在内)，值是键的平方。
# #
# def func():
#     d = {}
#     for i in range(1,4):
#         d[i] = i ** 2
#     print(d)
# func()

# 30、定义一个函数，它可以打印一个字典，其中键是1到20之间的数字(包括在内)，值是键的平方。
#
# def func():
#     d = {}
#     for i in range(1,21):
#         d[i] = i ** 2
#     print(d)
# func()

# 31、定义一个函数，它可以生成一个字典，其中键是1到20之间的数字(包括在内)，值是键的平方。函数只输出值即可。
#
# def func():
#     d = {}
#     for i in range(1,21):
#         d[i] = i ** 2
#     for k, v in d.items():   #这边有题目要求
#         print(v)
# func()

# 32、定义一个函数，它可以生成一个字典，其中键是1到20之间的数字(包括在内)，值是键的平方。函数只打印键即可。
#
# def func():
#     d = {}
#     for i in range(1,21):
#         d[i] = i ** 2
#     for k, v in d.items():   #这边有题目要求
#         print(k)
# func()

# 33、定义一个函数，它可以生成和打印一个列表，其中的值是1到20之间的数的平方（包括这两个数）。
#
# def func():
#     li = []
#     for i in range(1,21):
#         s= i**2
#         li.append(s)
#     print(li)
# func()