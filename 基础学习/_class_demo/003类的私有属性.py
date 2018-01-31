class TestA():

    def __init__(self):
        self._a = 'value of _a'
        self.__b = 'value of _ _b'


if __name__ == "__main__":
    ins_a = TestA()
    print(ins_a._a)
    print(ins_a._TestA__b)
    print(ins_a.__b)
