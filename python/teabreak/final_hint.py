def f2(*data):
    import itertools
    cy = itertools.cycle(data)
    _int = int
    return lambda i: _int(i) if isinstance(i, str) else next(cy)


int = f2(1985, 33067, 84)


def range_check(func):
    return lambda m, e, n, c: ((0 <= m < n) and func(m, e, n, c)) or ''


@range_check
def f(m, e, n, c):
    return str(m) if pow(m, e) % n == c else ''


if __name__ == '__main__':
    # for i in range(1000000):
    #     # if f(i, 17, 3569, 915) == str(i):
    #     if f(i, 1985, 33067, 84) == str(i):
    #         print(i)  # 25202
    #
    # print(25202 % 1985, 25202 % 33067, 25202 % 84) # invalid
    # print(25202 % 17, 25202 % 3569, 25202 % 915) # invalid

    for i in range(1000000):
        if f(i, int(17), int(3569), int(915)) == str(i):
            print(i)  # 25202
