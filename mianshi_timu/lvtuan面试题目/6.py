a = [1, 2]
b = [3, 4]


def list_sort(list1=None, list2=None):
    """
    鉴于题目中两个demo都是b的最小值大于a的最大值，所以采用list.extend再sort
    如果两个list完全混乱 那么轮流遍历两个list效率最佳
    """
    if not list1:
        list1 = a
    if not list2:
        list2 = b
    res = list1.copy()
    res.extend(list2)
    res.sort()
    len_list = len(res)
    if len_list % 2 == 1:
        return res[len_list // 2]
    else:
        return (res[len_list // 2 - 1] + res[(len_list // 2)]) / 2

if __name__ == '__main__':
    print(list_sort())
