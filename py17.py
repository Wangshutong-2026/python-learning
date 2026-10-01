# 1.继承
# 就是让类和类之间转变为父子关系，子类默认继承父类的属性和方法
# 1.1语法
# class 类名(父类名):
#     代码块
# 1.2单继承
class Person():
    def eat(self):
        print('我会吃饭')
    def sing(self):
        print('我是唱歌小能手')
class Girl(Person):  #Person类的子类
    pass   #占位符，代码里面类下面不写任何东西，会自动跳过，不会报错
class Boy(Person):
    pass
girl = Girl()
girl.sing()
girl.eat()
boy = Boy()
boy.sing()
boy.eat()
#总结：子类可以继承父类的属性和方法，就算子类自己没有，也可以使用父类的
# 1.3继承和传递（多重继承）
# A/B/C    C（子类）继承于B类（父类），B（子类）继承于A类（父类），C类具有A/B类的属性和方法
# 子类拥有父类的父类的属性和方法
class Father:
    def eat(self):  #父类
        print('吃饭')
    def sleep(self):
        print('睡觉')
class Son(Father):  #Father类的子类
    def drink(self):
        print('喝水')
class Son2(Son):    #Son的子类
    pass
# son = Son()
# son.eat()
# son.sleep()
son2 = Son2()
son2.sleep()
son2.eat()
son2.drink()
# 继承的传递性就是子类拥有父类以及父类的父类中的属性和方法

# 1.4重写指在子类中定义与父类相同名称的方法
# 1.4.1覆盖父类方法
class Father:    #父类
    def money(self):
        print('一百万需要被继承')
class Son(Father):    #子类
    def money(self):
        print('自己赚一千万')
man = Son()
man.money()
# 1.4.2对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
# 1.父类名.方法名(self)
# 2.super().方法名()    ---推荐使用，懒人写法
# 3.super(子类名.self).方法名()
# super在python里面是一个特殊的类，super()试试用super类创建出来的对象，可以调用父类中的方法

class Person:
    def money(self):
        print('一百万需要被继承')
    def sleep(self):
        print('睡觉')
class Man(Person):
    # pass
    def money(self):
        # Person.money(self)
        super().sleep()  #可以调用父类中的其他方法
        #注意小括号
        # super(Man.self).money()
        print('自己赚一千万')
man = Man()
man.money()

# 2.新式类写法
# 2.1 class A:  #经典类：不由任何内置类型派生出的类
#     pass
class Animal:
    def walk(self):
        print('我会走路')
class Dog(Animal):
    name = '富贵'
    def bite(self):   #Dog类是派生类
        print('我会咬人')
    # pass   #不是派生类
# 2.2 class A()
# 2.3class A(object)     新式类：继承了object类或者该类的子类都是新式类  --推荐使用
# object --对象，python为所有对象提供的基类（顶级父类），提供一些内置的属性和方法，可以使用dir()查看
# print(dir(object))
# python3中如果一个类没有继承任何类，则默认继承object类，因此python3都是新式类

# 3.多继承
# 3.1子类可以拥有多个父类，并且具有所有父类的属性和方法
class Father(object):   #父类一
    def money(self):
        print('一百万需要被继承')
class Mother(object):   #父类二
    def appearance(self):
        print("绝世容颜需要被继承")
class Son(Father, Mother):   #子类
    pass
son = Son()
son.money()
son.appearance()

# 3.2不同的父类存在同名的方法
# 开发时，需要尽量避免这种情况
class Father(object):   #父类一
    def money(self):
        print('一百万需要被继承')
class Mother(object):   #父类二
    def money(self):
        print('一百二十万需要被继承')
    def appearance(self):
        print("绝世容颜需要被继承")
class Son(Mother,Father):   #子类
    # pass
    def money(self):
        print('十万')
son = Son()
son.money()
son.appearance()
# son.func()   #报错
# 有多个父类的属性和方法，如果多个父类具有同名方法的时候，调用就近原则
# 括号内哪一个离得最近，优先调用哪一个类的方法
# 3.3方法的搜索顺序（了解）
# python中内置的属性__mro__可以查看方法搜索顺序
print(Son.__mro__)
# 搜索方法时，会先按照__mro__的输出结果，从左往右的顺序查找
# 如果在当前类中找到了方法，就直接执行，不再搜索
# 如果找到最后一个类，还没有找到这个方法，程序就会报错

# 4.多态
# 指同一种行为具有不同的表现形式
# 4.1多态的前提
# 继承
# 重写
# print(10+10)   #算术运算符：可以实现整型之间的相加操作
# print('10'+'10')   #字符串拼接：实现字符串之间的拼接操作
class Animal(object):
    """父类：动物类"""
    def shout(self):
        print('动物会叫')
class Cat(Animal):
    """子类一：猫类"""
    def shout(self):
        print('小猫喵喵喵')
class Dog(Animal):
    """子类二：狗类"""
    def shout(self):
        print('小狗汪汪汪')
cat = Cat()
cat.shout()
dog = Dog()
dog.shout()
# 4.2多态性：一种调用方式，不同的执行结果
class Animal(object):
    def eat(self):
        print("我会干饭")
class Pig(Animal):
    def eat(self):
        print("猪吃猪饲料")
class Dog(Animal):
    def eat(self):
        print("狗吃狗粮")
# 多态性：定义一个统一的接口，一个接口多种实现
def test(obj):
    obj.eat()
animal = Animal()
pig = Pig()
dog = Dog()
test(animal)
test(pig)
test(dog)
# test函数传入不同的对象，执行不同对象的eat方法

# 5.静态方法
# 使用@staticmethod来进行修饰，静态方法没有self，cls参数的限制
# 静态方法与类无关，可以被转换成函数使用
class Person(object):
    @staticmethod  #静态方法
    def study(name):
        print(f'{name}人类会学习')
# 静态方法可以使用对象访问也可以使用类访问
Person.study('shutong')
pe = Person()
pe.study('susu')   #调用方法时传参数
# 取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗

# 6.类方法
# 使用装饰器@classmethod来标识为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
# class 类名:
#     @classmethod
#     def 方法名(cls.形参):
#         方法体
# 类方法内部可以访问类属性，或者调用其他的类方法
class Person(object):
    name = 'shutong'
    @classmethod
    def sleep(cls):
        print(cls)   #cls代表类对象本身，类本质上就是一个对象
        print("人类在睡觉")
        print(cls.name)
Person.sleep()
print(Person)
# 当方法中需要使用到类对象（如访问私有类属性等），定义类方法
# 类方法一般是配合类属性使用