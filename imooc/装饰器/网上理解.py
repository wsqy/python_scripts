def decorator_func(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

""" 装饰器
@decorator_func
def func(name):
    print('my name is', name)

func("qiyuan")
"""

""" 函数传参""""


def func(name):
    print('my name is', name)
xx = decorator_func(func)
xx("qiyuan")
