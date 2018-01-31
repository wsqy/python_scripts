def str_demo_dir():
    print(dir(str))
#     '__add__', '__class__', '__contains__', '__delattr__', '__dir__',
#      '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#      '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
#      '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
#      '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#      '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
#      '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
#      'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
#      'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
#     'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
#     'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace',
#     'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
#     'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'


def str_demo_capitalize():
    """字符串首字母大写 """
    s = 'python is the best'
    str = s.capitalize()
    print(str)


def str_demo_casefold():
    """把字符串中的字母全部改为小写 3.3版本新加
    功能与 lower()类似  但lower 只能对A-Z有效
    casefold 对所有语言都有效
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.casefold()
    print(str)


def str_demo_center():
    """把字符串填充到宽度为width的字符串中间，默认填充字母fillchar为空格
    S.center(width[, fillchar])
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.center(50, '#')
    print(str)


def str_demo_count():
    """ 统计字符串中字符出现的次数，可规定区间
    S.count(sub[, start[, end]])
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.count('h')
    print(str)


def str_demo_encode():
    """以你规定的encoding方式编码字符串，用于网页编码等很多方面
    # S.encode(encoding='utf-8', errors='strict') -> bytes
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.encode(encoding='utf-8', errors='strict')
    print(str)


def str_demo_endswith():
    """ 检查字符串是否是以suffix结尾 可以指定区间
    # S.endswith(suffix[, start[, end]]) -> bool
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.endswith('best')
    print(str)


def str_demo_startswith():
    """检查是否以特定字符串开头
    S.endswith(suffix[, start[, end]]) -> bool
    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.startswith('P')
    print(str)


def str_demo_expandtabs():
    """ 把字符串中的tab符号（\t）转换为空格(默认8空格)
    S.expandtabs(tabsize=8) -> str
    """
    s = 'pYtHo3n I\ts t!hE Best'
    str = s.expandtabs()
    print()


def str_demo_index():
    """返回字串在母串中的第一次出现的位置(可指定区间)
    S.index(sub[, start[, end]]) -> int
    Like S.find() but raise ValueError when the substring is not found
    """
    s = 'pYtHo3n I\ts t!hE Best'
    str = s.index('s')
    print(str)
    str = s.index('A')
    print(str)


def str_demo_rindex():
    """从右边数你要寻找的字符的位置，可定制范围,找不到抛出ValueError
    """
    str = 'python is best one'
    s = str.rfind('o')
    print(s)


def str_demo_find():
    """解决index函数的出现异常的情况，如果不存在返回-1
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.

    """
    s = 'pYtHo3n Is t!hE Best'
    str = s.find('A')
    print(str)


def str_demo_rfind():
    """从右边数你要寻找的字符的位置，可定制范围，找不到返回-1
    # S.rfind(sub[, start[, end]]) -> int
    """
    str = 'python is best one'
    s = str.rfind('o')
    print(s)


def str_demo_format():
    """字符串格式化
    S.format(*args, **kwargs) -> str
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
    """


def str_demo_format_map():
    """
    类似 str.format(*args, **kwargs) ，不同的是 mapping 是一个字典对象。

    S.format_map(mapping) -> str
    Return a formatted version of S, using substitutions from mapping.
    The substitutions are identified by braces ('{' and '}').
    """
    People = {'name': 'john', 'age': 56}
    str = 'My name is {name},i am {age} old'.format_map(People)
    print(str)
    # 'My name is john,i am 56 old'


def str_demo_isalnum():
    """检查是否只包含数字字母 """
    s = '23!A'
    print(s.isalnum())


def str_demo_isalpha():
    """检查是否只包含字母 """
    s = 'wqq'
    print(s.isalpha())


def str_demo_isdigit():
    """ 检查字符串中是否都是数字 """
    s = '123'
    print(s.isdigit())


def str_demo_isdecimal():
    """ 检查是否都是十进制的数字 只存在于unicode对象 """
    s = '0x123A'
    print(len(s))
    print(s)
    print(s.isdecimal())


def str_demo_isidentifier():
    """是否是字母开头
    S.isidentifier() -> bool

    Return True if S is a valid identifier according
    to the language definition.

    Use keyword.iskeyword() to test for reserved identifiers
    such as "def" and "class".
    """
    print("qiyu212".isidentifier())
    print("323qiyu212".isidentifier())


def str_demo_islower():
    """ 判断字符串中的字母全是小写(至少有一个小写字母) """
    str = 'qq!1q qq'
    s = str.islower()
    print(s)


def str_demo_isupper():
    """ 判断字符串中的字母全是大写(至少有一个小写字母) """
    str = 'A !a'
    s = str.isupper()
    print(s)


def str_demo_isnumeric():
    """ 判断字符串中只包含数字 """
    str = 'A !a'
    print(str.isnumeric())


def str_demo_isprintable():
    """ 字符串是否都是可打印字符
    Return True if all characters in S are considered
    printable in repr() or S is empty, False otherwise.
    """
    print("".isprintable())


def str_demo_isspace():
    """ 字符串中的是否全是空格字符 """
    str = '\t\n'
    print(str.isspace())


def str_demo_istitle():
    """ 判断字符串是否标题化（所有的单词都是以大写开始，其余字母均小写），则返回True """
    str = 'Python Is Best '
    print(str.istitle())


def str_demo_title():
    """ 字符串标题化 """
    str = 'Python is Best '
    print(str.title())


def str_demo_join():
    """ 将字符依次插入可迭代对象中
    S.join(iterable) -> str
    """
    s = '-'.join(['p', 'y', 't', 'h', 'o', 'n'])
    print(s)


def str_demo_zfill():
    """ 用0填充到指定长度 """
    str = 'Python IS BEst IS'
    s = str.zfill(20)
    print(s)


def str_demo_ljust():
    """ 将字符串左对齐,fillchar指定填充字符
    # S.ljust(width[, fillchar]) -> str
    """
    str = 'python'
    s = str.ljust(10, '#')
    print(s)


def str_demo_rjust():
    """ 右对齐字符串,fillchar指定填充字符
    # S.ljust(width[, fillchar]) -> str
    """
    str = 'python'
    s = str.rjust(10, '#')
    print(s)


def str_demo_lower():
    """ 将字符串转为小写字符串 """
    str = 'Python IS BEst'
    s = str.lower()
    print(s)


def str_demo_upper():
    """ 将字符串转为大写字符串 """
    str = 'Python IS BEst'
    s = str.upper()
    print(s)


def str_demo_strip():
    """ 删除字符串左右两边的空格，chars可定制删除的字符
    # S.strip([chars]) -> str
    """
    str = '  python is Best   '
    s = str.strip()
    print(s)


def str_demo_lstrip():
    """ 删除字符串左边的空格，chars可定制删除的字符 """
    str = '  python is Best   '
    s = str.lstrip()
    print(s)


def str_demo_rstrip():
    """ 删除字符串右边的空格
    S.strip([chars]) -> str
    """
    str = '  python is Best   '
    s = str.rstrip()
    print(s)


def str_demo_split():
    """ 将字符串分片
    默认以空格分片，可用sep参数定制，
    默认分片整个字符串，可用maxsplit分片次数
    # S.split(sep=None, maxsplit=-1) -> list of strings
    """
    str = 'Python IS BEISst'
    s = str.split()
    print(s)


def str_demo_rsplit():
    """ 没看出来跟 split 有啥区别
    Return a list of the words in S, using sep as the
    delimiter string, starting at the end of the string and
    working to the front.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified, any whitespace string
    is a separator.
    """
    str = 'Python IS BEISst'
    s = str.rsplit()
    print(s)


def str_demo_partition():
    """返回一个三元组，包括你要寻找的字符串，及给定字符串的左右两边
    如果找不到，则返回（ 原字符串，空字符串，空字符串 ）的三元组
    """
    str = 'Python IS BEISst'
    s = str.partition('IS')
    print(s)


def str_demo_rpartition():
    """
    类似于partition，不过从右边先开始查找
    """
    str = 'Python IS BEISst'
    s = str.rpartition('IS')
    print(s)


def str_demo_replace():
    """ 以new替换字符串中的old，count可指定替换的次数，默认全文替换
    # S.replace(old, new[, count]) -> str
    """
    str = 'Python IS BEst IS'
    s = str.replace('IS', 'py')
    print(s)


def str_demo_splitlines():
    """ 将字符串中按换行符分割 keepends=True指定是否保留换行符
    S.splitlines([keepends]) -> list of strings
    """
    str = 'Pyt\nhon\nIS BE\nst IS'
    s = str.splitlines(1)
    print(s)


def str_demo_swapcase():
    """ 字符串中大小写反转 """
    str = 'Python IS BEst IS'
    s = str.swapcase()
    print(s)


def str_demo_maketrans():
    """创建字符的映射

    maketrans(x, y=None, z=None, /)
    Return a translation table usable for str.translate().
    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    如果是一个参数必须是 字典形式
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y.
    如果有第二个参数 那么长度必须和第一个参数一致
    If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.
    如果有第三个参数 则必须是字符串 将以 None 映射
    """
    s_yingshe = str.maketrans({k:'' for k in "abcd"})
    print(s_yingshe)
    return s_yingshe


def str_demo_translate():
    """字符串映射
    根据 maketrans 创建的映射表映射字符串,如果映射表是None 则删除
    S.translate(table) -> str

    Return a copy of the string S, where all characters have been mapped
    through the given translation table, which must be a mapping of
    Unicode ordinals to Unicode ordinals, strings, or None.
    Unmapped characters are left untouched. Characters mapped to None
    are deleted.
    """
    yinshe_s = str_demo_maketrans()
    print("abcdefg".translate(yinshe_s))


if __name__ == "__main__":
    str_demo_translate()
