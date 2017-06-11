def range_check(func):
    # return lambda m, e, n, c: ((0 <= m and m < n) and func(m, e, n, c)) or ''
    return lambda m, e, n, c: ((0 <= m < n) and func(m, e, n, c)) or ''


@range_check
def f(m, e, n, c):
    return str(m) if pow(m, e) % n == c else ''


if __name__ == '__main__':
    for i in range(1000000):
        if f(i, 17, 3569, 915) == str(i):
            print(i)
