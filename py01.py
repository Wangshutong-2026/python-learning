#1.python是什么
#python是面向对象的解释型高级编程语言
#python是强类型的动态脚本语言

#2.编写第一个程序
print("HELLO WORLD")
#运行py文件推荐使用方式：右键点击代码空白处，选择Run...

#3.bug
#1.输入错误
#print(“123”) # 报错，中文引号
#注意：python中的符号都是要用英文模式下的
#2.缩进错误
#print(123)
#注意：print要顶格写，否则报错
#3.语法错误
#print(123)print(456)
#两个print不能写在同一行，一个print必须单独写一行，错误信息中遇到Syntax说明语法有问题
#4.命名错误
#print(WORLD)
# #错误原因：WORLD是字母，那么就是字符串，必须要加上引号，中文也要，单引号或者双引号都可以

#debug中代码为蓝色时表示即将要运行的代表
#Show execution Point  显示执行的断点
#Step Into  下一步
#Run to Cursor  跳到下一个断点的位置
#总结：可以通过debug调试看到程序执行的顺序

#4.注释
print("HELLO WORLD")   #我要输出HELLO WORLD
#我要输出HELLO WORLD  #print("HELLO WORLD")
#注意：注释可以放在任意位置，但是注释的内容不会被程序执行
"""
多行注释
print(123)
"""
'''
多行注释+1
print(123)
'''
#多行注释就是三引号，可以是三对单引号，也可以是三对双引号，三引号的内容也不会被程序执行
#Ctrl+/既可以添加注释，也可以取消注释，使用的是单行注释
# Ctrl+Z 撤销
# Ctrl+C 复制
# Ctrl+V 粘贴
# Ctrl+F 查找
# Ctrl+D 复制到下一行
#5.输出函数print()
# *values  值，表示可以一次输出多个对象，输出多个对象时，需要用,分隔
print("哈哈哈","嘿嘿嘿","嘻嘻嘻", sep='|')
#输出多个值或者多句话时，需要用,隔开，英文模式下的
#sep就是用来间隔多个值，默认是空格
#end用来设定以...结尾，默认值是换行符\n，可以切换成其他字符串
print("hello world",end="!")
print("shutong")
#print(字符串，end="后面拼接的值")最后输出的结果：第一个print中的字符串+后面拼接的值+第二个print中的字符串