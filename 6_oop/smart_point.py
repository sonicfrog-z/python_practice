class SmartPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return SmartPoint(self.x + other.x, self.y + other.y)

    def __mul__(self, factor):
        return SmartPoint(self.x * factor, self.y * factor)

    def __rmul__(self, factor):
        return self.__mul__(factor)


sp1 = SmartPoint(3, 4)
sp2 = SmartPoint(5, 7)
print(sp1)
print(sp2)

sp3 = sp1 + sp2
print(sp3)  # (8, 11)
sp4 = sp3 * 10
print(sp4)
sp5 = 10 * sp4
print(sp5)
