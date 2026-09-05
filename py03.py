# 1.算术运算符
# 1.1 +-*/
print(1/1)  #注意：使用算术运算符/，商一定是浮点数，且除数不能为0
a = 1/1
print(type(a))
# 1.2 //取整数，取商的整数部分，向下取整
# 向下取整：不管四舍五入的规则，只要后面有小数，就忽略小数
a = 5
b = 2
print(a // b)
# 1.3 % 取余数  只取余数部分
print(a % b)  #5 / 2 = 2 ... 1
# 1.4 ** 幂  m**n： m的n次方
print(a ** b)
print(7.0 // 2)
# 使用算术运算符，其中若有浮点数，结果也会用浮点数表示
# 优先级排序： 幂（最高优先级） > 乘、除、取余、取整数 > 加减
print(3**2+5/2)

# 2.赋值运算符
# =
# 给变量赋值
# num1 = 5
# num2 = 8
# 将一个变量的值赋给另一个变量
# num3 = num1
# print(num3)
# num4 = num2
# print(num4)
# 将运算的值赋给变量
# total = num3 + num4
# print(total)
# 2.2 +=
# a = 1
# print(a)
# a = a + 1
# a += 1  #等效于 a = a + 1
# print(a)
#
# n1 = 99  #成本价
# n2 = 66  #利润
# n1 = n1 + n2  #售价
# n1 += n2  #等效于 n1 + n2 = n1
# print(n1)
# 2.3 -=
# b = 1
# print(b)
# b = b - 1
# b -= 1
# print(b)
# 赋值运算符必须连着写，中间不能有空格，否则会报错
# n += 10 # n + 10 = n，n没有被提前定义，所以不能参与加法运算
# print(n)
# print(10 += 3)  #纯数字也不能使用，报错语法错误，因为赋值运算符是针对变量而存在的

# 3. input()输入函数
# input(prompt) prompt是提示，会在控制台中显示
name = input("请输入姓名：")
print(name)
pwd = input("请输入密码：")
print(pwd)

# 4.转义字符
# 4.1 \t 制表符 通常表示空四个字符，也称缩进
print('shu\ttong')
print("姓名\t年龄\t电话")
# 4.2 \n 换行符 表示当前位置移到下一行开头
print('哈哈\n嘻嘻')
# 4.3 \r 回车 表示将当前位置移到本行开头
print("wang\rshutong")
# 4.4 \\ 反斜杠符号
print('shu\\\tong')
print(r'shu\\\tong')  #r原生字符串，默认取消转义