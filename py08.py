# 1.元组tuple
# 基本格式：元组名 = (元素1,元素2,元素3...)
# 所有元素包含在小括号内，元素与元素之间用，隔开，不同元素也可以是不同的数据类型
tua = (1,2,3,'a','b')
print(type(tua))
tua = ()   #定义空元组
print(type(tua))
tua = ('a',)    #只有一个元素的时候，末尾必须加上,，否则返回唯一的值的数据类型
print(type(tua))

# 1.2元组与列表的区别
#     1.元组只有一个元素末尾必须加,，列表不需要
li = [1]
print(type(li))
    # 2.元组只支持查询操作，不支持增删改操作
li = [1,2,3]
li[1] = 'a'
print(li)

tua = (1,2,3,1)
print(tua[2])  #元组也有下标，从左往右，从0开始
# tua[2] = 'a'    #报错，元祖不支持修改操作
# count()、index()、len()跟列表的用法相同
print(tua.index(2))
print(tua.count(1))
print(len(tua))
print(tua[1:])

# 1.3应用场景
# 函数的参数和返回值
# 格式化输出后面的()本质上就是一个元组
name = 'shutong'
age = 20
print("%s的年龄是:%d" % (name,age))
info = (name,age)
print(type(info))
print("%s的年龄是:%d" % info)
# 数据不可以修改，保护数据的安全

# 2.字典
# 2.1基本格式：字典名 = [键1:值1,键2:值2...]
# 键值对形式保存，键和值之间用:隔开，每个键值对之间用,隔开
dic = {'name':'shutong','age':20}
print(type(dic))
# 字典中的键具备唯一性，但是值可以重复
dic2 = {'name':'shutong','name':'susu'}  #不会报错，键名重复前面的值会被后面的值覆盖
print(dic2)
dic3 = {'name':'shutong','name2':'shutong'}
print(dic3)

# 2.2字典常见操作一
# 2.2.1查看元素
# 变量名[键名]
dic = {'name':'shutong','age':20}
#print(dic[2])   #不可以根据下标，字典中没有下标，查找元素需要根据键名，键名相当于下标
print(dic['age'])  #20
# print(dic['sex'])   #报错，键名不存在
#变量名.get(键名)
dic = {'name':'shutong','age':20}
print(dic.get('name'))  #shutong
print(dic.get('tel'))   #None   键名不存在，返回None
print(dic.get('tel','不存在哦'))  #不存在哦    如果没有这个键名，返回自己设置的默认值

# 2.2.2修改元素
# 变量名[键名] = 值
dic = {'name':'shutong','age':20}
dic['age'] = 18   #列表通过下标修改，字典通过键名修改
print(dic)

# 2.2.3添加元素
# 变量名[键名] = 值
# 注意：键名存在就修改，不存在就新增
dic = {'name':'shutong','age':20}
dic['tel'] = 12789   #此时没有tel键，新增进字典
print(dic)
dic['tel'] = 12345   #此时已经有了tel键了，修改tel对应的值
print(dic)
dic['remark'] = '在线征婚'
print(dic)
dic['remark'] = '是个好人'
print(dic)

# 2.2.4删除元素
# del
# 删除整个字典  del 字典名
# dic = {'name':'shutong','age':20}
# del dic
# print(dic)  #报错，已经被删除了，找不到这个字典
#删除指定键值对，键名不存在就会报错  del 字典名[键名]
dic = {'name':'shutong','age':20}
del dic['age']
# del dic['tel']   #没有指定的键就会报错
print(dic)

# clear():清空整个字典里面的东西，但保留了这个字典
dic = {'name':'shutong','age':20}
dic.clear()
print(dic)

# pop()  删除指定键值对，键不存在就会报错
dic = {'name':'shutong','age':20}
# dic.pop('age')
# dic.pop('tel')   #报错，不存在键名
# dic.pop()   #报错，没有指定键名
dic.popitem()   #3.7之前的版本是随机删除一个键值对，3.7之后的版本默认删除最后一个键值对
print(dic)

# 2.3字典常见操作二
# 2.3.1 len()求长度
dic = {'name':'shutong','age':20,'tel':'123'}
print(len(dic))  #3，字典中有3个键值对
li = [1,2,3,4]
print(len(li))
st = 'hello'
print(len(st))

# 2.3.2 keys():返回字典里面包含的所有键名
dic = {'name':'shutong','age':20,'tel':'123'}
print(dic.keys())  #dict_keys(['name', 'age', 'tel'])
# for循环取出键名
for i in dic:  #只取出键名
    print(i)

# 2.3.3 values()：返回字典里面包含的东西
dic = {'name':'shutong','age':20,'tel':'123'}
print(dic.values())
for i in dic.values():
    print(i)

#2.3.4 item(): 返回字典里面包含的所有键值对，键值对以元组形式
dic = {'name':'shutong','age':20}
print(dic.items())
for i in dic.items():
    print(i,type(i))  #i是元组类型

# 2.4字典的应用场景
# 使用键值对，存储描述一个物体的相关信息
#
# 3.集合 set
# 3.1 基本格式： 集合名 = {元素1,元素2,元素3...}
# s1 = {1,2,3}
# s1 = {}  #定义空字典
s1 = set()  #定义空集合   要用()而不是{}
print(s1,type(s1))

# 3.2集合具有无序性
s1 = {'a','b','c','d','e','f'}
print(s1)  #每次运行结果都不一样
s2 = {1,2,3,4,5,6}
print(s2)  #数字运行结果都一样

# 集合无序的实现方式涉及hash表（了解）
print(hash('a'))
print(hash('b'))
print(hash('c'))
# 每次运行结果都不同，hash值不同，那么在hash表中的位置也不同，这就实现了集合的无序性
print(hash(1))
print(hash(2))
print(hash(3))
# python中int整型的hash值就是它本身，在hash表中的位置不会发生改变，所以顺序也不会改变
print(hash('1'))
print(hash('2'))
print(hash('3'))
print(hash('4'))
# 用引号括起来整型就变成了字符串类型，所以hash值还是会发生改变
# 无序性：不能修改集合中的值

# 3.3集合具有唯一性，可以自动去重
s1 = {1,2,3,4,3,4,1,5}
print(s1)

# 3.4集合的常见操作
# 3.4.1添加元素
# add添加的是一个整体
s2 = {1,2,3,4}
print("原集合：",s2)
# 集合的唯一性，决定了如果需要添加的元素在原集合中已经存在，就不进行任何操作
s2.add(1)
s2.add(5)
# s2.add(5,6)  #一次只能添加一个元素
s2.add((5,6))
print("现集合：",s2)

# update 把传入的元素拆分，一个个放进集合中
s2 = {1,2,3,4}
print("原集合：",s2)
s2.update((5,6,7))  #元素必须是能够被我们for循环取值的可迭代对象
print("添加后：",s2)

# 3.4.2 删除元素
# remove：选择删除的元素，如果集合中有就删除，没有就会报错
s2 = {1,2,3,4}
s2.remove(3)
# s2.remove(5)  #报错，集合中没有5这个元素
print("删除后：",s2)

# 2.pop:对集合进行无序排列，然后将左边的第一个元素删除
s2 = {'a','b','c','d'}
print("原集合：",s2)
s2.pop()  #默认删除根据hash表排序后的第一个元素
print("删除后：",s2)

# 3.discard：选择要删除的元素，有就会删除，没有则不会发生任何改变，即不会进行任何操作
s2 = {1,2,3,4}
print("原集合：",s2)
s2.discard(3)
s2.discard(7)
print("删除后：",s2)

# 4.交集和并集
# 4.1交集 &
# 含义：共有的部分
a = {1,2,3,4}
b = {3,4,5,6}
# b = {5,6,7,8}   #没有共有的部分返回空集合set()
print(a & b)
s1 = {'a','b'}
s2 = {'c','d'}
print(s1 & s2)
#
# 4.2并集 |
# 含义：所有的都放在一起，重复的不算（集合的唯一性）
a = {1,2,3,4}
b = {3,4,5,6}
b = {5,6,7,8}
print(a | b)
l = a | b
print(type(l))