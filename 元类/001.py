def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      返回一个将属性列表变为大写字母的类对象
    """

    # 选取所有不以'__'开头的属性,并把它们编程大写
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name] = val
            uppercase_attr[name.upper()] = val.upper()
        else:
            uppercase_attr[name] = val

    # 用'type'创建类
    return type(future_class_name, future_class_parents, uppercase_attr)


class MyList(list, metaclass=upper_attr):
    bbb = 'bbb'

# print(MyList.bbb)
# print(MyList.BBB)
