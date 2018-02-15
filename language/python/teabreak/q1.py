def range_check(func):
    return lambda m, e, n, c: ((0 <= m < n) and func(m, e, n, c)) or ''


@range_check
def lets_take_tea_break(m, e, n, c):
    return str(m) if pow(m, e) % n == c else ''


if __name__ == '__main__':
    for i in range(1000000):
        if lets_take_tea_break(i, 17, 3569, 915) == str(i):
            print(i)  # 2012 -> 2102(invalid)
            break
