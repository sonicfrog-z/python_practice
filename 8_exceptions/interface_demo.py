from abc import ABC, abstractmethod


class Foo(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class Bar(Foo):
    def method1(self):
        pass

    def method2(self):
        print('method2')

if __name__ == '__main__':
    b = Bar()
