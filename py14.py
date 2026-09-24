def test(fn):  #fn是普通形参
    print("登录")
    print("注册")
    fn()  #test2()
def test2():
    print("发消息")
test(test2)

# 1.装饰器
# 含义：装饰器本质上就是一个闭包函数，它的好处就是在不修改原有代码的基础上，增加额外的功能
# 1.2标准版装饰器
def send():
    print("发消息")
send()
def send2():
    print("转账1314")
send2()

# 闭包的三个条件
# 1.函数嵌套
# 2.内函数要使用外函数的局部变量
# 3.外函数的返回值是内函数的函数名
def outer(fn):       #外层函数，fn是形参，但是往里面传入的是被装饰的函数名：send
    #即包含原有功能，又包含新功能
    def inner():     #内函数
        print("登录")
        #执行被装饰的函数
        fn()         #send()
    return inner
print(outer(send))
ot = outer(send2)     #调用外函数
ot()      #调用内函数

# 装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包

# 1.3语法糖
# 格式：@装饰器名称
def outer(fn):
    def inner():
        print("登录")
        #执行被装饰的函数
        fn()
    return inner
# 注意：装饰器名称后面不要加()，前者是引用，后者是调用函数，返回该函数要返回的值
@outer
def send():
    print("发消息:笑死我了")
send()
@outer
def send2():
    print("发消息:呵呵呵")
send2()

# 1.4被装饰的函数有参数
def outer(fn):
    def inner(name):
        print(f"{name}是inner函数中的参数")
        fn(name)
    return inner
@outer
def func(name):
    print("这是被装饰的函数")
func("shutong")
# ot = outer(func)
# ot("shutong")

# 1.5被装饰的函数有可变参数*args,**kwargs
# 被装饰的函数
def func(*args,**kwargs):
    print(args)    #不要加*
    print(kwargs)
# func(name = 'shutong')
# 装饰器函数
def outer(fn):
    def inner():
        print("登录...")
        fn()
    return inner
# 函数必须要被调用才会执行
# print(outer('test'))
# outer(func)()
# outer('test')  -->inner
# print(outer(func))
# ot = outer(func)
# ot('susu','haha',name = 'shutong',age = 18)   #susu以元组的形式传递给args，name = 'shutong'以键等于值的形式传递给kwargs

# 1.6多个装饰器
# 第一个装饰器
def decol1(fn):
    def inner():
        return "哈哈哈"+fn()+"呵呵呵"
    return inner
# 第二个装饰器
def decol2(fn):
    def inner():
        return "奈斯"+fn()+"你真棒"
    return inner
# 第三个装饰器
def decol3(fn):
    def inner():
        return "你好"+fn()+"嘻嘻"
    return inner
#被装饰的函数
@decol3
@decol2
@decol1
def test1():
    return "晚上在学习python基础"
print(test1())

# 多个装饰器的装饰过程，离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程

# "哈哈哈"+"晚上在学习python基础"+"呵呵呵"
# "奈斯"+"哈哈哈"+"晚上在学习python基础"+"呵呵呵"+"你真棒"
# "你好"+"奈斯"+"哈哈哈"+"晚上在学习python基础"+"呵呵呵"+"你真棒"+"嘻嘻"