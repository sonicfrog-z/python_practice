from point import Point


class Circle:
    def __init__(self, x, y, r):
        self.center = Point(x, y)
        self.radius = r

    def __str__(self):
        return 'center at {} with radius {}'.format(
            self.center, self.radius
        )

    def cover(self, pt):
        return self.center.distance(pt) <= self.radius


if __name__ == '__main__':
    c = Circle(3, 4, 6)
    print(c)  # center at (3, 4) with radius 6
    c2 = Circle(3, 4, 2)
    p1 = Point(4, 3)
    p2 = Point(6, 6)
    print(c2.cover(p1))
    print(c2.cover(p2))
