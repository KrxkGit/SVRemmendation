# coding=utf-8
"""
主函数
"""


import GlobalVariable

if __name__ == '__main__':
    # 以下代码用于测试
    my_global = GlobalVariable.GlobalVariable()
    print(type(my_global))
    print(type(my_global.InitWeight))
    print(my_global.InitWeight.weight1.shape)
