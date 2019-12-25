import time


def trace(fname):
    def file_trace(func):
        def call_func(*args):
            with open(fname, 'a+') as fout:
                fout.write('{}\n'.format(time.strftime('%H:%M:%S')))
                fout.write('call {}: {}\n'.format(func.__name__, args))
                result = func(*args)
                fout.write('{} returns {}.\n'.format(func.__name__, result))
                return result

        return call_func
    return file_trace


@trace('trace.log')
def square(x):
    return x**2


@trace('trace.log')
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c


print(square(10))
print(quadratic(5, 1, 2, 3))
