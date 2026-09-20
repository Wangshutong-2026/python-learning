# 1.作用域
# 1.1含义：指的是变量生效的范围，分为两种，分别是全局变量和局部变量
# 1.2全局变量
# 函数外部定义的变量，在整个文件中都是有效的
from functools import reduce
from ipaddress import summarize_address_range
from sys import argv

a = 100   #全局变量
def test1():
    print("这是test1中a的值：",a)
def test2():
    a = 120
    print("这是test2中a的值：",a)
print("调用函数前a的值：",a)
test1()
test2()
print("调用函数后a的值：",a)
# a的值没有被覆盖是因为函数内部如果要使用变量，会先从内部找，有的话就直接使用，没有会到函数外面去找
# 1.3局部变量
# 函数内部定义的变量，从定义位置开始到函数定义结束位置有效
def funa():
    num = 10  #局部变量
    print("num:",num)
funa()
# print("num:",num)  #报错，局部变量只能在被定义的函数中使用，函数外部不能使用
# 作用：在函数体内部，临时保存数据，即当函数调用完成之后，就销毁局部变量
def funa():
    num = 10
    print("funa中的num:",num)
funa()
def funb():
    num = 18
    print("funb中的num:",num)
funb()

# 全局变量和局部变量命名相同
# 在函数内部修改全局变量的值，可以使用global关键字
# global
# 将变量声明变为全局变量
# 语法格式：global 变量名
a = 100   #全局变量
def test1():
    print("这是test1中a的值：",a)
def test2():
    global a  #声明全局变量
    a = 120
    print("这是test2中a的值：",a)
print("调用函数前a的值：",a)
test1()
test2()
print("调用函数后a的值：",a)

def study():
    global name,age   #将局部变量name，age声明为全局变量
    name = "python基础"   #局部变量
    age = 20
    print(f"{age}岁的我们在学习{name}")
study()
print(name,age)
def work():
    print(name)
work()

# 1.5nonlocal   ———了解
# 用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明
a = 10  #全局变量
def outer():  #外函数
    a = 5     #局部变量
    def inner():  #内函数
        # nonlocal a
        a = 20
        def inner2():
            nonlocal a
            a = 30
            print("inner2函数中a的值", a)
        inner2()
        print("inner函数中a的值",a)
    inner()
    print("outer函数中a的值：",a)
outer()
#总结：nonlocal只能对上一级进行修改

# 2.匿名函数
# 2.1基本语法
# 函数名 = lambda 形参 : 返回值(表达式)
# 调用：结果 = 函数名(实参)

# 普通函数
def add(a,b):
    return a+b
print(add(10,20))
# 匿名函数
add = lambda a,b: a+b   #a,b就是匿名函数的形参，a+b是返回值的表达式
# lambda不需要写return来返回值，表达式本身结果就是返回
print(add(10,20))

# 2.2 lambda的参数形式
# 函数名 = lambda 形参 : 返回值(表达式)
# 2.2.1无参数
funa = lambda : "一桶水果茶"
print(funa())
# 2.2.2一个参数
funa = lambda name : name
print(funa("shutong"))
# 2.2.3默认参数
func = lambda name,age=18:(name,age)
print(func("shutong"))
print(func("shutong","20"))
fune = lambda a,b,c=12:a+b+c
print(fune(1,2,4))
print(fune(1,2))
# 默认参数必须写在非默认参数后面
# 2.2.4关键字参数
fund = lambda **kwargs:kwargs
print(fund(name = 'shutong',age = 18))

# 2.3lambda 结合if判断
a = 8
b = 5
# 为真结果 if 条件 else 为假结果
print("a比b小") if a<b else print("a大于等于b")
comp = lambda a,b : "a比b小" if a<b else "a大于等于b"   #a/b是形参，比较大小
print(comp(8,5))
# 特点：
# lambda只能实现简单的逻辑，如果逻辑复杂且代码量较大，不建议使用lambda，降低代码的可读性，为后期代码维护增加困难

# 3.内置函数
# 3.1查看所有内置函数
import builtins
print(dir(builtins))
# 大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
# 3.2内置函数一
# 3.2.1 abs()：返回绝对值
print(abs(-10))
print(abs(10))
# 3.2.2sum()：求和
# print(sum(123))  #报错，整型不是可迭代对象，sum函数内要放可迭代对象，注意：字符串不可以进行相加，普通字典也不行
print(sum({1.5,3,4}))  #运算时，只要有一个为浮点数，那么结果必定是浮点型

# 3.3内置函数二
# 3.3.1 min()：求最小值
# 3.3.2 max()：求最大值
print(min(4,1,8))
print(max(4,1,8))
print(min(-8,5,key=abs))  #传入了求绝对值的函数（不用加括号），则参数就会先求绝对值再取较大者

# 3.3.3 zip():将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
li = [1,2,3]
li2 = ['a','b','c']
print(zip(li,li2))
# 第一种方式：通过for循环
for i in zip(li,li2):
    print(i)
    print(type(i))
# 如果元素个数不一致，就按照长度最短的返回
# 第二种方式：转换成列表打印
print(list(zip(li,li2)))  #转换成列表打印
# 注意：必须是可迭代对象
# print(list(zip(li,3)))  #报错，两个都必须是可迭代对象

# 3.3.4 map():可以对可迭代对象中的每一个元素进行映射，分别去执行
# map(func,iter1):func --自己定义的函数 iterl --要放进去的可迭代对象
# 简单来说就是对象中的每一个元素都会去执行这个函数
li = [1,2,3]
def funa(x):
    return x + 5
funa = lambda x:x+5
mp = map(funa,li)  #注意：只要写函数名，不需要加上小括号
print(mp)
# 第一种方式：for循环取出
for i in mp:
    print(i)
# 第二种：转换成列表打印
print(list(mp))

# 3.3.5 reduce(): 先把对象中的两个元素取出，计算一个值然后保存着，接下来把这个计算值跟第三个元素进行计算
# 需要先导包
from functools import reduce
# reduce(function,sequence)  #function--函数：必须是有两个参数的函数，sequence--序列：可迭代对象
li2 = [1,2,3,4]
def add(x,y):
    return x+2*y   #1+2*2=5->5+2*3=11->11+2*4=19
res = reduce(add,li2)
print(res)

# 4.拆包
# 含义：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
tua = (1,2,3,4)
print(tua)
print(tua[0])
# 方法一：
a,b,c,d = tua
print("a=",a,"b=",b,"c=",c,"d=",d)
# 要求元组内的个数与接收的变量个数相同，对象内有多少个数据就需要定义多少个变量接收
#a,b = tua  #报错，值错误，要拆包的值过多
# print(a,b)
# 方法二：
a,*b = tua
print(a,b)
c,*d = b
print(c,d)
#要先把单独的给它取完，其他剩下的全部都交给带*的变量
# 一般在函数调用时使用
def funa (a,b,*args):
    print(a,b)
    print(args,type(args))
funa(1,2,3,4,5,6,7)
arg = (1,2,3,4,5,6,7)
print(*arg)