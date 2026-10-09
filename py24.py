from logging import Manager
from multiprocessing import Process,Queue,Pool,Manager
import time
import os
# from queue import Queue
# 1.1含义
# 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
# 一个正在运行的程序或者软件就是一个进程
# 程序跑起来就成了进程
# 注意：进程里面可以创建多个线程，多进程也可以完成多任务
# 1.2进程的状态
# 1.就绪状态：运行的条件都已经满足，正在等待cpu执行
# 2.执行状态：cpu正在执行其功能
# 3.等待（阻塞）状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态

# print('我是shutong')  #程序开始，处于执行状态
# sex = input('输入性别：')  #光标闪动，等待用户输入，处于等待状态
# print(sex)  #执行状态
# time.sleep(1)   #延时1秒，等待（阻塞）状态

# 2.进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# 2.1 Process 类参数
# 1.target：执行的目标任务名，即子进程要执行的任务
# 2.args：以元组的形式传参
# 3.kwargs：以字典的形式传参
# 2.2常用的方法
# 1.start()：开启子进程
# 2.is_alive()：判断子进程是否还活着，存活返回True，死亡返回False
# 3.join()：主进程等待子进程执行结束
# 2.3常用的属性
# name：当前进程的别名，默认Process-N
# pid：当前进程的进程编号
def sing():
    #os.getpid():获取当前进程编号
    #os.getppid():获取当前父进程编号
    print(f'sing子进程编号：{os.getpid()}，父进程id：{os.getppid()}')  #父进程的pid就是py文件主进程的id
    print('唱歌')
def dance():
    print(f'dance子进程编号：{os.getpid()}，父进程id：{os.getppid()}')
    print('跳舞')
if __name__ == '__main__':
    #创建子进程
    #修改子进程名的第一种方式
    p1 = Process(target=sing,name='子进程一')
    p2 = Process(target=dance,name='子进程二')
    #开启
    p1.start()
    p2.start()
    #修改子进程名的第一种方式
    p1.name = '子进程1'
    p2.name = '子进程2'
    #访问name属性
    print('p1:',p1.name)
    print('p2:',p2.name)
    #查看子进程的进程编号
    print('p1.pid:',p1.pid)
    print('p2.pid:',p2.pid)
    print(f"主进程的pid：{os.getpid()},,主进程的父进程pid：{os.getppid()}")
    #cmd命令提示符窗口输入tasklist可以查看电脑里面进程的命令
    # Ctrl+F 查找
    # pycharm64软件进程编号就是主进程的父进程编号
def eat(name):
    print(f"{name}在干饭")
def sleep(name):
    print(f"{name}在睡觉")
if __name__ == '__main__':
    p1 = Process(target=eat,args=('shutong',))
    p2 = Process(target=sleep,args=('zihan',))
    p1.start()
    p1.join()  #主进程处于等待的状态，p1是运行状态
    p2.start()
    print("p1存活状态：",p1.is_alive())
    print("p2存活状态：",p2.is_alive())
#写在主进程中判断存活状态的时候需要加入join阻塞一下

# 2.4进程间不共享全局变量
# li = []  #定义全局变量
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.2)
#     print('写入的数据是：',li)
# # 读取数据
# def rdata():
#     print('读取的数据是：',li)
# # 1.防止别人导入文件的时候执行main里面的方法
# # 2.防止windows系统递归创建子进程
# if __name__ == '__main__':
#     p1 = Process(target=wdata)
#     p2 = Process(target=rdata)
#     p1.start()
#     p1.join()
#     p2.start()

# 读取一直为空，进程不共享全局变量

# 3.进程间的通信
# Queue（队列）
# q.put(): 放入数据
# q.get(): 取出数据
# q.empty(): 判断队列是否为空
# q.qsize(): 返回当前队列包含的消息数量
# q.full(): 判断队列是否满了
# # 初始化一个队列队形
# q = Queue(3)  #最多可以接受三条消息，没写或者是负值就代表没有上限，直到内存的尽头
# q.put('haha')
# q.put('xixi')
# print("是否满了",q.full())
# q.put('hehe')
# # print(q.qsize())
# print(q.get())  #获取队列的一条消息，然后将其从队列中移除
# print(q.get())
# print(q.qsize())
# q.put('heihei')
# # print(q.empty())
# print(q.get())
# print(q.get())
# # print(q.empty())
# # print(q.qsize())

li = ['张三','李四','王五','赵六']  #定义全局变量
# 写入数据
def wdata(q1):
    for i in li:
        print(f"{i}已经被放入")
        q1.put(i)
        time.sleep(0.2)
    print('写入的数据是：',li)
# 读取数据
def rdata(q2):
    res = []
    while True:
        #判断是否为空，队列为空就退出循环
        if q2.empty():
            break
        else:
            data = q2.get()
            res.append(data)
            print('取出数据：',data)
    print('读取的数据是：',res)
# 1.防止别人导入文件的时候执行main里面的方法
# 2.防止windows系统递归创建子进程
if __name__ == '__main__':
    # 1.创建队列对象
    q = Queue()
    p1 = Process(target=wdata ,args=(q,))
    p2 = Process(target=rdata ,args=(q,))
    p1.start()
    p1.join()  #等待队列中的数据放入完成
    p2.start()

# 进程池
# 主要的方法
# p.apply_async(func[,args[,kwds]])   非阻塞方式调用func   并行执行
# func 函数名
# args为传递给func的参数列表---元组形式
# kwds为传递给func的关键字参数列表
#
# p.close() 关闭进程池，防止进一步操作（进程池不接受新的任务）
# p.join() 阻塞
# enumerate()不管任务是否完成，立即终止
# 如果使用异步提交任务，等进程池内任务都处理完，需要用get()来收集结果
#
# 使用场景：
# 利用python进行系统管理的时候，同时操作多个文件目录，或者远程控制多台主机，
# 并且操作可以节约大量的时间

# 同步和异步
# 阻塞：遇到I/O就发生阻塞，程序一旦遇到阻塞操作就停在原地，并且立刻释放的cpu资源
# 非阻塞：没有I/O操作或者通过某种手段让程序即便遇到IO操作，也不会停在原地，而去执行其他操作
# ，力求尽可能多的占有cpu资源
#
# 同步与异步指的是提交任务的两种方式：
# 同步调用：提交完任务后，就在原地等待，直到任务运行完毕后，拿到任务的返回值，才继续执行下一行代码
# 异步调用：提交完任务后，不在原地等待，直接执行下一行代码
#
# 同步：我等你（当你告诉（拿到任务的返回值）我已经执行完，那我再往下执行）
# 异步：只管提交任务执行，系统会通知任务是否执行完毕

# 进程池异步和同步操作

# 异步：不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
def learn(n):
    print('我们在学习python')
    time.sleep(2)
    return n**2
if __name__ == '__main__':
    # 创建进程池，最大进程数为3
    p = Pool(3)
    list1 = []
    for i in range(6):
        #apply_async异步
        result = p.apply_async(learn,args=(i,))   #learn函数名，i为函数learn的参数
        #把结果添加到list1列表里
        list1.append(result)
    # 关闭进程池，关闭后p不再接受新的请求
    p.close()
    # 等待p中所有子进程执行完成，必须放在close语句之后
    p.join()
    for j in list1:
        #使用get来获取apply_async的结果
        print(j.get())

# 同步：apply 同步阻塞，等待当前子进程执行完毕后，再执行下一个进程（按顺序执行）
def learn(n):
    print('我们在学习python')
    time.sleep(2)
    return n**2
if __name__ == '__main__':
    # 创建进程池，最大进程数为3
    p = Pool(3)
    list1 = []
    for i in range(6):
        result = p.apply(learn,args=(i,))
        list1.append(result)
    print(list1)

# 进程池的通信
# Pool创建进程池，需要使用multiprocessing.Manager()中Queue()
# 进程间的通信：multiprocessing.Queue()
# Manager()模块，专门做数据共享，支持类型很多，如value，array，list，dict，Queue，Lock等
#
# multiprocessing 模块下的 Queue 为进程提供服务：、
# queue模块下的Queue为线程提供服务

# 队列实例化 q = Manager().Queue()

def rd(q):
    print(f'rd启动{os.getpid()},父进程{os.getppid()}')
    for i in range(q.qsize()):  #q.qsize()返回队列中数据的数量
        print('取出数据：',q.get())

def wd(q):
    print(f'wd启动{os.getpid()},父进程{os.getppid()}')
    for i in '123':
        print('wd中的：',i)
        q.put(i)  #把字符串123中的某个数据放入队列中

if __name__ == '__main__':
    print('开始了',os.getpid())
    # 实例化一个队列对象
    q = Manager().Queue()
    # 创建进程池
    p = Pool()
    # 异步
    p.apply_async(wd, args=(q,))
    p.apply_async(rd, args=(q,))
    p.close()  #关闭进程池
    p.join()  #阻塞进程池
    print('结束了',os.getpid())