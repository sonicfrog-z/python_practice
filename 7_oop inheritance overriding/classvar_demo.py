class Foo:

    a = 3

    def __init__(self, b):
        self.b = b


if __name__ == '__main__':
    f = Foo(10)
    print(f.b)
    print(f.a)
    print(Foo.a)

    g = Foo(5)
    print(g.b)
    print(g.a)

    Foo.a = 30
    print(f.a)
    print(g.a)

    print('=' * 30)
    f.a = 300
    print(f.a)
    print(g.a)
    print(Foo.a)

    f.a = None
    print(f.a)

    del f.a
    print(f.a)
