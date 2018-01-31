def dict_demo_dir():
    print(dir(dict))
# ['__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__setattr__', '__setitem__', '__sizeof__', '__str__',
#  '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get',
# 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


def dict_demo_creat():
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    print(dicts)


def dict_demo_fromkeys():
    """以一个可迭代对象为键生成一个值为value的字典
    fromkeys(iterable, value=None, /) method of builtins.type instance
    """
    lists = [1, 'q', 3, 4]
    dicts = dict.fromkeys(lists, "")
    print(dicts)


def dict_demo_get():
    """返回键为k的值，若不存在会返回d(默认为None)
    # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    d = dicts.get('k')  # 键不存在，返回None
    print(d)
    d = dicts.get('k', 'sorry,you find not found!')  # 自定义空键的返回值
    print(d)
    d = dicts['k']  # 键不存在  报错
    print(d)


def dict_demo_items():
    """打印出字典的 键值对
    D.items() -> a set-like object providing a view on D's items
    """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    for k, v in dicts.items():
        print(k, v)


def dict_demo_keys():
    """取出字典中键的组合 """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    d = dicts.keys()
    print(d)


def dict_demo_values():
    """取出字典中值的组合 """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    d = dicts.values()
    print(d)


def dict_demo_pop():
    """弹出键的值
    # D.pop(k[,d]) -> v
    """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    d = dicts.pop('a')  # 键存在则返回值，并删除键值对
    print(d)
    print(dicts)

    d = dicts.pop('py')  # 键不存在，则会报KeyError
    print(d)
    print(dicts)

    d = dicts.pop('py', 'sorry,you find not found')  # 键不存在，则会报KeyError
    print(d)
    print(dicts)


def dict_demo_popitem():
    """ 以2元祖的形式随机返回一个键值对并删除
    """
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    d = dicts.popitem()
    print(d)
    print(dicts)


def dict_demo_setdefault():
    # D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    dicts = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}

    # 如果键在字典中，则相当于D.get()
    d = dicts.setdefault('a')
    print(d)
    print(dicts)

    d = dicts.setdefault('a', 'an')
    print(d)
    print(dicts)

    # 如果键不在字典中，则相当于添加一个键值对
    d = dicts.setdefault('py')
    print(d)
    print(dicts)

    d = dicts.setdefault('python', 'python')
    print(d)
    print(dicts)


def dict_demo_update():
    """ D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
    """
    dictA = {'a': 'any', 'b': 'body', 'c': 'common', 'd': 'date'}
    dictB = {'b': 'body_B'}
    print(dictA.update(dictB))
    print(dictA)


if __name__ == '__main__':
    dict_demo_update()
