# coding=utf-8

def Krxk_Clock(fun):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = fun(*args, **kwargs)
        stop_time = time.time()
        print('算法 %s 运行时间：%s ms ' % (fun.__name__, (stop_time - start_time) * 1000))
        return result

    return wrapper
