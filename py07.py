# 4.列表
# 基本格式：
# 列表名 = [元素1,元素2,元素3...]
# 注意：
# 所有元素放在[]内，元素与元素之间用,隔开
# 元素之间的数据类型可以各不相同
from pkgutil import extend_path

li = [1,2,'a',4]
print(li,type(li))
li = [1,2,3,4,5]
print(li,type(li))
# 列表也可以进行切片操作
print(li[0:3])
# 列表是可迭代对象，可是for循环遍历取值
for i in li:
    print(i)

# 5.列表的常见操作
# 5.1添加元素
# append()  extend()  insert()
# li = ['one','two','three']
# li.append('four')   #append整体添加
# li.extend('four')   #extend 分散添加，将另一个类型中的元素逐一添加
# li.insert(4,'four')   #在指定位置插入元素
# li.insert(0,'four')   #指定位置如果有元素，原有元素就会后移
# li.insert('four')   #报错，没有制定下标
# print(li)
# li = [1,2,3]
# li.append(4)
# li.extend(4)   #报错
# li.insert(3,4)
# print(li)

# 5.2修改元素
# 直接通过下标就可以进行修改
li = [1,2,3]
li[1] = 'a'
print(li)

# 5.3查找元素
# in：判断指定元素是否存在列表中，如果存在就返回True，不存在就返回False
# not in：判断指定元素是否存在列表中，如果不存在就返回True，存在就返回False
li = ['a','b','c','d']
print('e' in li)

# 用户输入昵称，昵称重复则不能使用
# 定义一个列表，保存已经存在的昵称
# name_list = ['xixi','haha','hehe']
# while True:   #忘记冒号了
#     name = input('请输入您的昵称')
#     if name in name_list:
#         print(f"您输入的昵称{name}已经存在了")
#     else:
#         print(f"昵称{name}已经被您使用")
#         name_list.append(name)
#         print(name_list)
#         break

# index：返回指定数据所在位置的下标，如果查找的数据不存在就会报错
# count：统计指定数据在当前列表出现的次数
# 跟字符串中的用法相同

# 5.4删除元素
# del
li = ['a','b','c','d']
# del li  #删除列表
del li[2]  #根据下标删除
print(li)

# pop：删除指定下标的数据，Python3版本默认删除最后一个元素
li = ['a','b','c','d']
# li.pop()  #默认删除最后一个元素
li.pop(2)  #不能指定元素删除，只能根据下标进行删除，下标不能超出范围
print(li)

# remove：根据元素的值进行删除
li = ['a','b','c','d','b']
# li.remove('d')
# li.remove('t')  #报错，列表中不存在这个元素
li.remove('b')  #默认删除最开始出现的指定元素
print(li)

# 5.5排序
# sort：将列表按特定顺序重新排列，默认从小到大
# reverse：倒序，将列表倒置（反过来）
li = [1,5,3,2,4]
# li.sort()  #按照从小到大顺序排序
li.reverse()  #倒序
print(li)

# 5.6列表推导式
# 格式一：[表达式 for 变量 in 列表]
# 注意：in后面不仅可以放列表，还可以放range()，可迭代对象
li = [1,2,3,4,5,6]
[print(i*5) for i in li]
li = []
for i in range(1,6):
    print(i)
    li.append(i)
print(li)
[li.append(i) for i in range(1,6)]
print(li)

# 格式二：[表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表
li =[]
for i in range(1,11):
    if i % 2 == 0:
        li.append(i)
print(li)
[li.append(i) for i in range(1,11) if i % 2 == 0]
print(li)

# 5.7列表嵌套
# 含义：一个列表里面又有一个列表
li = [1,2,3,[4,5,6]]   #[4,5,6]是里面的列表
print(li[3])   #取出里面的列表
print(li[3][2])  #取出内列表中的下标为2的元素