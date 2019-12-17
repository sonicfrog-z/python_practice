import math


class Rational:
    def __init__(self, n, d):
        gcd = math.gcd(n, d)
        n //= gcd
        d //= gcd
        self.numer = n
        self.denom = d

    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom + self.denom * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
        else:
            return NotImplemented


r1 = Rational(3, 4)
r2 = Rational(20, 50)
print(r1)  # 3/4
print(r2)  # 2/5

r3 = r1 + r2  # => r1.+(r2) => r1.__add__(r2)
print(r3)  # 23/20
r4 = r1 * r2
print(r4)  # 6/20, 3/10 even better

r5 = r1 + r1
print(r5)
