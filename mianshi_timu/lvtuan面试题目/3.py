def move(n=3, a='A', b='B', c='C'):
    if(n == 1):
        print(a, "->", c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)

if __name__ == '__main__':
    move()
