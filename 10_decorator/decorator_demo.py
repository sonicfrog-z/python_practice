def bar(func):
    print('bar')
    return func


@bar
def foo():
    print('foo')


# foo = bar(foo)
foo()
