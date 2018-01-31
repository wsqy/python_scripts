"""
函数可以作为参数  也可以返回函数对象---函数闭包
"""

def say_hello(func):
    def _inner():
        print("say hello start...")
        func()
        print("sya hello end..")
    return _inner


def main():
    print("this is main")


main = say_hello(main)

main()
