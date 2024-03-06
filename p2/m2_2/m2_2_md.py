# -*- coding: utf-8 -*-
# @Author: MiracleRice
# Blog   : miraclerice.com

def m2_2():
    print("m2_2")


if __name__ == '__main__':
    import os
    import sys
    # sys.path.append('.'.join(os.path.dirname(__file__).split('\\')[:-1]))
    # print(sys.path)
    # import m2_2
    # import oprator as op
    #
    # print(op.Oprator("+")(1, 2))

    sys.path.append('/'.join(os.path.dirname(__file__).split('\\')[:-2]))
    print(sys.path)
    from p3 import *
    m3.m3()