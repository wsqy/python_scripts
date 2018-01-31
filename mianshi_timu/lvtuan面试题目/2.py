sent = [1, 2, 3, 2, 1]


def duplication(lists=None):
    if not lists:
        lists = sent
    res = list(set(lists))
    return res


if __name__ == '__main__':
    print(duplication())
