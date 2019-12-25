class NameDescriptor:
    def __get__(self, instance, owner):
        print('__get__ is called')
        return instance._name

    def __set__(self, instance, value):
        print('__set__ is called')
        instance._name = value


class Person:
    def __init__(self, name):
        self._name = name

    name = NameDescriptor()


if __name__ == '__main__':
    john = Person('John')
    print(john.name)
    john.name = 'Johnny'
    print(john.name)
