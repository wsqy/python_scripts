# abs()          dict()        help()          min()         setattr()
# all()          dir()         hex()           next()        slice()
# any()          divmod()      id()            object()      sorted()
# ascii()        enumerate()   input()         oct()         staticmethod()
# bin()          eval()        int()           open()        str()
# bool()         exec()        isinstance()    ord()         sum()
# bytearray()    filter()      issubclass()    pow()         super()
# bytes()        float()       iter()          print()       tuple()
# callable()     format()      len()           property()    type()
# chr()          frozenset()   list()          range()       vars()
# classmethod()  getattr()     locals()        repr()        zip()
# compile()      globals()     map()           reversed()    __import__()
# complex()      hasattr()     max()           round()     
# delattr()      hash()        memoryview()    set()     
from ctypes.wintypes import SIZE
from os.path import getsize

# 返回一个数值的绝对值，如果是复数则返回实际大小


def demo_abs():
    #     abs(number) -> number
    a = abs(-6 + 3j)
    print(a)

# 如果一个可迭代的对象中的所有元素都是true(或者迭代器是空的)则返回Tuue


def demo_all():
    #      all(iterable) -> bool
    print(all((1, 2, 3)))
    print(all([]))

# 如果可迭代的对象中的任何一个元素是true则返回True；如果可迭代的对象是空的, 则返回False


def demo_any():
    #     any(iterable) -> bool
    print(any([None, 1]))
    print(any([]))

# 返回一个包含任何可打印形式对象的字符串, 当遇到不可打印的ASCII码时，就会输出\x，\u或\U等字符来表示


def demo_ascii():
    #     ascii(object) -> string
    #
    #     As repr(), return a string containing a printable representation of an
    #     object, but escape the non-ASCII characters in the string returned by
    #     repr() using \x, \u or \U escapes.  This generates a string similar
    #     to that returned by repr() in Python 2.
    print(ascii(12))
    print(ascii('\10'))

# 返回一个整数的2进制形式


def demo_bin():
    #     bin(number) -> string
    print(bin(10))

# 返回一个布尔值,即 True 或 False
# python中的False包括：任何数值类型的零0, 0.0, 0j ; 空的序列和映射, '', (), [], {}.


def demo_bool():
    print(bool(1))
    print(bool([]))


def demo_bytearray():
    pass


def demo_bytes():
    pass


def demo_callable():
    pass

# 返回参数i表示的字符。比如，chr(97)返回字符”a”。参数i的有效范围为0到1,114,111（0x10FFFF），
# 其它范围的值会抛出异常ValueError。与之相反转换的函数是ord()，它是把一个字符串变成数值。


def demo_chr():
    #     chr(i) -> Unicode character
    print(chr(97))


def demo_classmethod():
    pass


def demo_compile():
    pass


def demo_complex():
    pass

# 本函数是用来删除对象的属性，比如在函数setattr()里添加的属性，就可以利用这个函数来删除。
# 参数object是一个对象，参数name是一个字符串，但这个字符串必须是对象的属性。比如delattr(x, ‘test’) 等价于 del x.test。


def demo_delattr():
    pass


def demo_dict():
    pass

# 用来显示当前作用域的属性列表


def demo_dir():
    print(dir())

# Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x.
# 返回商和余数的2元祖


def demo_divmod():
    #     divmod(x, y) -> (div, mod)
    print(divmod(5, 3))


def demo_enumerate():
    pass

#property(fget=None, fset=None, fdel=None, doc=None)
# 感觉就是用一个属性访问属性，但是这个属性的一些方法顺序要严格控制


class A:
    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, vaule):
        self.size = vaule

    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)


def demo_property():
    c = A(14)
    print(c.size)
    print(c.x)
    c.x = 29
    print(c.x)
    del c.x
    print(c.x)


if __name__ == "__main__":
    demo_property()
