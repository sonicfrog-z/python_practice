def numbers(start):
    current = start
    while True:
        yield current
        current += 1


def firstn(g, n):
    for i in range(n):
        print(next(g))


if __name__ == '__main__':
    g = numbers(15)
    firstn(g, 10)  # 15 ... 24
    print('=' * 40)
    g2 = numbers(20)
    firstn(g2, 10)  # 20 ... 29
    print('=' * 40)
    firstn(g, 10)  # 25 ... 34