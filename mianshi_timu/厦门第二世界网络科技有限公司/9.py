"""
9. 有20个犯人站成一圈，编号1~20，
从1开始报数，报到3的人就被枪毙，然后下一个重新报1。
问题是编号11的犯人第几次被枪毙？
"""
# 第几次循环
index = 0
# 生成编号
a = [x for x in range(1, 21)]
# 该删除的编号
del_number = 2
while True:
    index += 1
    print("kill:%s in index:%s" % (a[del_number], index))
    if a[del_number] == 11:
        break
    del a[del_number]
    del_number = (del_number + 2) % len(a)
