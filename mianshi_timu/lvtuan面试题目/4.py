def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]


def out_triangles(NUM=10):
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == NUM:
            break

if __name__ == '__main__':
    out_triangles()
