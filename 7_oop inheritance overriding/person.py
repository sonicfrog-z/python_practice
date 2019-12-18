class Person:
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = age

    def __str__(self):
        return 'I am {} and I am {} years old.'.format(
            self.name, self.age
        )

    def happy_birthday(self):
        self.age += 1


class Student(Person):
    def __init__(self, name, age, school):
        # Does not work for multi-inheritance
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.school = school

    def __str__(self):
        return 'I am {} and I am from {}'.format(
            self.name, self.school
        )

    def graduate(self):
        self.name = 'Dr. {}'.format(self.name)


if __name__ == '__main__':
    john = Person('John Smith', 18)
    print(str(john))
    john.happy_birthday()
    print(john)

    jack = Student('Jack Jones', 25, 'Stanford')
    print(jack)
    jack.happy_birthday()
    print(jack)
    jack.graduate()
    print(jack)
