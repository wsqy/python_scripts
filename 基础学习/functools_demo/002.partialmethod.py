from functools import partial, partialmethod


def standalone(self, a=1, b=2):
    "Standalone function"
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


class MyClass:
    "Demonstration class for functools"
    def __init__(self):
        self.attr = 'instance attribute'
    method1 = functools.partialmethod(standalone)  # 使用partialmethod
    method2 = functools.partial(standalone)  # 使用partial

"""
>>> o = MyClass()

>>> o.method1()
  called standalone with: (<__main__.MyClass object at 0x7f46d40cc550>, 1, 2)
  self.attr = instance attribute

# 不能使用partial
>>> o.method2()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: standalone() missing 1 required positional argument: 'self'

"""
