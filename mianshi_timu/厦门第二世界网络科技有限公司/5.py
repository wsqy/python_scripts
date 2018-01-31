"""
5. 写个函数，找出并返回一个数组中的最大数和最小数
"""
a = [1, 2, 0, -9, 11]
# 利用BIF,复杂度 n^2
max_num = max(a)
min_num = min(a)


# 自己实现 复杂度 n
max_num = min_num = a[0]
for i in a:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(max_num)
print(min_num)
