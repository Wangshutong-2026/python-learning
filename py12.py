# 2.4抛出异常 raise
# 步骤：
# 1.创建一个Exception('xxx')对象， xxx---异常提示信息
# 2.raise抛出找个对象(异常对象)
# raise Exception("我抛出一个异常")
# def funa():
#     raise Exception("我抛出一个异常")
#     print("哈哈哈哈")   #执行了raise语法，代码不会继续往下执行
# funa()
from typing import cast


# 需求：密码长度不足，就报异常
# 分析：用户输入密码，判断输入的长度是否大于等于6，如果输入长度不足6位，就报错，即抛出自定义异常，并捕获该异常
def login():
    pwd = input("请输入您的密码")
    if len(pwd) >= 6:
        return "密码输入成功"
    raise Exception("长度不足六位，密码输入失败")
# print(login())
try:
    print(login())
except Exception as e:
    print(e)
# 捕获异常是为了检测到异常代码还能继续往下运行，即程序不会终止

# 3.模块
# 3.1含义：一个py文件就是一个模块，即导入一个模块本质上就是执行一个文件
# 3.2分类
# 3.2.1内置模块
# 如：random、time、os、logging，直接导入即可使用
# 3.2.2第三方模块（第三方库）
# 下载：cmd窗口输入pip install 模块名
# 3.2.3自定义模块
# 即自己在项目中定义的模块
# 注意：命名要循环标识符规定以及变量的命名规范，并且不要与内置模块冲突，否则将导致模块功能无法使用

# 3.3导入模块
# 3.3.1 方法一：import 模块名
# 导入模块：  #注意：可以一个import导入多个模块，但是最好是一个模块单独使用一个import
# import 模块名
# 调用功能：
# 模块名.功能名
# import pytest
# # 调用pytest模块中的name变量
# print(pytest.name)
# # 调用pytest模块中的funa()
# pytest.funa()

# 3.3.2 方式二：from...import...
# 语法：
# 从模块中导入指定部分
# from 模块名 import 功能1, 功能2..
# 调用功能
# from pytest import funa,name #导入函数只需要函数名，不需要加上()
# funa()
# print(name)  #没有导入就会报错
# import后面填写需要导入的功能
# funb()  #报错，没有导入funb

# 3.3.3方法三：from...import *
# 语法：from 模块名 import *
from pytest import funa,funb,name
from pytest1 import funa,funb,name
# from pytest import *   #把模块中的所有内容全部导入
# from pytest1 import *
funa()
funb()
print(name)
# 注意：不建议过多使用from...import...声明，有时候命名冲突会造成一些错误

# 3.3.4 as起别名
# 1.as给模块起别名
# 语法： import 模块名 as 别名
# 给模块起别名
import pytest as pt
# 调用模块中的funa()
pt.funa()
# 打印模块中的name变量
print(pt.name)
# 2.as给功能起别名
# 语法；from 模块名 import 功能 as 别名
from pytest1 import funa as a,funb as b
a()
print(name)
b()
# 注意：导入多个功能，使用,将功能与功能隔开，后面的功能也可以取别名：功能名 as 别名

# 3.4内置全局变量__name__
# 3.4.1 语法：
# if __name__ == "__main__":
# 3.4.2作用
# 用来控制py文件在不同的应用场景执行不同的逻辑
# 3.4.3 __name__
# 1.文件在当前程序执行（即自己执行自己）：__name__ == "__main__"
# 2.文件被当做模块被其他文件导入：__name__ == 模块名
import pytest2
pytest2.test()
#注意：被当做模块导入时，__name__ == "__main__"下面的代码不会被显示出来

# 4.包
# 4.1含义：就是项目结构中的文件夹/目录
# 4.2与普通文件夹区别：包是含有__init__.py的文件夹
# 4.3作用：包就是将有联系的模块放到同一个文件夹，有效避免模块名称冲突问题，让结构更清晰。
# 4.4新建包：右键项目包 -> new ->Python Package

# 4.5import导入包时，首先执行__init__.py文件的代码
# 导包方式一：
import pack01
# 导包方式二：
# from pack01 import register
# register.reg()

# 4.6不建议在init文件中编写过多代码，尽量保证init文件的内容简单
# 4.7__all__:本质上是一个列表，列表里面的元素就代表要导入的模块
# 作用：可以控制要引入的东西
from pack01 import *
register.reg()
login.log()
# 4.8包的本质依然是模块，包又可以包含包