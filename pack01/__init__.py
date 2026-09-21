# print("这是__init__.py")
# 不建议在init文件中写大量代码
# 主要作用：导入这个包内的其他模块
# from pack01 import register
# register.reg()
__all__ = ['register','login']  #相当于导入[]里面定义的模块