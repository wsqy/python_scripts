def lru_cache(expire=5):
    # 默认5s超时
    def func_wrapper(func):
        def inner(*args, **kwargs):
            # cache 处理 bala bala bala
            return func(*args, **kwargs)
        return inner
    return func_wrapper


@lru_cache(expire=10 * 60)
def get(request, pk):
    # 省略具体代码
    return response()

get()
