from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper():
        """wrapper_doc"""
        print('Calling decorated function')
        return f()
    return wrapper


@my_decorator
def example():
    """example_doc"""
    print('Called example function')


"""
>>> example.__name__
'example'
>>> example.__doc__
'example_doc'

# 尝试去掉@wraps(f)来看一下运行结果，example自身的__name__和__doc__都已经丧失了
>>> example.__name__
'wrapper'
>>> example.__doc__
'wrapper_doc'

"""
