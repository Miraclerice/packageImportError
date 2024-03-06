# -*- coding: utf-8 -*-
# @Author: MiracleRice
# Blog   : miraclerice.com
import sys


# import p2.m2_2. m2_2_md
# 以下相对导入为该模块的`__name__`属性为当前脚本名字时不报错，当直接运行，即为`__name__`属性为`__main__`时报错
# from . import m2_2_md
# from .m2_2_md import m2_2
# from ..m2_2.m2_2_md import m2_2
# import m2_2_md
# import p2.m2_2.m2_2_md
# import m2_2.m2_2_md
"""
   具体看调用该模块形式
   如果为 import p2.m2_2.oprator as op
       module_test.py 调用该模块使用以下导包， 该模块的顶级包(top-level package)为m2_2， 而m2_2包下并没有子包m2_1  
   如果为 import m2_2.oprator as op
       p2包下存在子包m2_1
   因此报错： ValueError: attempted relative import beyond top-level package
"""
# from ..m2_1 import m2_1_test

class Oprator(object):
    def __init__(self, op_sign):
        super().__init__()
        self.op_sign = op_sign

    def __call__(self, *args, **kwargs):
        if self.op_sign == "+":
            return args[0] + args[1]
        elif self.op_sign == "-":
            return args[0] - args[1]
        elif self.op_sign == "*":
            return args[0] * args[1]
        elif self.op_sign == "/":
            return args[0] / args[1]
        else:
            print("op_sign error")


# def main():
#     # SyntaxError: import * only allowed at module level 方法内部不能import所有
#     from m2_2_md import *
#     pass
#
#
# main()

if __name__ == '__main__':
    # 以下导包会抛出异常ImportError: attempted relative import with no known parent package，因为使用相对导入的模块不能作为顶级执行文件，此时`__package__`属性为None
    # from .m2_2_md import *
    # from . import m2_2_md
    print(sys.path)
    pass

