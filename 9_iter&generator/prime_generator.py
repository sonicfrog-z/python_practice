def numbers_from(start):
    current = start
    while True:
        yield current
        current += 1


def not_div_by(g, factor):
    for i in g:
        if i % factor != 0:
            yield i


def prime_gen(g):
    while True:
        prime = next(g)
        yield prime
        g = not_div_by(g, prime)


def firstn(g, n):
    for i in range(n):
        print(next(g))


if __name__ == '__main__':
    firstn(prime_gen(numbers_from(2)), 100)
