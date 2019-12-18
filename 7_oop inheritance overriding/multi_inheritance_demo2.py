class Food:
    def __init__(self, rate, **kwargs):
        self.rate = rate


class Animal:
    number_of_animals = 0

    def __init__(self, name, **kwargs):
        # super().__init__(**kwargs)
        self.name = name
        Animal.number_of_animals += 1


class Dish(Animal, Food):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Dog(Animal):
    def __init__(self, breed, age, **kwargs):
        super().__init__(**kwargs)
        self.breed = breed
        self.age = age

    def get_age(self):
        return self.age

    def mystery(self):
        print('foo')


class Domestic(Animal):
    def __init__(self, address, **kwargs):
        super().__init__(**kwargs)
        self.address = address

    def get_address(self):
        return self.address

    def mystery(self):
        print('bar')


class HomePuppy(Domestic, Dog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    p = HomePuppy(name='Max', breed='Chihuahua', age=3, address='San Jose')
    print(p.name)
    print(p.age)
    print(p.address)
    q = HomePuppy(name='John', breed='Bulldog', age=10, address='LA')
    print(Animal.number_of_animals)

    print(HomePuppy.__mro__)
    p.mystery()

    f = Dish(name='chicken', rate=5)
    print(f.name)
    print(f.rate)