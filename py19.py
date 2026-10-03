# 2.单例模式
# 可以理解成一个特殊的类，这个类只存在一个对象
# 优点：可以节省内存空间，减少了不必要的资源浪费
# 弊端：多线程访问的时候容易引发线程安全问题
# 2.2方式
# 1.通过@classmethod
# 2.通过装饰器实现
# 3.通过重写__new__()实现（重点）
# 4.通过导入模块实现
from typing import Self


class A(object):
    pass
a1 = A()
print(a1)
a2 = A()
print(a2)
# 内存地址发生变化说明是不同对象
# 实现单例模式，对象的内存地址都是一样的，只有一个对象

# 2.3通过重写__new__()实现单例模式
# 设计流程
# 1.定义一个类属性，初始值为None，来记录单例对象的引用
# 2.重写__new__()方法
# 3.进行判断，如果类属性是None，把__new__()返回的对象引用保存进去
# 4.返回类属性中记录的对象引用
class Singleton(object):
    # 记录第一个被创建的对象的引用
    obj = None   #类属性
    def __new__(cls, *args, **kwargs):
        print("这是__new__()方法")
        #判断类属性是否为空
        if cls.obj == None:
            cls.obj= super().__new__(cls)
        return cls.obj
    def __init__(self):
        print("我是__init__()")
s = Singleton()
print("s:",s)
s2 = Singleton()
print("s2:",s2)
# 单例模式：每一次实例化所创建的对象都是同一个，内存地址都一样

# 2.4通过导入模块实现单例模式
# 模块就是天然的单例模式
from pytest02 import te as te01
from pytest02 import te as te02
print(te02,id(te02))
print(te01,id(te01))

# 2.5应用场景
# 1.回收站对象
# 2.音乐播放器，一个音乐播放软件负责音乐播放的对象只有一个
# 3.开发游戏软件  场景管理器
# 4.数据库配置，数据库连接池的设计

# 3.魔术方法&魔法属性
# 3.1__doc__:类、函数的描述信息
class Person(object):
    """人类---类的描述信息"""   #只能使用多行注释，单行注释无效
    pass
print(Person.__doc__)
def sing():
    """唱歌"""
    pass
print(sing.__doc__)
# 3.2__module__:表示当前操作对象的所在模块
# 3.3__class__:表示当前操作对象所在的类
import pytest01
b = pytest01.B()
print(b)
b.funa()
print(b.__module__)   #输出模块
print(b.__class__)    #输出类
# 3.4__str__():对象的描述信息
# 如果过类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中return的数据
# 注意：__str__()必须返回一个字符串
class C:
    def __str__(self):
        return "这里是返回值"    #必须要有返回值，并且一定是字符串类型
        # return123
    # pass
c = C()
print(c)
# 3.5__del__():析构函数，在程序结束时会调用，或者在删除某个对象的时候也会被调用
# 3.6__call__():使一个实例对象成为一个可调用对象，就像函数那样可以调用
# 可调用对象：函数\内置函数和类都是可调用对象，凡是可以把一对()应用到某个对象身上都可以称之为可调用对象
# callable()：判断一个对象是否是可调用对象
def func():
    print("哈哈哈哈")
func()
print(callable(func))   #True
name = 'shutong'
# name()   #报错
print(callable(name))    #False

class A:
    def __call__(self, *args, **kwargs):
        print("这是__call__()")
a = A()
a()    #调用一个调用的实例对象，其实就是在调用它的__call__()方法
a2 = A()
a2()
print(callable(a))