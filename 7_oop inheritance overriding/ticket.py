import random


class Ticket:
    def __init__(self):
        self.number = random.randint(1000, 9999)

    def __str__(self):
        return '{}: ${}'.format(
            self.number, self.get_price()
        )

    def get_price(self):
        return NotImplemented


class MovieTicket(Ticket):
    def __init__(self, adays):
        super().__init__()
        self.days_in_advance = adays

    def get_price(self):
        return 30 if self.days_in_advance >= 10 else 40


class StudentTicket(MovieTicket):
    def __str__(self):
        return '{}\n(Student ID required)'.format(
            super().__str__()
        )

    def get_price(self):
        return super().get_price() // 2


if __name__ == '__main__':
    mt = MovieTicket(12)
    print(mt)

    st = StudentTicket(4)
    print(st)
