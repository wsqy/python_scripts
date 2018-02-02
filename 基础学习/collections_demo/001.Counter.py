import collections


class CounterDemo:
    def __init__(self, _iterable='qyqi'):
        self._iterable = _iterable

    def counter_create_demo(self):
        """
        Counter 继承字典类, 可以通过 isinstance查看
        """
        counter_result = collections.Counter(self._iterable)
        print(counter_result)
        print(type(counter_result))
        print(isinstance(counter_result, dict))

    def counter_update_demo(self, now_iterable='abcdab', other_iterable='chci'):
        """
        重写了 字典的update 方法, 相加或者添加
        """
        now_counter_result = collections.Counter(now_iterable)
        print(now_counter_result)
        other_counter_result = collections.Counter(other_iterable)
        print(other_counter_result)
        now_counter_result.update(other_counter_result)
        print(now_counter_result)

    def counter_elements_demo(self):
        """
        迭代 键
        """
        counter_result = collections.Counter(self._iterable)
        for i in counter_result.elements():
            print(i)

    def counter_subtract_demo(self, now_iterable='abcdab', other_iterable='chci'):
        """
        求 now_iterable 与 other_iterable的差
        """
        now_counter_result = collections.Counter(now_iterable)
        print(now_counter_result)
        other_counter_result = collections.Counter(other_iterable)
        print(other_counter_result)
        now_counter_result.subtract(other_counter_result)
        print(now_counter_result)

    def counter_most_common_demo(self, now_iterable="abcdaba"):
        """
        取出出现次数最多的n项(默认n = len())
        返回一个由tuple(key, count)组成的list
        """
        now_counter_result = collections.Counter(now_iterable)
        print(now_counter_result)
        print(now_counter_result.most_common(2))





cd = CounterDemo()
# cd.counter_create_demo()
# cd.counter_update_demo()
# cd.counter_elements_demo()
# cd.counter_subtract_demo()
cd.counter_most_common_demo()
