# 导入线程模块
import threading
import time
from platform import release


# def sing():
#     print('我在唱歌')
#     time.sleep(2)   #睡眠，以秒为单位
#     print('唱完歌了')
# def dance():
#     print('我在跳舞')
#     time.sleep(2)
#     print('跳完舞了')
# sing()
# dance()

# 2.多线程：同时运行多个线程
# 2.1线程和进程
# 进程：是操作系统进行资源分配的基本单位，每打开一个程序至少会有一个进程
# 线程：是cpu调度的基本单位，每一个进程至少都会有一个线程，这个线程通常就是我们所说的主线程
# 一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程
# 2.2多线程
# Thread线程类参数
# target：执行的任务名
# args：以元组的形式给任务传参
# kwargs：以字典的形式给任务传参
def sing(name):
    print(f'{name}我在唱歌')
    time.sleep(2)   #睡眠，以秒为单位
    print('唱完歌了')
def dance(name2):
    print(f'{name2}我在跳舞')
    time.sleep(2)
    print('跳完舞了')
# 主程序入口
if __name__ == '__main__':
    # 1.创建子线程
    t1 = threading.Thread(target=sing,args=('shutong',))   #注意不要在函数名后面加()
    # print(t1)
    t2 = threading.Thread(target=dance,args=('shutong',))  #以元组形式传参，只有一个元素，一定要加,
    # 3.守护线程，必须放在start()前面：主线程执行结束，子线程也会跟着结束
    t1.daemon = True
    t2.daemon = True
    # 2.开启子线程
    t1.start()
    t2.start()
    # 4.阻塞主线程join():暂停的作用，等子线程执行结束后，主线程才会继续执行，必须放在start()后面
    t1.join()
    t2.join()
    # 5.获取线程名字
    print(t1.name)
    print(t2.name)
    # 6.更改线程名
    t1.name = '子线程一'
    t2.name = '子线程二'
    print(t1.name)
    print(t2.name)
    print('完美谢幕，本次表演结束')

# 2.3线程之间执行是无序的
# 线程执行是根据cpu调度决定的
def task():
    time.sleep(1)
    print('当前线程是：',threading.current_thread().name)   #显示当前线程对象名
if __name__ == '__main__':
    for i in range(5):
        # 每循环一次就创建一个子线程
        t = threading.Thread(target=task)
        # 启动子线程
        t.start()

# 2.4线程之间共享资源
# from threading import Thread   如果用导入方式就简单了
#只需要这样写wd = Thread(target=wdata)
li = []  #定义全局变量
# 写入数据
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print('写入的数据是：',li)
# 读取数据
def rdata():
    print('读取的数据是：',li)
if __name__ == '__main__':
    # 创建子线程：
    wd = threading.Thread(target=wdata)
    rd = threading.Thread(target=rdata)
    # 开启子线程：
    wd.start()
    wd.join()
    rd.start()
    rd.join()

# 2.5资源竞争
# a = 0
# b = 1000000   #数额不够大的话，程序就能够计算
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print('第一次累加：',a)
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print('第二次累加：',a)
# # add()
# # add2()
# if __name__ == '__main__':
#     a1 = threading.Thread(target=add)
#     a2 = threading.Thread(target=add2)
#     a1.start()
#     a2.start()

# 3.线程同步
# 两种方式：join 和 互斥锁
# 主线程和创建的子线程之间各自执行完自己的代码直至结束
a = 0
b = 1000000   #数额不够大的话，程序就能够计算
def add():
    for i in range(b):
        global a
        a += 1
    print('第一次累加：',a)   #第一次累加： 1000000
def add2():
    for i in range(b):
        global a
        a += 1
    print('第二次累加：',a)   #第二次累加： 2000000
# add()
# add2()
if __name__ == '__main__':
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()
    a1.join()   #等待a1子线程执行结束以后，代码再继续往下进行，开始执行a2子线程
    a2.start()
    a2.join()

# 4.互斥锁
# 对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题：保证同一时刻只能有一个线程去操作
# acquire() 加锁
# release() 解锁
# 两种方法必须承兑出现，否则容易形成死锁
# 死锁：一直等待对方释放锁的情景就是死锁
#      会造成应用程序停止响应，不能再处理其他业务
# 导入模块
from threading import Lock
# 1.创建全局互斥锁
lock = Lock()
a = 0
b = 1000000   #数额不够大的话，程序就能够计算
def add():
    # 2.上锁
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print('第一次累加：',a)
    # 3.释放锁
    lock.release()
def add2():
    # 2.上锁
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print('第二次累加：',a)
    # 3.释放锁
    lock.release()
# add()
# add2()
if __name__ == '__main__':
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()
    # a1.join()   #等待a1子线程执行结束以后，代码再继续往下进行，开始执行a2子线程
    a2.start()
    # a2.join()
# 注意：互斥锁是多个线程一起去抢，抢到锁的线程先执行

# 4.2总结
# 1.互斥锁的作用：保证同一个时刻只有一个线程去操作共享数据，保证共享数据不会出现错误问题
# 2.上锁和释放锁必须成对出现，否则容易造成死锁现象
#   死锁：一直等待对方释放锁的情景就是死锁
#        会造成应用程序停止响应，不能再处理其他业务
# 3.互斥锁的缺点：会影响代码的执行效率