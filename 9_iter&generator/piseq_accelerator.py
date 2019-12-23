def piseq():
    curr = 0
    denominator = 1
    sign = 1

    while True:
        curr += sign / denominator
        yield 4 * curr
        sign *= -1
        denominator += 2


def accelator(g):
    s1 = next(g)
    s2 = next(g)
    s3 = next(g)

    while True:
        result = s3 - (s3-s2)**2 / (s3 - 2*s2 + s1)
        yield result
        s1, s2, s3 = s2, s3, next(g)


def firstn(g, n):
    for i in range(n):
        print(next(g))


if __name__ == '__main__':
    firstn(accelator(piseq()), 1000)
