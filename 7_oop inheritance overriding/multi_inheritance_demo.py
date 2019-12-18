class Animal:
    number_of_animals = 0

    def __init__(self, name):
        self.name = name
        Animal.number_of_animals += 1


class Dog(Animal):
    def __init__(self, name, breed, age):
        Animal.__init__(self, name)
        self.breed = breed
        self.age = age

    def get_age(self):
        return self.age


class Domestic(Animal):
    def __init__(self, name, address):
        Animal.__init__(self, name)
        self.address = address

    def get_address(self):
        return self.address


class HomePuppy(Domestic, Dog):
    def __init__(self, name, breed, age, address):
        Dog.__init__(self, name, breed, age)
        Domestic.__init__(self, name, address)


if __name__ == '__main__':
    p = HomePuppy('Max', 'Chihuahua', 3, 'San Jose')
    print(p.name)
    print(p.age)
    print(p.address)
    q = HomePuppy('John', 'Bulldog', 10, 'LA')
    print(Animal.number_of_animals)

    print(HomePuppy.__mro__)
