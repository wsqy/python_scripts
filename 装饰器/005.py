"""
被装饰的对象带了参数  但是装饰器也想带参数怎么办呢
这是一个打日志的方法  可以传入日志的级别
"""
def logger(*_args, **_kwargs):
    def _inner(func):
        def __inner(*args, **kwargs):
            print("say hello start...")
            print("level is--{}".format(_kwargs.get('level')))
            func(*args, **kwargs)
            print("sya hello end..")
        return __inner
    return _inner


@logger(level='error')
def main(_name):
    print("this is {}".format(_name))

main('qiyuan')
