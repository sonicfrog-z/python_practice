class Foo:
    def mystery(number):
        return number


class Bar(Foo):
    def mystery(number):
        return number ** 2


print(Foo.mystery(5))
print(Bar.mystery(10))
