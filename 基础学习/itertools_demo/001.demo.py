import itertools

def count_demo():
    """ count(start=0, step=1) --> count object
    返回以start开头的均匀间隔step步长的值
    """
    for item in itertools.count(1):
        if item > 10:
            break
        print(item)


def cycle_demo(its=["a", "b", "c", "d"]):
    """
    保存迭代对象的每个元素的副本，无限的重复返回每个元素的副本
    """
    for _index, item in enumerate(itertools.cycle(its)):
        if _index > 10:
            break
        print("{}--{}".format(_index, item))


def repeat_demo(its=["a", "b", "c", "d"]):
    """ 负责把一个对象无限重复下去，不过如果提供第二个参数就可以限定重复次数
    repeat(object [,times]) -> create an iterator which returns the object
    for the specified number of times.  If not specified, returns the object
    endlessly.
    """
    for _index, item in enumerate(itertools.repeat(its, 4)):
        print("{}--{}".format(_index, item))


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


def chain_demo():
    """把一组迭代对象串联起来，形成一个更大的迭代器
    chain(*iterables) --> chain object
    """
    for i in itertools.chain('ABCD', '1234', 'QIYUAN'):
        print(i, end='  ')


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


def takewhile_demo():
    """返回元素，直到遇到不满足predicate的元素终止 跟dropwhile相反
    takewhile(predicate, iterable) --> takewhile object
    Return successive entries from an iterable as long as the
    predicate evaluates to true for each entry.
    """
    for i in itertools.takewhile(lambda e: e < 5, range(10)):
        print(i, end='')


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


def groupby_demo(its='AaabBbcCAAa'):
    """按照分组函数的值对元素进行相邻分组(默认分组函数为相等)
    groupby(iterable[, keyfunc]) -> create an iterator which returns
    (key, sub-iterator) grouped by each value of key(value).
    """
    for key, group in itertools.groupby(its, lambda c: c.upper()):
        print(key, list(group))


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


def tee_demo():
    """ 生成n个iterable, 因为生成器只能迭代一遍，如果有多次使用的需求只能通过此函数创建多个iterable
    tee(iterable, n=2) --> tuple of n independent iterators
    """
    for i in itertools.tee(range(10), 3):
        print(list(i))


def product_demo():
    """生成笛卡尔积   repeat代表 参数复制多少份
    product(*iterables, repeat=1) --> product object

    Cartesian product of input iterables.  Equivalent to nested for-loops.

    For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).

    The leftmost iterators are in the outermost for-loop, so the output tuples
    cycle in a manner similar to an odometer (with the rightmost element changing
    on every iteration).

    To compute the product of an iterable with itself, specify the number
    of repetitions with the optional repeat keyword argument. For example,
    product(A, repeat=4) means the same as product(A, A, A, A).

    product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
    product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...
    """
    print(list(itertools.product('ab', 'ijk')))
    print(list(itertools.product('ab', 'ijk', repeat=2)))


def permutations_demo(its='ABCD', repeat=2):
    """袋子里有len(iterable), 摸 r 次 ，不放回  有多少种可能
    permutations(iterable[, r]) --> permutations object

    Return successive r-length permutations of elements in the iterable.
    """
    list1 = itertools.permutations(its, repeat)
    print(list(list1))


def combinations_demo(its='123456', repeat=2):
    """骰子有6面
    combinations(iterable, r) --> combinations object

    Return successive r-length combinations of elements in the iterable.

    combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
    """
    list1 = itertools.combinations(its, 3)
    print(list(list1))


def combinations_with_replacement_demo(its='ABCD', repeat=2):
    """袋子里有len(iterable), 摸 r 次 ，摸完放回  有多少种可能
    combinations_with_replacement(iterable, r) --> combinations_with_replacement object

    Return successive r-length combinations of elements in the iterable
    allowing individual elements to have successive repeats.
    combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    """
    list1 = itertools.combinations_with_replacement(its, repeat)
    print(list(list1))


if __name__ == '__main__':
    permutations_demo()
