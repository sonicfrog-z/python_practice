def calculate(a, b, c):
    return a + b**2 + c**3


print(calculate(10, 5, 6))
print(calculate(5, 6, 10))
print(calculate(b=5, c=6, a=10))


def mystery(**kwargs):
    print(kwargs)


mystery(a=3, b=4, c=5)
mystery(a=10, b=20)
mystery(x=1, y=2, z=3)


def magic(a, *foo, **bar):
    print(a)
    print(foo)
    print(bar)
    # magic_process_tuple(7, 8, 21)
    magic_process_tuple(*foo)


def magic_process_tuple(*foo):
    print(foo)


magic(5, 7, 8, 21, x=1, y=4, z=7)
