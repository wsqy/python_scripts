# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass


my_singleton = My_Singleton()



# to use
from mysingleton import my_singleton
my_singleton.foo()
