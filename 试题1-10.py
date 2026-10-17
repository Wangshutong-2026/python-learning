# 1.编写一个程序，找到2000年至3200年(包括在内)中所有可被7整除但不能被5整除的所有数字，
# 得到的数字按逗号分隔，打印在一行上。

# li = []   #不能定义在for循环里，每次循环都会清空
# for i in range(2000,32001):
#     if i % 7 ==0 and i % 5 != 0:
#         li.append(str(i))   #转成字符串数据类型，join只吃字符串
# print(','.join(li))   #join()把所有元素拼接成一个巨大的字符串

# 2.编写一个可以计算给定数阶乘的程序，结果以逗号分隔，打印在一行上。

# def funa(n):
#     if n == 0:
#         return 1
#     return n*funa(n-1)
# print("请输入一个数字：")
# n = int(input())
# print(funa(n))

# 3.使用给定的整数n，编写程序生成一个包含(i, i×i)的字典，该字典包含从1到n之间的整数(两者都包含)，然后打印字典。

# print("请输入一个数字：")
# n = int(input())
# d = dict()
# for i in range(1,n+1):
#     d[i] = i * i
# print(d)

# 4.编写一个程序，该程序接收控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设，
# 向程序提供以下输入：34岁,67年,55岁,33岁,12日,98年；
# 则输出为:['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# import re
# print("请输入数据：")
# values = input()
# k = re.findall(r'\d+',values)  #返回列表
# l = tuple(k)
# print(k)
# print(l)

# 5.定义一个至少有两个方法的类：一、getString：从控制台输入获取字符串；二、printString：打印大写的字符串，并写出简单的测试函数来测试类方法。

# class InputOutString(object):
#     def __init__(self):
#         self.s = ''
#     def getString(self):
#         print('请输入数据：')
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())
# str1 = InputOutString()
# str1.getString()
# str1.printString()

# 6.编写一个程序，根据给定的公式计算并打印值。Q=根号下（2*C*H）/H其中，假设C=50，H=30。
# D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 例：程序的输入序列为（以逗号分隔）：100,150,180；则程序输出为：18,22,24；

# import math
# c = 50
# h = 30
# values = []
# print('请输入数据：')
# items = [x for x in input().split(',')]
# #先把输入字符串按逗号切开，得到字符串列表，挨个取出里面每一个字符串给 x ，然后收集进新列表
# for d in items:  #d现在是字符串要转换成浮点数
#     values.append(str(int(round(math.sqrt(2*c*float(d)/h)))))  #round()四舍五入
#     print(','.join(values))

# 7.编写一个程序，X,Y作为输入，生成一个二维数组，数组的第i行和第j列的元素值应该是i×j。
# 注意：i=0,1…X‑1；j=0,1…Y‑1。假设程序输入3,5；则程序输出为：[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]；

# print("请输入两个数字：")
# s = input()
# nums = [int(x) for x in s.split(',')]
# X = nums[0]   # 行数
# Y = nums[1]   # 列数
# multi = []
# for i in range(X):  #循环嵌套
#     row = []
#     for j in range(Y):
#         row.append(i * j)
#     multi.append(row)
# print(multi)

# 8.编写一个程序，以逗号分隔的单词序列作为输入，按照字母顺序对单词进行排序，并通过逗号分隔的序列来打印单词。
# 假设向程序输入：without,hello,bag,world；则输出为：bag,hello,without,world；

# items = [x for x in input().split()]
# items.sort()
# print(','.join(items))

# 9.编写一个程序，接收一行序列作为输入，并将句子中的所有字符大写后打印。

#多行输入  (有点问题)
# l3 = []
# while True:
#     s = input()
#     if s:
#         l3.append(s.upper())
#     else:
#         break
#     for s1 in l3:
#         print(s1)

#单行输入：
# s = input()
# print(s.upper())

# 10.编写一个程序，以一系列空格分隔的单词作为输入，并在删除所有重复的单词后，按字母顺序排序后打印这些单词。
# 假设向程序输入：hello world and practice makes perfect and hello world again
# 则输出为：again and hello makes perfect practice world

# print("请输入数据：")
# s = input()
# l = [x for x in s.split('')]
# print(''.join(sorted(list(set(l)))))
# #set集合去重，转为列表进行sorted排序