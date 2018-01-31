"""
1. 求从10到100中能被3或5整除的数的和。
"""
answer = [i for i in range(10, 101) if i % 3 == 0 or i % 5 == 0]
print(sum(answer))

# 或者
answer = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(10, 101)))
print(answer)
