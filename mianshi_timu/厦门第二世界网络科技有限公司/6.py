"""
6. 求斐波那契数列第n项，斐波那契数列前10项为 1,1,2,3,5,8,13,21,34,55,... 。
"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return

if __name__ == '__main__':
    for i in fib(10):
        print(i)
