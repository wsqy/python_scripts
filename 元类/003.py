class Aha:
    aa = 'aaa3'
    def __getattr__(self, name):
        super().__setattr__(name, name)
        return getattr(self, name)


print(Aha().aa)
