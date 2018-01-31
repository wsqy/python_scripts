class DemoA:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(DemoA, cls).__new__(cls, *args, **kw)
        return cls._instance

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
