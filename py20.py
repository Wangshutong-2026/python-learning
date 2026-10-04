# 1.文件
# 文件就是存储在某种长期储存设备上的一段数据
# 1.2文件操作
# 打开文件 --> 读、写文件 -->关闭文件
# 1.3文件对象的方法
# 1.open()：创建一个file对象，默认是以只读模式打开
# 2.read(n)：n表示从文件中读取的数据的长度，没有传n值就默认一次性读取文件中的所有内容
# 3.write()：将指定内容写入文件
# 4.close()：关闭文件
# 1.4属性
# 文件名.name：返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode：返回文件的访问模式
# 文件名.closed：检测文件是否关闭，关闭就返回Ture
from os import read

# 1.打开文件
f = open('test.txt')
print(f.name)  #文件名
print(f.mode)  #文件访问模式
print(f.closed)

# 2.关闭文件
f.close()
print(f.closed)

# 2.读写操作
# 2.1read(n)：n表示从文件中读取的数据的长度，没有传n值或者传的是负值就默认一次性读取文件的所有内容
f = open(r'C:\Users\L\Desktop\test.txt')  #r:转义
# print(f)
print(f.name)   #文件所在的具体路径
# print(f.read(-1))
print(f.read(5))  #最多读取5个数据
f.close()

# 2.2readline():一次读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
f = open('test.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())

while True:
    test = f.readline()  #读取一行内容
    #读取不到内容要退出循环
    if not test:
        break
    print(test)
# for i in f:
#     print(i)
f.close()

# 2.3readlines():按照行的方式，把文件内容一次性读取，返回的是一个列表，每一行的数据就是列表中的一个元素
f = open('test.txt')
test = f.readlines()
print(test)   #返回列表
print(type(test))   #<class 'list'>
for i in test:
    print(i)
f.close()

# 2.4访问模式
# 2.4.1 r：只读模式（默认模式），我呢间必须存在，不存在就会报错
# 2.4.1 w：只写模式，文件存在就会先清空文件内容，再写入添加内容，不存在就创建文件
file = open('test01.txt','w')
# print(file.read())
file.write('gagagagga')    #重复编辑文件内容，原有内容会被覆盖
file.close()

# 2.4.3 +：表示可以同时读写某个文件
# 使用+会影响文件的读写效率，开发过程中更多时候会以只读、只写的方式来操作文件
# r+：可读写文件，文件不存在就会报错
# w+：先写后读，文件存在就重新编辑文件，不存在就创建新文件
f = open('test.txt','w+')
print(f.read())
f.write('shutong')
print(f.read())
f.close()

# 2.4.4 a:追加模式，不存在就创建文件进行写入，存在则在原有内容的基础上追加新的内容
f = open('test.txt','a')
# print(f.read())
f.write('\ntest is being eritten')
f.close()
# # 文件指针：标记从哪个位置开始读取数据
f = open('test.txt','w+')
f.write('Hello world')
print(f.read())
f.close()

f = open('test.txt')
print(f.read())
f.close()

# 2.5文件定位操作
# tell()和seek()
# tell()：显示文件内当前位置，即文件指针的当前位置
# seek(offset,whence)：移动文件读取指针到指定位置
# offset：偏移量，表示要移动的字节数
# whence：起始位置，表示移动字节的参考位置，默认是0,0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表将文件结尾作为参考位置
# seek(0,0)就会把文件指针移到文件开头
f = open('test.txt','w+')
f.write('Hello python!')
pos = f.tell()   #13---文件内容长度
print('当前文件指针所在位置：',pos)
f.seek(0,0)   #把指针移到开头
pos2 = f.tell()
print('移动后所在位置：',pos2)
print(f.read())
f.close()