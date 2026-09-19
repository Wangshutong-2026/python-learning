# 1.函数
# 1.1含义：将独立的代码块组织成一个整体，使其具有特殊功能的代码集，在需要的时候再去调用即可
# 1.2作用：提高代码的重用性，使整体代码看上去更加简练
# 1.3基本格式
# 1.定义函数
# def 函数名 ():
#     函数体
# 2.调用函数
# 函数名()
from py02 import age


def login():
    print("这是登录函数")
    print('___')
login()
login()
# 调用几次，函数里面的代码就会运行几次，每次调用的时候，函数都会从头开始

# 编写一个打招呼的函数并调用它
def say_hello():
    print("hello")
    print("shutong")
# 调用函数前，必须保证函数已经存在
say_hello()

# 2.返回值 return
# 函数执行结束后，最后给调用者的一个结果
# 作用：
#   1.return会给函数的执行者返回值
def buy():
    return "一桶水果茶"
buy()
print(buy())
#   2.函数中遇到return，表示此函数结束，不继续执行
def buy():
    return "一桶水果茶",20  #return返回多个值，以元组的形式返回给调用者
    return 20   #函数中遇到return，return下面的代码不会被执行
print(buy())
# 返回值的三种情况总结
#     1.一个返回值也没有，返回结果为None
#     2.一个返回值，就把值返回给调用者
#     3.多个返回值，以元组的形式返回调用者
# return 和 print 区别
#     1.return表示次函数结束，print会一直执行
def funa():
    # return 123
    print(456)
    print(123)
funa()
# print(funa())
#     2.return是返回计算值，print是打印结果
def add():
    a = 1
    b = 2
    return a + b
    # print(a+b)
print(add())
# add()

# 3.参数
# 定义格式：
# def 函数名(形参a,形参b):   #形参：定义函数时，小括号里面的变量
#     函数体
#     ...(如a =1，b = 2)
# 调用格式：
# 函数名(实参1,实参2)   #实参：调用函数时，小括号里面的具体的值
def add(a,b):  #a,b就是形参
    return a+b
print(add(2,5))  #2,5就是实参
# 传参 a = 2，b = 5

# 3.2函数参数
# 3.2.1必备参数（位置参数）
# 含义：传递和定义参数的顺序及个数必须一致
# 格式：def func(a,b):
def funa(name1,age,sex):
    print(name1)
    print(age)
    print(sex)
funa('shutong',18,'女')  #写了几个就必须要传几个，不可以多传，也不可以少传

# 3.2.2默认参数
# 含义：为参数提供默认值，调用函数时可不传该默认参数的值
# 注意：所有的位置参数必须出现在默认参数前，包括函数定义和调用
# 格式：def func(a=12):
def funb(b=8,a=8):
    print(b)
funb()
funb(200)
# 设置默认值，没有传值会根据默认值来执行代码，传了值会根据传入的值来执行代码

# 3.2.3可变参数
# 含义：传入的值的数量是可以改变的，可以传入多个，也可以不传
# 格式：def func(*args):
def func(*args):   #可以把args改成其他参数名，但是args符合代码的规范性
    print(args)
    print(type(args))   #以元组形式接收
func('海绵宝宝','派大星','章鱼哥')

# 3.2.4关键字参数
# 格式：def func(**kwargs):
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))   #以字典形式接收
func()  #空字典
func(name = 'shutong',age ='20')   #传值的时候，需要采用 键=值 的形式
# 作用：可以扩展函数的功能

# 4.函数嵌套
# 4.1嵌套调用
# 含义：在一个函数里面调用另一个函数
def study():
    print("晚上在学习")
def course():
    study()   #在course()函数内调用study()
    print("Python基础")
# 调用
# study()
course()

# 4.2嵌套定义
# 含义：在一个函数中定义另外一个函数
def study():   #外函数
    print("晚上在学习")
    def course():   #内函数
        print("python基础")   #不要在内层函数中调用外层函数，会陷入循环，直到超过递归的最大深度
    course()   #注意：注意缩进，定义和调用是同级的，调用如果在定义里面则永远调用不到
study()