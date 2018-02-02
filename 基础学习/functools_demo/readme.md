> functools模块用于高阶函数：作用与或者返回其它函数的函数。一般来说，对于该模块，任何可调用对象都可以视为一个函数

[TOC]

# cmp_to_key
参考 [CSDN](blog.csdn.net)网站中的文章[大星星的专栏](http://blog.csdn.net/asmcvc/article/details/51144428)
```
Help on function cmp_to_key in module functools:

cmp_to_key(mycmp)
    Convert a cmp= function into a key= function

```
> 帮助文档说的很简单 将 比较函数转换为key函数,这就引出三个问题1:什么是比较函数;2:什么是key函数;3:怎么将cmp函数转为key函数;3:为什么要py3要取消cmp函数
1. 什么是比较函数

    py3中取消了cmp函数 而这个函数在py2中是BIF,定义如下:
    ```
    Help on built-in function cmp in module __builtin__:

    cmp(...)
        cmp(x, y) -> integer

        Return negative if x<y, zero if x==y, positive if x>y.

    ```
    > 如果是x小于y则返回一个负数;如果z>y则返回一个正数;如果x==y则返回0

2. 什么是`key函数`
    key函数接受一个参数,返回一个可以用作排序的关键字(有点感觉是hash了)

3. 怎么将`cmp函数`转为`key函数`
    - 因为`python3`不存在`cm`p函数了呀 导致很多函数不支持`cmp`了 比如看`sorted`的帮助文档:
        - py2
            ```
            Help on built-in function sorted in module __builtin__:

            sorted(...)
                sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
            ```
        - py3
            ```
            Help on built-in function sorted in module builtins:

            sorted(iterable, key=None, reverse=False)
                Return a new list containing all items from the iterable in ascending order.

                A custom key function can be supplied to customise the sort order, and the
                reverse flag can be set to request the result in descending order.

            ```
    - 很简单 在py2设计过一个cmp函数了,但是到py3不能用了怎么办?用`functools.cmp_to_key`啊:
        1. 对序列 `a=range(10)`进行排序
        2. 首先定义一个比较函数:比较x+4和y的大小关系
            ```
            >>> cmp_func = lambda x,y: x+4 >y
            >>> cmp_func(3,10)
            False
            >>> cmp_func(3,1)
            True
            >>> cmp_func(3,7)
            False
            >>> cmp_func(3,6)
            True
			```
        3. py2 排序的时候直接用cmp参数
            ```
            >>> sorted(a, cmp=cmp_func)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```
        4. py3没有cmp参数 只有key参数
            ```
            # 当然py2中也是可以采用这种方法的
            >>> sorted(a, key=functools.cmp_to_key(cmp_func))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```
    - 参考[Chi's Blog]()网站中的文章[Python3中排序的cmp函数的替代方法](http://blog.codescv.com/python/2016/02/27/python3-cmp.html?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)


    ## functools.reduce
    > functools.reduce 和BIF reduce的功能很相似
    以下是两种方法的定义
    - functools.reduce
    ```
    Help on built-in function reduce in module _functools:
    reduce(...)
        reduce(function, sequence[, initial]) -> value

        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.

    ```
    - reduce
    ```
    Help on built-in function reduce in module __builtin__:

    reduce(...)
        reduce(function, sequence[, initial]) -> value

        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.

    ```
    可以看到两个方法连定义都一模一样, 但是以上是在python2中的测试结果,在python3中是没有reduce这个BIF的,这就是这两个函数的本质区别: **引入functools.reduce就是为了兼容python3的**,下面就以reduce说明一下功能:
    > 对序列`sequence`连续使用函数`function`;如果给出 初始值`initial`,会首先将initial加到`sequence`的头部;第一次将序列的头两个元素进行`function`计算,以后每次都是使用前一次的计算结果和下一个元素进行计算

    - 无初始值
    ```
    >>> reduce(lambda x,y:x*y, xrange(1,6))
    120
    >>>
    ```
    - 有初始值
    ```
    >>> reduce(lambda x,y:x*y, xrange(1,6), 10)
    1200
    >>>
    ```


    ## functools.total_ordering
> 类装饰器 当你需要自定义一个类的比较方法时,默认你需要定义 等于eq  大于gt 小于lt  大于等于ge 小于等于le  有可能还要定义不等于(ne)  但是如果适用了这个类装饰器 那么只需要定义 eq 和 lt le gt ge中的一个就好了

```
@functools.total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

print(dir(Student))
# ['__doc__', '__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__module__']
```


# partial
>偏函数  最常用的应用场景是固定一个函数的某些参数

如果有大量二进制转换任务,我们可能定义一个in2函数
```
>>> int('10010', base=2)
18
>>> def in2(x, base=2):
...     return int(x, base)
...
>>> in2('1010')
10
```
但是我们也可以直接简单生成
```
>>> in22 = functools.partial(int, base=2)
>>> in22('11001')
25
```
# partialmethod
> 类似于 partial 但是 只有 partialmethod才能作用于方法


# lru_cache
> 缓存函数的运行结果:递归求斐波拉切数列时可以缓存某个结果;缓存网络请求等

```
lru_cache(maxsize=128, typed=False)
maxsize是指定最大缓存数量, typed则代表是否严格判断类型如果设置为False,则参数3.0不能使用参数为3的缓存
```


# update_wrapper
> update_wrapper 类似于 wraps 甚至 `@wraps`内部实际上就是基于update_wrapper来实现的

```
def wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    def decorator(wrapper):
        return update_wrapper(wrapper, wrapped=wrapped...)
    return decorator
```

# wraps
> 装饰器会遗失被装饰函数的__name__和__doc__等属性，可以使用@wraps 来恢复

# singledispatch
> JAVA等语言可以类的重载，可以为同一个方法不同类型参数执行不同的方法, 但Python不支持同名方法有不同的参数类型，python给我们的解决方案是使用 singledispatch 来动态指定相应的方法所接收的参数类型，而不用把参数判断放到方法内部去判断从而降低代码的可读性
