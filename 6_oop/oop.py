import math


class Point:
    # magic methods:
    # a method will be automatically triggered
    # in certain situation
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    # for any instance method
    # the first parameter is the instance caller
    def move(self, x, y):
        self.__init__(x, y)

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)


# Two steps:
# 1. create a blank Point instance pt
# 2. pt.__init__(10, 5)
pt = Point(10, 5)
print(pt.distance())
pt.move(3, 4)  # => Point.move(pt, 3, 4)
print(pt)  # => print(str(pt))
print(pt.distance())  # => print(Point.distance(pt))

pt2 = Point()
print(pt2)

pt3 = Point(3, 4)
print(pt3)
print(pt is pt3)
print(pt == pt3)  # => pt.==(pt3) => pt.__eq__(pt3)
pt4 = pt
print(pt4)
print(pt is pt4)
print(pt == pt4)


class Car:
    pass


c = Car()
c.x = 3
c.y = 4
print(pt == c)
