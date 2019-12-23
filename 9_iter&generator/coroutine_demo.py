def consumer():
    n = 1
    while True:
        n += 1
        number = yield n
        print(number)


if __name__ == '__main__':
    c = consumer()
    v = next(c)
    print(v)
    v = c.send(10)
    print(v)
    v = c.send(7)
    print(v)
    next(c)
    c.close()

