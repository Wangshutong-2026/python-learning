# 1.字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# 1.2Unicode ： 所有字符都是2个字符
# 好处：字符与数字之间的转换速度更快一些
# 坏处：占用空间大
#
# 1.3UTF-8 ：精准，对不同的文字用不同的长度表示
# 优点：节省空间
# 缺点：字符与数字的转换速度较慢，每次都需要计算字符要用多少个字节来表示
#
# 1.4字符串编码转换
from itertools import count
from shlex import split

a = 'hello'
print(a,type(a))  #str，字符串是以字符为单位进行处理
a1 = a.encode()   #编码
print("编码后：",a1)   #bytes，以字节为单位进行处理的
a2 = a1.decode()  #解码
print(a2,type(a2))
# 注意：对于bytes，只需要知道它跟字符串类型之间的互相转换

st = "我是大学生"
st1 = st.encode('UTF-8')
print(st1,type(st1))
st2 = st1.decode('UTF-8')
print(st2,type(st2))

# 2.字符串常见操作
# 2.1 + 字符串拼接
print(10+10)  #20，整数相加，+是算术运算符
print("10"+"10")  #1010，字符串相加，+是字符串拼接
name1 = "王"
name2 = "小彤"
print(name1 + name2)
print(name1 , name2,sep="")

# *重复输出
print("好好学习，天天向上\n"*5)
# 注意：需要输出多少次*后面就写多少
print('&\t'*10)

# 2.2成员运算符
# 作用：检查字符串中是否包含了某个子字符串（即某个字符或多个字符）
# in：如果包含的话，返回True，不包含返回False
# not in：如果不包含的话，返回True，包含返回False
name = 'shutong'
print('s' in name)  #True
print('t' in name)  #True
print('a' not in name)  #True
print('s' not in name)  #False
print('shu' in name)  #True
print('sha' in name)  #False

name = '姝彤'
print('shu' in name)  #False
print('姝彤' in name)  #True
print('书彤' in name)  #False

# 2.3下标
# Python中下标从0开始
# 作用：通过下标能够快速找到对应的数据
# 格式：字符串名[下标值]
name = 'shutong'
# 从左向右数，下标从0开始
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7])  #报错，取值的时候不要超出下标范围
# 从右向左数，下标从-1开始，-1，-2 ...
print(name[-1])
print(name[-2])
# print(name[-8]) #报错，超出索引范围

# 2.4切片
# 含义：指对操作的对象截取其中一部分的操作
# 语法:[开始位置:结束位置:步长]
# 包前不包后：即从起始位置开始，到结束位置的前一位结束（不包含结束位置本身）
st = 'abcdefghigk'
print(st[0:4])  #abcd
print(st[4:7])  #efg
print(st[3:])  #defghigk
print(st[:7])  #abcdefg
# 从右往左
print(st[-1:])  #k
print(st[:-1])  #abcdefghig
print(st[-1:-5])  #
# 步长：表示选取间隔，不写步长，则默认为1
# 步长的绝对值大小决定切取的间隔，正负号决定切取方向
# 正数表示从左往右取值，负数表示从右往左取值
st = 'abcdefghigk'
print(st[-1::-1])  #kgihgfedcba
print(st[-1:-5:-1])  #kgih
print(st[0:7:3])

# 3.字符串常见操作
# 3.1 查找
# 1.find：检测某个子字符是否包含在在子字符串中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
# find（子字符串，开始位置下标，结束位置下标）
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = 'tongtong'
print(name.find('o'))  #1   第一个o的下标为1
print(name.find('tong'))  #0   检测到第一个tong，t的下标为0
print(name.find('t',3))  #4
print(name.find('t',5))  #-1   超出范围，不包含返回-1
print(name.find('t',3,5))  #4   在下标3-5位置范围内查找
# 包前不包后
print(name.find('t',3,4))  #-1

# 2.index():检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就会报错
# index(子字符串，开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = '我命由我不由天'
print(name.index("命"))  #1
# print(name.index("命",2))  #报错，从下表2开始找，没有找到
print(name.index("命",1,3))  #1
# 同样遵循包前不包后原则
# 和find的区别，find没找到，返回-1，index没找到就会报错

# 3.count():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串中查找
name = 'tongtong'
print(name.count("t"))  #2
print(name.count("a"))  #0
print(name.count("t",1))  #1
print(name.count("t",1,3))  #0
print(name.count("t",1,4))  #0   同样遵循包前不包后原则

# 3.3判断
# 1.startswith()：是否以某个子字符串开头，是的话就返回True，不是的话就返回False，如果设置开始和结束位置
# 则在指定单位内检查
# startswith(子字符串，开始位置下标，结束位置下标)
st = 'shutong'
print(st.startswith('shu'))  #True
print(st.startswith('sha'))  #False
print(st.startswith('s',2,6))  #False

#2.endswith():是否以某个子字符串结尾，是的话就返回True，不是的话就返回False，如果设置开始和结束位置
# 则在指定单位内检查
# endswith(子字符串，开始位置下标，结束位置下标)
st = 'shutong'
print(st.startswith('eg'))  #False

# 3.isupper():检测字符串中所有字母是否都为大写，是的话就返回True
st = 'shutong'
print(st.isupper())  #False
print("SHU".isupper())  #True

# 3.2修改元素
# 1.replace():替换
# replace(旧内容，新内容，替换次数)
# 注意：替换次数可以省略，默认全部替换
name = '好好学习，天天向上'
print(name.replace("天","时"))  #好好学习，时时向上
print(name.replace("天","时",1))  #好好学习，时天向上

# 2.split():指定分隔符来切字符串
st = "hello,python"
print(st.split(','))  #['hello', 'python'],以列表的形式返回
#如果字符串中不包含分割内容，就不进行分割，会作为一个整体
print(st.split('a'))  #['hello,python']
print(st.split('o'))  #['hell', ',pyth', 'n']
print(st.split('o',1))  #['hell', ',python']  指定只分割一次

# 3.capitalize():第一个字符大写,其他都小写
st = 'bingBing'
print(st.capitalize())

# 4.lower():大写字母转为小写
st = 'bIngBinG'
print(st.lower())

# 5.upper():小写字母转为大写
st = 'bIngBinG'
print(st.upper())