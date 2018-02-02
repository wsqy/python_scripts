>`itertools`模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算

[TOC]
# 无限迭代器
## count
>返回一个无限迭代器 可以知道初始值和步长，as:count(2.5, 0.5) -> 2.5 3.0 3.5 ...

demo
```
def count_demo():
    """ count(start=0, step=1) --> count object
    返回以start开头的均匀间隔step步长的值
    """
    for item in itertools.count(1):
        if item > 10:
            break
        print(item)
```
实现类似于
```
def count(firstval=0, step=1):
    x = firstval
    while 1:
        yield x
        x += step
```


## cycle
>把传入的一个序列无限重复下去， as：cycle('ABCD') --> A B C D A B C D A B C D ...

chain_demo
```
def cycle_demo(its=["a", "b", "c", "d"]):
    """
    保存迭代对象的每个元素的副本，无限的重复返回每个元素的副本
    """
    for _index, item in enumerate(itertools.cycle(its)):
        if _index > 10:
            break
        print("{}--{}".format(_index, item))
```
实现类似于
```
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
```

## repeat
> 把传入的一个元素重复n次， as：repeat(10, 3) --> 10 10 10

demo
```
def repeat_demo(its=["a", "b", "c", "d"]):
    """ 负责把一个对象无限重复下去，不过如果提供第二个参数就可以限定重复次数
    repeat(object [,times]) -> create an iterator which returns the object
    for the specified number of times.  If not specified, returns the object
    endlessly.
    """
    for _index, item in enumerate(itertools.repeat(its, 4)):
        print("{}--{}".format(_index, item))
```
实现类似于
```
def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object
```


# 在最短输入序列上终止的迭代器

## accumulate
>accumulate([1,2,3,4,5]) --> 1 3 6 10 15
accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120

demo
```
def accumulate_demo(its=range(1, 10)):
    """累计求和(默认)
    accumulate(iterable[, func]) --> accumulate object
    Return series of accumulated sums (or other binary function results).
    """
    for _index, i in enumerate(itertools.accumulate(its), 1):
        print("{}-->{}".format(_index, i))

    print("\n-----\n"*2)
    import operator
    # 累计求积
    for _index, i in enumerate(itertools.accumulate(its, operator.mul), 1):
        print("{}-->{}".format(_index, i))

    print("\n-----\n"*2)

    # 求次幂
    for _index, i in enumerate(itertools.accumulate(range(2, 5), operator.pow), 2):
        print("{}-->{}".format(_index, i))
```

实现类似于
```
def accumulate(iterable, func=operator.add):
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total
```

## chain
>把一组迭代对象串联起来，形成一个更大的迭代器
chain('ABC', 'DEF') --> A B C D E F

demo
```
def chain_demo():
    """把一组迭代对象串联起来，形成一个更大的迭代器
    chain(*iterables) --> chain object
    """
    for i in itertools.chain('ABCD', '1234', 'QIYUAN'):
        print(i, end='  ')
```
实现类似于
```
def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element
```

## compress
> 按要求过滤可迭代对象   
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F

demo
```
def compress_demo():
    """ 返回数据对象中对应规则为True的元素(跟filter很像)   当data/selectors之一用尽时停止
    在用一个可迭代对象过滤另一个可迭代对象时十分有用
    compress(data, selectors) --> iterator over selected data

    Return data elements corresponding to true selector elements.
    Forms a shorter iterator from selected data elements using the
    selectors to choose the data elements.
    """
    for _index, i in enumerate(itertools.compress(range(100), (True, True, True, False, False, True))):
        print("{}-->{}".format(_index, i))
```
实现类似于
```
def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)
```

## dropwhile
> 从可迭代对象里找到第一个不满足过滤条件的元素,并把它及其后的所有元素都迭代出来  
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

demo
```
def dropwhile_demo():
    """返回迭代器中条件第一次为false之后的所有元素
    dropwhile(predicate, iterable) --> dropwhile object

    Drop items from the iterable while predicate(item) is true.
    Afterwards, return every element until the iterable is exhausted.
    """
    for i in itertools.dropwhile(lambda x: 5 < x < 10, range(1, 20)):
        print(i, end="  ")

    print("\n-----\n"*2)

    for i in itertools.dropwhile(lambda x: 5 < x < 10, range(6, 20)):
        print(i, end="  ")
```
实现类似于
```
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

## takewhile
> 迭代一个可迭代对象,直到遇到不满足条件的元素    
takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4

demo
```
def takewhile_demo():
    """返回元素，直到遇到不满足predicate的元素终止 跟dropwhile相反
    takewhile(predicate, iterable) --> takewhile object
    Return successive entries from an iterable as long as the
    predicate evaluates to true for each entry.
    """
    for i in itertools.takewhile(lambda e: e < 5, range(10)):
        print(i, end='')
```
实现类似于
```
def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```

## filterfalse
>顾名思义 迭代出 不满足过滤条件的元素    
filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8

demo
```
def filterfalse_demo():
    """过滤所有不满足条件的元素(与filter相反)
    filterfalse(function or None, sequence) --> filterfalse object

    Return those items of sequence for which function(item) is false.
    If function is None, return the items that are false.

    """
    for i in itertools.filterfalse(lambda x: x % 2 == 0, range(10)):
        print(i, end="  ")

    print("\n-----\n"*2)

    for i in itertools.filterfalse(None, range(10)):
        print(i)
```
实现类似于
```
def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
```



## groupby
>把迭代器中相邻的重复元素挑出来放在一起,判断是否重复 不一定是需要是一样才算一致，也可以自己指定判断方法     
[k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B   
[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

demo
```
def groupby_demo(its='AaabBbcCAAa'):
    """按照分组函数的值对元素进行相邻分组(默认分组函数为相等)
    groupby(iterable[, keyfunc]) -> create an iterator which returns
    (key, sub-iterator) grouped by each value of key(value).
    """
    for key, group in itertools.groupby(its, lambda c: c.upper()):
        print(key, list(group))
```
实现类似于
```
class groupby:
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    
            # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)
```
## islice
>迭代器实现的切片, 不支持负数操作     
islice('ABCDEFG', 2) --> A B    
islice('ABCDEFG', 2, 4) --> C D    
islice('ABCDEFG', 2, None) --> C D E F G  
islice('ABCDEFG', 0, None, 2) --> A C E G

```
def islice(iterable, *args):
    s = slice(*args)
    it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
    try:
        nexti = next(it)
    except StopIteration:
        return
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)
```

## starmap
> 类似于map函数   
starmap(pow,[(1,2), (3,4), (5,6)]) --> 1, 81, 15625

demo
```
def starmap_demo():
    """ 假设iterable将返回一个元组流，并使用这些元组作为参数给function调用
    starmap(function, sequence) --> starmap object
    Return an iterator whose values are returned from the function evaluated
    with an argument tuple taken from the given sequence.
    """
    import os
    its = [
        ('/bin', 'python', 'lib'),
        ('/bin', 'java'),
        ('/usr', 'bin', 'python3'),
    ]
    for i in itertools.starmap(os.path.join, its):
        print(i)
```
实现类似于
```
def starmap(function, iterable):
    for args in iterable:
        yield function(*args)
```

## tee
> 把一个迭代器分成n个迭代器(不是切割,n个迭代器一致)

demo
```
def tee_demo():
    """ 生成n个iterable, 因为生成器只能迭代一遍，如果有多次使用的需求只能通过此函数创建多个iterable
    tee(iterable, n=2) --> tuple of n independent iterators
    """
    for i in itertools.tee(range(10), 3):
        print(list(i))
```
实现类似于
```
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)
```


## zip_longest
> 类似于 zip,不过这里是以长的迭代结束为结束  
itertools.zip_longest([1,2,3,4], [11,22]) --> (1, 11), (2, 22), (3, None), (4, None)]    
itertools.zip_longest([1,2,3,4], [11,22],fillvalue='?') ---> (1, 11), (2, 22), (3, '?'), (4, '?')
```
class ZipExhausted(Exception):
    pass

def zip_longest(*args, **kwds):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = len(args) - 1
    def sentinel():
        nonlocal counter
        if not counter:
            raise ZipExhausted
        counter -= 1
        yield fillvalue
    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            yield tuple(map(next, iterators))
    except ZipExhausted:
        pass
```


# 组合生成器

## product
>生成笛卡尔积   `product(*iterables, repeat=1) --> product object`
product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)     
product((0,1), repeat=3) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

实现
```
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```

## permutations 排列
> 返回可迭代中的元素的连续r长度排列(全排列)
permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC     
permutations(range(3)) --> 012 021 102 120 201 210

demo
```
def permutations_demo(its='ABCD', repeat=2):
    """袋子里有len(iterable), 摸 r 次 ，不放回  有多少种可能
    permutations(iterable[, r]) --> permutations object

    Return successive r-length permutations of elements in the iterable.
    """
    list1 = itertools.permutations(its, repeat)
    print(list(list1))
```
实现
```
# 代码未看懂
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

## combinations  组合
> 从输入可迭代返回r个元素的长度子序列;但是以字典序打印并且内容相同但顺序不同也被视为一个;一个元素只能出现一次   
combinations('ABCD', 2) --> AB AC AD BC BD CD   
combinations(range(4), 3) --> 012 013 023 123

demo
```
def combinations_demo(its='123456', repeat=2):
    """骰子有6面
    combinations(iterable, r) --> combinations object

    Return successive r-length combinations of elements in the iterable.

    combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
    """
    list1 = itertools.combinations(its, 3)
    print(list(list1))
```
实现
```
# 代码未看懂
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
```

## combinations_with_replacement 组合
> 前两点跟`itertools.combinations`;可以出现自身
combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC

demo
```
def combinations_with_replacement_demo(its='ABCD', repeat=2):
    """袋子里有len(iterable), 摸 r 次 ，摸完放回  有多少种可能
    combinations_with_replacement(iterable, r) --> combinations_with_replacement object

    Return successive r-length combinations of elements in the iterable
    allowing individual elements to have successive repeats.
    combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    """
    list1 = itertools.combinations_with_replacement(its, repeat)
    print(list(list1))
```
实现
```
# 代码未看懂
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
```
