import time
from os.path import isdir, isfile


def my_sum(*arg):
    if len(arg) == 0:
        return 0.0
    for val in arg:
        if not isinstance(val, int):
            return 0
    return sum(arg)


def my_average(*arg):
    if len(arg) == 0:
        return 0.0
    for val in arg:
        if not isinstance(val, int):
            return 0
    return sum(arg) / len(arg)


def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0.0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec


def sums(*ars):
    return sum(ars)


sums = dec(sums)
print(sums(1, 2, 3, 4, 5))
