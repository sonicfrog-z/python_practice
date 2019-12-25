import time


class trace:
    def __init__(self, fname):
        self._fname = fname

    def __call__(self, func):
        def call_func(*args):
            with open(self._fname, 'a+') as fout:
                fout.write('{}\n'.format(time.strftime('%H:%M:%S')))
                fout.write('call {}: {}\n'.format(func.__name__, args))
                result = func(*args)
                fout.write('{} returns {}.\n'.format(func.__name__, result))
                return result
        return call_func


@trace('trace.log')
def square(x):
    return x**2


@trace('trace.log')
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c


print(square(10))
print(quadratic(5, 1, 2, 3))
