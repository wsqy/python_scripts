"""
上一个写法中的 sya_hello已经是一个装饰器了：它对原函数做了包装并返回了另外一个函数，额外添加了一些功能
实际上python2.4之前也都是这么写的  但是2.4新加了一个语法糖@
"""

def say_hello(func):
    def _inner(*args, **kwargs):
        print("say hello start...")
        func(*args, **kwargs)
        print("sya hello end..")
    return _inner

@say_hello
def main(_name):
    print("this is {}".format(_name))

main('qiyuan')
