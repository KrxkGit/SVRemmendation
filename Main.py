# coding=utf-8
"""
主函数
"""


import GlobalVariable

if __name__ == '__main__':
    # 以下代码用于测试
    global_obj = GlobalVariable.global_obj
    print(type(global_obj))
    print(type(global_obj.InitWeight))
    print(global_obj.InitWeight.weight1.shape)
