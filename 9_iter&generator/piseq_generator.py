def piseq():
    curr = 0
    denominator = 1
    sign = 1

    while True:
        curr += sign / denominator
        yield 4 * curr
        sign *= -1
        denominator += 2


def firstn(g, n):
    for i in range(n):
        print(next(g))


if __name__ == '__main__':
    firstn(piseq(), 100)
