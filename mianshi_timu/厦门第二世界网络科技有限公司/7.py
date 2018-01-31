"""
7. 输入一个正整数N，求从1数到N的过程中出现的所有1的数量，
例如输入2，则输出（1：1个），输入10，则输出（1：2个），输入11，则输出（1：4个）
"""
import time
def num_1(N):
    count = 0
    for i in range(N+1):
        count += str(i).count('1')
    print(count)


if __name__ == '__main__':
    start_time = time.time()
    num_1(10**21)
    print("speend:" +time.time()-start_time())
