class TestA():
    non = 0

    def __init__(self):
        TestA.non += 1

    @classmethod
    def get_non(cls):
        return cls.non


if __name__ == "__main__":
    print(TestA().get_non())
    print(TestA().get_non())
    print(TestA().get_non())
