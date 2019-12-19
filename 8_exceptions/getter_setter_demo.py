class Person:
    _minimum_age = 16

    def __init__(self, name, age, ssn):
        self._name = name
        self._age = Person._minimum_age
        self.set_age(age)
        self.__ssn = ssn

    def __str__(self):
        return '{} is {} years old with SSN: {}'.format(
            self._name,
            self._age,
            self.get_ssn()
        )

    def set_age(self, age):
        if age > self._age:
            self._age = age

    def get_ssn(self):
        return '***-**-{}'.format(self.__ssn[-4:])


if __name__ == '__main__':
    john = Person('John', 18, '123456789')
    print(john)
    john.set_age(19)
    print(john)
    john.set_age(-50)
    print(john)
    print(john.get_ssn())

    jack = Person('Jack', -50, '111223333')
    print(jack)

