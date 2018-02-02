> collections 是Python内建的一个集合模块，提供了许多有用的集合类
```
'defaultdict', 'OrderedDict', 'namedtuple', 'UserString',
'Counter', 'ChainMap','deque', 'UserDict', 'UserList',
```
## collections.Counter
> 统计出现的次数
```
>>> collections.Counter('qyqi')
Counter({'q': 2, 'i': 1, 'y': 1})
```

## collections.namedtuple
> 将元祖中的数据命名(就可以按属性访问了)
```
>>> User = collections.namedtuple('User', ['name', 'sex', 'age'])
>>> User.__doc__
'User(name, sex, age)'
>>> user1 = User(name='u1', sex='male', age=21)
>>> user1
User(name='u1', sex='male', age=21)

```

## collections.deque
> 双向队列

## collections.defaultdict
> 带默认参数的字典

## collections.OrderedDict
>有序字典
