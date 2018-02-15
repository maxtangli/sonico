def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager_optimize():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(1), avg(2), avg(3))
    avg = make_averager()
    print(avg(1), avg(2), avg(3))

    avg = make_averager_optimize()
    print(avg(1), avg(2), avg(3))
    avg = make_averager_optimize()
    print(avg(1), avg(2), avg(3))
