"""
函数闭包怎么传递参数
"""

def say_hello(func):
    def _inner(*args, **kwargs):
        print("say hello start...")
        func(*args, **kwargs)
        print("sya hello end..")
    return _inner


def main(_name):
    print("this is {}".format(_name))


main = say_hello(main)

main('qiyuan')
