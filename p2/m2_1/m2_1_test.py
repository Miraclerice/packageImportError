# -*- coding: utf-8 -*-
# @Author: MiracleRice
# Blog   : miraclerice.com
import os
import sys

import m2_1 as m21
# os.getcwd() 获取当前工作目录


sys.path.append("..")
# import m2_2 as m22
if __name__ == '__main__':
    m21.m2_1()
    print(sys.path)
    print(os.path.abspath(__file__))  # 当前绝对目录
    print(os.path.dirname(__file__))  # 当前脚本目录
    print(os.path)  # ntpath 模块
    print(os.pardir)  # ..
    # 获取上级目录一，因为..需要规范化normpath
    print(os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir)))
    # 获取上级目录二, 强烈推荐
    print('/'.join(os.path.dirname(__file__).split('\\')[:-1]))
    # 此时可以使用sys
    sys.path.append('.'.join(os.path.dirname(__file__).split('\\')[:-1]))
    print(sys.path)
    # import m2_2 as m22
    # import m2_2.oprator as op
    # from m2_2 import oprator as op
    # from m2_2.oprator import Oprator as op
    # add = op("+")
    # minus = op("-")
    # print(minus(1, 2))
    # print(add(1, 2))
    # print(op.Operator("+")(1, 2))
