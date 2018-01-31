import string


def str_demo_dir():
    """
    'Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__',
    '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
    '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters',
    'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits',
    'octdigits', 'printable', 'punctuation', 'whitespace'
    """
    print(dir(string))


def ascii_letters_demo():
    """ a-z and A-Z  lowercase + uppercase """
    print(string.ascii_letters)


def ascii_lowercase_demo():
    """ 返回a-z """
    print(string.ascii_lowercase)


def ascii_uppercase_demo():
    """ 返回A-Z """
    print(string.ascii_uppercase)


def capwords_demo():
    """ 将sep切割后的字符串首字母大写
    capwords(s [,sep]) -> string

    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.

    等价于:
    ```
    def capwords(s, sep=None):
    lt = []
    for x in s.split(sep):
        lt.append(x.capitalize())
    return (sep or ' ').join(lt)
    ```
    """
    print(string.capwords("qiqyyuan", "qy"))


def digits_demo():
    """  返回 0-9 """
    print(string.digits)


def hexdigits_demo():
    """  返回16进制字符串 0-9 a-f A-F """
    print(string.hexdigits)


def octdigits_demo():
    """  返回8进制字符串 0-7 """
    print(string.octdigits)


def printable_demo():
    """  返回所有的可打印字符  digits + letters + punctuation + whitespace
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c
    """
    print(string.printable)


def punctuation_demo():
    """  返回 标点符号 """
    print(string.punctuation)


def punctuation_demo():
    """  返回 空白字符
    ' \t\n\r\x0b\x0c'
    """
    print(string.punctuation)


if __name__ == "__main__":
    capwords_demo()
