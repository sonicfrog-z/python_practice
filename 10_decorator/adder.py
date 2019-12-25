class Adder:
    def __init__(self, base):
        self._base = base

    def __call__(self, value):
        return self._base + value


if __name__ == '__main__':
    adder5 = Adder(5)
    print(adder5(10))
    print(adder5(3))
