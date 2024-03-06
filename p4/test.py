# -*- coding: utf-8 -*-
# @Author: MiracleRice
# Blog   : miraclerice.com
import os
import sys

if __name__ == '__main__':
    # 如果`sys.path`没有p3所在的目录，需要添加，否则会报错
    # sys.path.append('\\'.join(os.path.dirname(__file__).split('\\')[:-1]))
    # print(sys.path)
    from p3 import *
    m3.m3()