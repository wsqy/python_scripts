"""共享属性
创建实例时把所有实例的 __dict__ 指向同一个字典,这样它们具有相同的属性和方法.
"""


class DemoA:
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(DemoA, cls).__new__(cls, *args, **kw)
        od.__dict = cls._state
        return ob


class TestA(DemoA):
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
