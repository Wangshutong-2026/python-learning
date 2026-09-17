# 1.类型转换
# 1.1 int():转换为一个整数，只能转换由纯数字组成的字符串
# float -> int
a = 1.2
print(type(a))
b = int(a)
print(b,type(b))
print(int(1.8))
# 浮点型强转整型会去掉小数点及后面的数值，只保留整数部分
# str -> int
a = int('123')
print(a,type(a))
# print(int('shutong'))  #报错
# 如果字符串中有数字和正负号（+/-）以外的字符就会报错
print(int('-10'))
# +/-写在前面表示正负号，不可以写在后面
# print(int('10-'))  #报错

#用户从控制台输入，判断年龄
# age = int(input("请输入您的年龄"))   #input默认输入的是字符串类型
# print(type(age))
# if age >= 18:
#     print("成年了")

# 1.2float():转换为一个小数
print(float(11))   #整型转换为浮点型，会自动添加一位小数
print(float(-11))
print(float('+11.345'))
#print(float('10-'))   #如果字符串中有正负号、数字和小数点以外的字符，则不支持转换

# 1.3str():转换为字符串类型，任何类型都可以转换成字符串类型
n = 100
print(type(n))  #<class 'int'>
n2 = str(n)
print(n2,type(n2))  #100 <class 'str'>
st = str(-1.800)
print(st,type(st))   # -1.8   float转型成str会取出末位为0的小数部分,保留一位小数
li = [1,2,3]
st = str(li)
print(st,type(st))

# 1.4eval()：用来执行一个字符串表达式，并返回表达式的值
print(10+10)
print('10'+'10')
print(eval('10+10'))  #20 执行运算，并返回运算值
# print(eval(10+'10'))  #报错。整型和字符串不可以相加

# eval():可以实现list、dict、tuple和str之间的转换
# str -> list
st1 = "[[1,2],[3,4],[5,6]]"
print(type(st1))
li = eval(st1)
print(li,type(li))

# str -> dict
st2 = "{'name':'shutong','age':20}"   #字典用{}，列表用[]
dic = eval(st2)
print(dic,type(dic))

# eval()非常强大，但是不够安全，容易被恶意修改数据，不建议使用

# 1.5list():将可迭代对象转换成列表
# 支持转换为list的类型：str、tuple、dict、set
# str -> list
print(list('abcdef'))
# print(list(123456))   #报错，整型不是可迭代对象

# tuple -> list
print(list((1,2,3,4)))

# dict -> list
print(list({'name':'shutong','age':20}))
#字典转换成列表，会取键名作为列表的值

# set -> list
print(list(set('abcdbc')))
# 集合转换成列表，会先去重，再转换

# 2.深浅拷贝
# 2.1赋值
li = [1,2,3,4]
print(li)
li2 = li  #将li直接复制给li2
print('li',li,id(li))
print('li2',li2,id(li2))
# 给li列表新增元素
li.append(5)
print('新增后的li',li)
print('新增后的li2',li2)
# 赋值:等于完全共享资源，一个值的改变会完全被另一个值共享

# 2.2浅拷贝（数据半共享）
# 会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
import copy  #导入copy模块
li = [1,2,3,[4,5,6]]    #定义一个嵌套列表
li2 = copy.copy(li)   #浅拷贝
print('li',li)
print('li2',li2)
# 查看内存地址id()
print("li内存地址：",id(li))
print("li2内存地址：",id(li2))
# 内存地址不一样，说明不是同一个对象
li.append(8)
print('li',li)
print('li2',li2)
#往嵌套列表添加元素
li[3].append(7)
print('li',li)
print('li2',li2)
print("li[3]内存地址：",id(li[3]))
print("li2[3]内存地址：",id(li2[3]))
# 外层的内地址不同，但是内层的内层地址相同

# 优点：拷贝速度快，占用空间小，拷贝效率高

# 2.3深拷贝(数据完全不共享)
# 外层的对象和内部的元素都拷贝了一遍
import copy  #导入copy模块
li = [1,2,3,[4,5,6]]
li2 = copy.deepcopy(li)  #深拷贝
print('li',li,id(li))
print('li2',li2,id(li2))
li.append(8)
print('li',li)
print('li2',li2)
#往嵌套列表添加元素
li[3].append(7)
print('li',li)
print('li2',li2)
print("li[3]内存地址：",id(li[3]))
print("li2[3]内存地址：",id(li2[3]))
#深拷贝数据变化只影响自己本身，跟原来的对象没有联系

# 3.可变类型
# 含义：变量对应的值可以修改，但是内存地址不会发生改变
# 常见可变类型：list、dict、set
li = [1,2,3,4]
print("li的原内存地址：",id(li))
li.append(5)
print(li)
print("li的现内存地址：",id(li))
dic = {'name':'shutong','age':20}
print(dic,id(dic))
dic['name'] = 'susu'  #修改元素
print(dic,id(dic))

set = {1,2,3,4,5}
print(set,id(set))
set.remove(3)  #删除元素
print(set,id(set))

# 4.不可变对象
# 含义：变量对应的值不能被修改，如果修改就会生成一个新的值从而分配新的内存空间
n = 10 #整型
print("原地址：",n,id(n))    #不要忘记用,隔开
n =15
print("修改后：",n,id(n))
#内存地址不一样，修改n的值就会生成新的值，重新赋值给变量a

st = 'hello'  #字符串
print(st,id(st))
st = ('shutong')
print(st,id(st))

tua = (1,2,3)
print(tua,id(tua))
#不支持新增删除和修改操作
tua = ('a','b','c')
print(tua,id(tua))

#注意：前面所说的深浅拷贝只针对可变对象，不可变对象没有拷贝的说法