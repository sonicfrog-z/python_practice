class Person:
    _minimum_age = 16

    def __init__(self, name, age, ssn):
        self._name = name
        self._age = Person._minimum_age
        self.age = age
        self.__ssn = ssn

    def __str__(self):
        return '{} is {} years old with SSN: {}'.format(
            self._name,
            self._age,
            self.ssn
        )

    def _get_age(self):
        return self._age

    def _set_age(self, age):
        if age > self._age:
            self._age = age

    def _get_ssn(self):
        return '***-**-{}'.format(self.__ssn[-4:])

    def _del_ssn(self):
        print('ssn will be deleted.')
        del self.__ssn

    age = property(fget=_get_age, fset=_set_age)
    ssn = property(fget=_get_ssn, fdel=_del_ssn)


if __name__ == '__main__':
    john = Person('John', 18, '123456789')
    print(john)
    john.age = 19
    print(john)
    john.age = -50
    print(john)
    print(john.ssn)

    jack = Person('Jack', -50, '111223333')
    print(jack)
    print(jack.age)
    del jack.ssn
    print(jack)

