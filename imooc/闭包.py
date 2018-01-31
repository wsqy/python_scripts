# coding:utf-8

passline = 60


def func_100(val):
    if val > passline:
        print("pass")
    else:
        print("failed")


def func_150(val):
    passline = 90
    if val > passline:
        print("pass")
    else:
        print("failed")


def setPassline(pasline):
    def cmp(val):
        if val > passline:
            print("pass")
        else:
            print("failed")
    return cmp


f_100 = setPassline(90)
f_100(100)
print(type(f_100))
