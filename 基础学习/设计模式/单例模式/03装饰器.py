def singleton(cls, *args, **kw):
    _instances = {}
    def _getinstance():
        if cls not in _instances:
            _instances[cls] = cls(*args, **kw)
        return _instances[cls]
    return _getinstance


@singleton
class TestA:
    a = 3


a = TestA()
b = TestA()
c = TestA()

print('a-->id(a)', a.a, id(a.a))
print('b-->id(b)', b.a, id(b.a))
print('c-->id(c)', c.a, id(c.a))

a.a = 11
b.a = 12
print('a-->id(a)', a.a, id(a.a))
print('b-->id(b)', b.a, id(b.a))
print('c-->id(c)', c.a, id(c.a))

d = TestA()
print('d-->id(d)', d.a, id(d.a))
