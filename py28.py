# 导入os模块
import os
# 导入sys模块
import sys
# 导入time模块
import time
# 导入logging模块
import logging
# 导入random模块
import random
from logging import CRITICAL, INFO, NOTSET
from time import struct_time

# 一、os模块
# 作用：用于和操作系统进行交互
# 1.os.name    #指示正在使用的工作平台（返回操作系统类型）
print(os.name)
# 对于Windows，返回nt，对于Linux，返回posix
# 2.os.getenv(环境变量名称)   #读取环境变量
print(os.getenv('path'))
# 3.os.path.split()   #把目录名和文件名分离，以元组的形式接受，第一个元素是目录路径，第二个元素是文件名
print(os.path.split(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))
o = os.path.split(r'C:\Users\L\PycharmProjects\python-learning\py28.py')
print(o[1])
# 4.os.path.dirname()    #显示split分割的第一个元素，即目录
# 5.os.path.basename()    #显示split分割的第二个元素，即文件名
print(os.path.dirname(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))
print(os.path.basename(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))
# print(os.path.basename(r'C:\Users\L\PycharmProjects\python-learning\'))
#报错，如果路径以/结尾，那么就返回空值，如果以\结尾，会报错
# 6.os.path.exists()    #判断路径（文件或目录）是否存在，存在的话就返回True，不存在就返回False
print(os.path.exists(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))   #True
print(os.path.exists(r'C:\Users\L\PycharmProjects\python-learning\py8.py'))    #False
# 7.os.path.isfile()    #判断是否存在文件
print(os.path.isfile(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))   #True
print(os.path.isfile(r'C:\Users\L\PycharmProjects\python-learning'))   #False
print(os.path.isfile(r'C:\Users\L\PycharmProjects\python-learning\py8.py'))   #False
# 8.os.path.isdir()     #判断目录是否存在
print(os.path.isdir(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))   #False
print(os.path.isdir(r'C:\Users\L\PycharmProjects\python-learning'))   #True
# 9.os.path.abspath()   #获取当前路径下的绝对路径
# 10.os.path.isabs()    #判断是否是绝对路径
print(os.path.abspath('py28.py'))
print(os.path.abspath('py8.py'))   #不存在也没关系
print(os.path.isabs(r'C:\Users\L\PycharmProjects\python-learning\py28.py'))   #True
print(os.path.isabs(r'C:\Users\L\PycharmProjects\python-learning\py8.py'))   #True

# 二、sys模块
# 作用：负责程序跟python解释器的交互
# 1.sys.getdefaultencoding()  #获取系统默认编码格式
print(sys.getdefaultencoding())
# 2.sys.path                  #获取环境变量的路径，跟解释器相关
print(sys.path)  #以列表的形式返回，第一项为当前所在的工作目录
# 3.sys.platform              #获取操作系统平台名称
print(sys.platform)
# 4.sys.version               #获取python解释器的版本信息
print(sys.version)

# 三、time模块
# 三种时间表示
#   1.时间戳（timestamp）
#   2.格式化的时间字符串（format time）
#   3.时间元组（struct_time）
# 1.time.sleep()  #延时操作，以秒为单位
print(12)
time.sleep(2)
print(123)
# 2.time.time()  #获取当前的时间戳：以秒计算，从1970年1月1日 00:00:00开始到现在的时间差
print(type(time.time()))   #返回的是浮点型
# 3.time.localtime()   #将一个时间戳转换为当前时区的struct time，九个元素
print(type(time.localtime()))
t = time.localtime()
print(t.tm_year)
# 4.time.asctime()   #获取系统当前时间，把struct_time换成固定的字符串表达式
print(time.asctime())
t = time.localtime()
print(t)
print(time.asctime(t))
# 5.time.ctime()   #获取系统当前时间，把时间戳转换成固定的字符串表达式
print(time.ctime())
t = time.time()
# t = time.localtime()  #会报错
print(time.ctime(t))

# 6.time.strftime(格式化字符串,struct_time)   #将struct_time转换成时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(type(t))
# 7.time.strptime(时间字符串,格式化字符串)   #将时间字符串转换成struct_time
print(time.strptime('2026-10-14','%Y-%m-%d'))
t = time.strptime('2026-10-14','%Y-%m-%d')
print(type(t))

# 四、logging模块
# 1.作用：用于记录日志信息
# 2.日志的作用
#   1.程序调试
#   2.了解软件程序运行情况是否正常
#   3.软件程序运行故障分析与问题定位
# 3.级别排序（从高到低）
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')
#logging默认的level就是warning，也就是说logging只会显示级别大于等于warning的日志信息
# 4.logging.basicConfig()  #配置 root logger的参数
#   1.filename:  指定日志文件的文件名，所有会显示的日志都会存放到这个文件中去
# logging.basicConfig(filename = 'log.log')
  # 2.filemode:  文件的打开方式，默认是a，追加模式
# logging.basicConfig(filename = 'log.log', filemode = 'w')
  # 3.level:  指定日志显示级别，默认是警告信息warning
# logging.basicConfig(filename = 'log.log', filemode = 'w',level = logging.NOTSET)
  # 4.format:  指定日志信息的输出格式
logging.basicConfig(filename = 'log.log',
                    filemode = 'w',level = logging.NOTSET,
                    format='%(levelname)s:%(asctime)s\t%(message)s')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

# 五、random模块
# 作用：用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值
# 1.random.random()  #产生大于0且小于1之间的小数
print(random.random())
# 2.random.uniform()  #产生指定范围的随机小数
print(random.uniform(1,3))
# 3.random.randint()  #产生指定范围内的随机整数，包括开头和结尾
print(random.randint(1,3))
# 4.random.randrange(start,stop,[step])  #产生start，stop范围内的整数，包含开头但不包含结尾
# step 指定产生随机的步长，随机选择一个数据
print(random.randrange(2,5,2))