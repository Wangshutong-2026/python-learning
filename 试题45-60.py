# ### 第45题
# 问题：定义一个名为American的类，它有一个名为printNationality的静态方法。提示：使用@staticmethod装饰器来定义类的静态方法。
#
import email


class American(object):
    @staticmethod
    def printNationality():
        print('American')
anAmerican = American()
anAmerican.printNationality()
American.printNationality()

# ### 第46题
# 问题：定义一个名为American的类及其子类NewYorker。提示：使用类子类(ParentClass)来定义子类。
#
class American(object):
    pass
class NewYorker(American):
    pass
anAmerican = American()
aNewYorker = NewYorker()
print(aNewYorker)
print(anAmerican)

# ### 第47题
# 问题：定义一个名为Circle的类，可以用半径来构造。Circle类有一个可以计算面积的方法。
#
class Circle(object):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r * self.r
c = Circle(5)
print(c.area())

# ### 第48题
# 问题：定义一个名为Rectangle的类，它可以由长度和宽度构造。矩形类有一个方法可以计算面积。
#
class Rectangle(object):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
r = Rectangle(5,6)
print(r.area())
# ### 第49题
# 问题：定义一个名为Shape的类及其子类Square。Square类有一个init函数，它以长度作为参数。这两个类都有一个area函数，可以打印形状的区域，形状的区域默认为0。
#
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.l = l
    def area(self):
        return self.l * self.l
sq = Square(5)
print(sq.area())

# ### 第50题
# 问题：请引发RuntimeError异常。
#
# raise RuntimeError('something wrong')

# ### 第51题
# 问题：编写一个函数来计算5/0，并使用try/except来捕获异常。
#
def func():
    try:
        return 5/0
    except ZeroDivisionError:  #子类异常要写在父类 Exception 的前面。
        print('division by zero')
    except Exception:
        print('Caught an exception')
    finally:
        print('In finally block for cleanup')
func()
# ### 第52题
# 问题：定义一个自定义异常类，它将字符串消息作为属性。
#
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
try:
    raise MyError("something wrong")  # raise 抛出我们自己定义的异常
except MyError as e:   #e不是MyError，它是"something wrong"？
    print("捕获到自定义异常：", e.msg)

# ### 第53题
# 问题：假设我们有一些'username@companyname.com'格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名，用户名和公司名都只由字母组成。
# 示例：如果下面的电子邮件地址作为程序的输入：john@google.com，那么，程序的输出应该是：john。在向问题提供输入数据的情况下，应该假定它是控制台输入。
#
# import re
#
# emailaddress = input("请输入：")
# pat = r'(\w+)@(\w+)(\.com)'
# res = re.match(pat,emailaddress)
# print(res.group(1))

# ### 第54题
# 问题：假设我们有一些“username@companyname.com”格式的电子邮件地址，请编写程序打印给定的电子邮件地址的公司名称；用户名和公司名都只由字母组成。
# 示例：如果下面的电子邮件地址作为程序的输入：john@google.com，那么，程序的输出应该是：google。在向问题提供输入数据的情况下，应该假定它是控制台输入。
#
# import re
#
# emailaddress = input("请输入：")
# pat = r'(\w+)@(\w+)(\.com)'
# res = re.match(pat,emailaddress)
# print(res.group(2))
# ### 第55题
# 问题：编写一个程序，接收一个由空格分隔的单词序列作为输入，打印只由数字组成的单词。
# 示例：如果下面的单词作为程序的输入：2 cats and 3 dogs；那么，程序的输出应该是：['2', '3']。在向问题提供输入数据的情况下，应该假定它是控制台输入。
#
# import re
# s = input('请输入：')
# res = re.findall(r'\d+',s)
# print(res)

# ### 第56题
# 问题：打印unicode字符串 “hello world”。
#
s = u"hello world"
print(s)

# ### 第57题
# 问题：python中的解码与编码。
#
s = '我python老牛了'
a = s.encode('utf-8')
b = a.decode('utf-8')
print(a)
print(b)

# ### 第58题
# 问题：编写一个特殊注释来表明Python源代码文件是unicode格式的。
#
# -*- coding: utf-8 -*-

# ### 第59题
# 问题：写一个程序来计算1/2+2/3+3/4+……+n/(n+1)。
# 示例：如果下面的n作为程序的输入：5；那么，程序的输出应该是：3.55；
#
n = int(input("请输入："))
s = 0.0
for i in range(1,n+1):
    s += i/(i+1)
print(s)
# ### 第60题
# 问题：编写程序计算：当n>0和F(0)=1时，F(n)=F(n-1)+100，通过控制台输入一个给定的n（n>0）。
# 示例：如果下面的n作为程序的输入：5，那么，程序的输出应该是：500；
#
def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100
n = int(input())
print(f(n))