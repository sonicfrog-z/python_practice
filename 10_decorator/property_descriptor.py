class DescriptorProperty:
    def __init__(self, getter, setter):
        self._getter = getter
        self._setter = setter

    def __get__(self, instance, owner):
        if self._getter:
            return self._getter(instance)
        else:
            raise AttributeError('cannot get')

    def __set__(self, instance, value):
        if self._setter:
            self._setter(instance, value)
        else:
            raise AttributeError('cannot set')


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    def _get_age(self):
        return self._age

    def _set_age(self, age):
        self._age = age

    # name = property(fget=_get_name, fset=_set_name)
    # age = property(fget=_get_age, fset=_set_age)

    name = DescriptorProperty(getter=_get_name, setter=_set_name)
    age = DescriptorProperty(getter=_get_age, setter=_set_age)


if __name__ == '__main__':
    john = Person('John', 16)
    print(john.name)
    print(john.age)
    john.name = 'Johnny'
    john.age = 19
    print(john.name)
    print(john.age)
