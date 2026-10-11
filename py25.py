import time  #导入时间模块
from greenlet import greenlet    # 导入greenlet模块
import gevent   #导入gevent模块
# 1.协程：单线程下的开发，又称为微线程
# 注意：线程和进程的操作是由程序触发系统接口，最后的执行者是系统，协程的操作则是程序员
# 1.1简单实现协程
# def task1():
#     while True:
#         yield '哈哈哈'
#         time.sleep(1)
#     # yield 'a'
#     # yield '哈哈哈'
# def task2():
#     while True:
#         yield '嘿嘿嘿'
#         time.sleep(1)
#     # yield 'b'
#     # yield '嘿嘿嘿'
# if __name__ == '__main__':
#     t1 = task1()
#     # print(t1)
#     t2 = task2()
    # print(next(t1))
    # print(next(t2))
    # print(next(t1))
    # print(next(t2))
    # while True:
    #     print(next(t1))
    #     print(next(t2))

# 1.2应用场景
#     1.如果一个线程里面IO操作比较多的时候，可以用协程
#       Input/Output
#       常见的IO操作：文件操作、网络请求
#     2.适合高并发处理

# 2.greelet：是一个由C语言实现的协程模块，通过设置swich()来实现任意函数之间的切块
# 2.1安装第三方模块
# 安装：pip install 模块名
# 卸载：pip uninstall 模块名
# 若失败，就加上前缀 python -m
# 查看已安装的模块：pip list
# 2.2注意：greelet属于手动切换，当遇到IO操作，程序会阻塞，而不能进行自动切换
# 2.3通过greenlet实现任务的切换

def sing():
    print('在唱歌')
    g2.switch()
    print('唱完歌了')
def dance():
    print('在跳舞')
    print('跳完舞了')
    g1.switch()
# sing()
# dance()
if __name__ == '__main__':
    #创建协程对象 greenlet(对象名)
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    g1.switch()  #切换到g1中去运行
    g2.switch()

# 3.gevent：遇到IO操作时，会进行自动切换，属于主动式切换
# 注意：文件命名不要和第三方模块或内置模块重名

# 3.1使用
# gevent.spawn(函数名):创建协程对象
# gevent.sleep():     耗时操作
# gevent.join():      阻塞，等待某个协程执行结束
# gevent.joinall():   等待所有协程对象都执行结束再推出，参数是一个协程对象列表
def sing():
    print('在sing')
    gevent.sleep(3)
    print('sin完歌了')
def dance():
    print('在dance')
    gevent.sleep(2)
    print('dan完舞了')
if __name__ == '__main__':
    # 1.创建协程对象
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    # 2.阻塞，等待协程执行结束
    g1.join()  #等待g1对象执行结束
    g2.join()  #一个join都不给将不会有运行结果

# 3.3 joinall()
def sing(name):
    for i in range(3):
        gevent.sleep(1)
        print(f'{name}在sing，背诵走的第{i}次')
if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing,'shutong'),
        gevent.spawn(sing,'zihan'),
    ])

# joinall():等待所有的协程都执行结束再退出

# 3.4monkey补丁：拥有在模块运行时替换的功能
# 导入模块
from gevent import monkey
monkey.patch_all()   #将用到的time.sleep()替换成gevent里面自己实现耗时操作的gevent.sleep()代码
# 注意：monkey.patch_all()必须放在被打补丁者的前面
def sing(name):
    for i in range(3):
        time.sleep(1)
        print(f'{name}在sing，背诵走的第{i}次')
if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing,'shutong'),
        gevent.spawn(sing,'zihan'),
    ])

# 4.总结
# 4.1线程是cpu调度的最基本单位，进程是资源分配的基本单位
# 4.2进程、线程和协程对比
#     进程：切换需要的资源最大，效率最低
#     线程：切换需要的资源一般，效率一般
#     协程：切换需要的资源最小，效率高
# 4.3多线程适合IO密集型操作（文件操作、爬虫），多进程适合cpu密集型操作（科学及计算、对视频进行高清解码、计算圆周率等）
# 4.3进程、线程、协程都是可以完成多任务的，可以根据自己实际开发的需要选择使用