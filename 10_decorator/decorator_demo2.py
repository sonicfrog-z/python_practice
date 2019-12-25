import time


def trace(func):
    def call_func(*args):
        print('{}'.format(time.strftime('%H:%M:%S')))
        print('call {}: {}'.format(func.__name__, args))
        result = func(*args)
        print('{} returns {}.'.format(func.__name__, result))
        return result

    return call_func


@trace
def square(x):
    return x**2


@trace
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c


print(square(10))
print(quadratic(5, 1, 2, 3))
