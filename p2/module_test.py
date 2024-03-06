# -*- coding: utf-8 -*-
# @Author: MiracleRice
# Blog   : miraclerice.com
import sys

# 正常，不会报错, p2存在子包m2_1
import p2.m2_2.oprator as op
# 报错，m2_2不存在子包m2_1
# import m2_2.oprator as op

# import p4.m4_1.m4_1_1.m4_1_1 as m4
# m4.m4_1_1()
# 报错，`sys.path`不存在m4_1所在目录
# import m4_1.m4_1_1.m4_1_1 as m4

# from p2.m2_2 import oprator as op
# print(op.Oprator("+")(1, 2))
# print(sys.path)

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

# 以下打印的`__name__`属性和`__package__`会因导包方式而改变，即类似java的全类名
from m2_1 import m2_1                # m2_1.m2_1      m2_1
# from p2.m2_1 import m2_1           # p2.m2_1.m2_1   p2.m2_1
# import p2.m2_1.m2_1                # p2.m2_1.m2_1   p2.m2_1
# __file__=E:\code\python_code\packagImport\p2\module_test.py | __name__=__main__             | __package__=None
# __file__=E:\code\python_code\packagImport\p2\m2_1\m2_1.py   | __name__=m2_1.m2_1            | __package__=m2_1