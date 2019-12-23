def numbers_from(start):
    current = start
    while True:
        yield current
        current += 1


def even_numbers(g):
    for i in g:
        if i % 2 == 0:
            yield i


def firstn(g, n):
    for i in range(n):
        print(next(g))


if __name__ == '__main__':
    firstn(even_numbers(numbers_from(15)), 10)
