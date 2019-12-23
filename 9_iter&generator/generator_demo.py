def count_down(n):
    print('Count down from {}'.format(n))

    while n > 0:
        print('Get next')
        # print(n)
        yield n

        n -= 1

    print('Done')


def count_down2():
    yield 4
    yield 10
    yield 346
    yield 2
    yield 46
    yield 9


if __name__ == '__main__':
    # count_down(10)

    # when call the generator function,
    # a generator object is returned.
    # but the statement is the generator function
    # has not been executed yet.
    # g = count_down(3)
    # print(type(g))
    #
    # curr = next(g)
    # print(curr)
    # curr = next(g)
    # print(curr)
    # curr = next(g)
    # print(curr)
    # curr = next(g)

    for i in count_down(10):
        print(i)

    print('=' * 40)
    for i in count_down2():
        print(i)
