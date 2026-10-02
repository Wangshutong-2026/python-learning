# 上节总结
# 1.实例方法：方法内部访问实例属性，方法内部可以通过类名.类属性名来访问类属性
# 2.静态方法@staticmethod：方法内部，不需要访问实例属性和类属性
# 如果要访问类属性，通过类名.属性名访问，不能访问实例属性
# 3.类方法@classmethod：方法内部只需要访问类属性，可以通过cls.类属性名访问类属性，不能访问实例属性
from traceback import print_tb


class Person(object):
    name = 'shutong'   #类属性：类所拥有的属性
    def __init__(self):
        self.age = 18   #实例属性：对象私有的
    def play(self):     #实例方法
        #在实例方法中访问类属性
        print(f"{Person.name}在玩游戏")
        print(self.age)
    # @staticmethod   #静态方法：类中的函数，形参没有限制
    # def introduction():
    #     # print(f"我是{Person.name}")   #静态方法能够访问到类属性，但是无意义
    #     pass
    @classmethod     #类方法：针对类存在的方法
    def introduction(cls):   #cls代表类对象本身
        print(cls.name)
        # print(self.age)    #报错

pe = Person()
pe.play()
pe.introduction()

# 类属性是公共的，所有方法内部都能够访问到，静态方法不需要访问类属性，因为静态方法和类、对象没有关系
# 实例属性是私有的，只有实例方法内部能够访问到

# 新知识
# 1.__init__()和__new__()
# 1.1__init__():初始化对象
class Test(object):
    def __init__(self):
        print('这是__init__()')
    def __new__(cls, *args, **kwargs):    #cls代表类本身
        print('这是__new__()')
te = Test()
# 1.2__new__()：object基类提供的内置的静态方法
# 作用：1.在内存中为对象分配空间  2.返回对象的引用
class Test(object):
    def __init__(self):
        print('这是__init__()')
    def __new__(cls, *args, **kwargs):    #cls代表类本身
        print('这是__new__()')
        print(cls)
        # 对父类方法进行扩展  super().方法名()
        res = super().__new__(cls)  #方法重写，res里面保存的是实例对象的引用，
        # __new__()是静态方法，形参里面有cls，实参就必须传cls
        return res
    # 注意：重写__new__()一定要return super().__new__(cls)，
    #     否则python解释器得不到分配空间的对象引用，就不会调用__init__()
te = Test()
print("te:",te)

# 执行步骤：
# 一个对象的实例化过程：首先执行__new__()，如果没有写__new__()，默认调用object里面的__new__()，返回一个实例对象
# 然后再去调用__init__()，对对象进行初始化
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('这是new方法')
        obj = super().__new__(cls)
        print('返回值：',obj)
        return obj
    def __init__(self, name):
        self.name = name   #实例属性
        print("名字是：",self.name)
pe = Person('shutong')
print(pe)
pe2 = Person('susu')
print(pe2)

# 总结：__init__()和__new__()
# 1.__new__()是创建对象，__init__()是初始化对象
# 2.__new__()是返回对象引用，__init__()定义实例属性
# 3.__new__()是类级别的方法，__init__()是实例级别的方法