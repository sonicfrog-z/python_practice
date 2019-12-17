import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def distance(self, pt):
        diff_x = self.x - pt.x
        diff_y = self.y - pt.y
        return math.sqrt(
            diff_x ** 2 + diff_y ** 2
        )


if __name__ == '__main__':
    p = Point(3, 4)
    print(p)
    p2 = Point(0, 5)
    print(p2)