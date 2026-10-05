# 3.1 with open
# 作用：代码执行完，系统会自动调用f.close()，可以省略文件关闭步骤
with open('test.txt', 'w') as f:   #f是文件对象
    f.write('Hello world')
    print(f.closed)
print(f.closed)
with open('test.txt', 'w',encoding='utf-8') as f:
    f.write('我是最棒的！')
# with open('test.txt',encoding='utf-8') as f:
#     print(f.read())

# 案例：图片复制 'rb'
"""
1.读取图片
图片是一个二进制文件，想要写入必须要先拿到
2.写入图片
"""
with open(r"C:\Users\L\Desktop\紫.jpg",'rb') as file:
    img = file.read()
    print(img)
# 将读取到的内容写入到当前文件中
with open("C:\\Users\\L\\PycharmProjects\\python-learning\\紫.jpg",'wb') as f:
    f.write(img)

# 4.目录常用操作
# #导入模块
# import os
# 1.文件重命名 os.rename(旧名字,新名字)
# os.rename('test.txt','shutong.txt')
# 2.删除文件 os.remove()
# os.remove('紫.jpg')
# 3.创建文件夹 os.mkdir()
# os.mkdir('shutong')
# 4.删除文件夹 os.rmdir()
# os.rmdir('shutong')
# 5.获取当前目录 os.getcwd()
# print(os.getcwd())
# 6.获取目录列表
# print(os.listdir())   #获取当前目录列表
# print(os.listdir('../'))   #获取上一级目录的列表