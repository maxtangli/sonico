import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            args = ', '.join(arg_lst)
            # print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate


@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)


@clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock()
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock()
def fibonacci_optimized(n):
    return n if n < 2 else fibonacci_optimized(n - 2) + fibonacci_optimized(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print('*' * 40, 'Calling fibonacci(10)')
    print('fibonacci(10) = ', fibonacci(10))
    print('*' * 40, 'Calling fibonacci_optimized(10)')
    print('fibonacci_optimized(10) = ', fibonacci_optimized(10))
