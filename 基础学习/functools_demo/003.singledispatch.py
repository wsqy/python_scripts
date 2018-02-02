from functools import singledispatch


class TestClass(object):
    @singledispatch
    def test_method(arg, verbose=False):
        if verbose:
            print("Let me just say,", end=" ")
        print(arg)

    @test_method.register(int)
    def _(arg):
        print("Strength in numbers, eh?", end=" ")
        print(arg)

    @test_method.register(list)
    def _(arg):
        print("Enumerate this:")

        for i, elem in enumerate(arg):
            print(i, elem)


"""
>>> TestClass.test_method(55555)  # call @test_method.register(int)
Strength in numbers, eh? 55555

>>> TestClass.test_method([33, 22, 11])   # call @test_method.register(list)
Enumerate this:
0 33
1 22
2 11

>>> TestClass.test_method('hello world', verbose=True)  # call default
Let me just say, hello world
"""
