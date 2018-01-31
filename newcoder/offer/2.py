# -*- coding:utf-8 -*-
"""
替换空格
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的
字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(" ", "%20")

if __name__ == "__main__":
    s = Solution()
    str = "We Are Happy"
    a = s.replaceSpace(str)
    print(a)
