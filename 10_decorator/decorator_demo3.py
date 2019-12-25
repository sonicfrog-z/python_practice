def memoized(func):
    cache = {}

    def call_func(*args):
        try:
            c = cache.get(args)
            if c:
                return c
            else:
                r = func(*args)
                cache[args] = r
                return r
        except:
            return func(*args)

    return call_func


@memoized
def fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(200))
