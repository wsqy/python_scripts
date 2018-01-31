def hellocounter(name):
    count = 0

    def counter():
        nonlocal count
        count += 1
        print('Hello,', name, ',', str(count) + ' access!')
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()
