from functools import reduce


def simple(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fun(n):
    l = []

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and simple(i):
            l.append(i)

    if len(l) >= 4:
        pr = reduce(lambda x, y: x * y, l)
        if (pr % sum(l)) == 0:
            return n, pr // sum(l)


for i in range(800000, 802000 + 1):
    if fun(i):
        print(fun(i))