# -*- coding:utf-8 -*-
import time
# 二维数组中的查找

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""
class Solution:
    # array 二维列表
    def Find(self, array, target):
        i = 0
        j = len(array[0]) - 1
        max_i = len(array) - 1
        while i <= max_i and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return False
"""


class Solution:
    # array 二维列表
    def Find(self, array, target):
        for a in array:
            if target in a:
                return True
        return False


if __name__ == '__main__':
    a = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15],
         ]
    st = time.time()
    s = Solution()
    print(s.Find(a, 14))
    print(s.Find(a, 7))
    print(time.time()-st)
