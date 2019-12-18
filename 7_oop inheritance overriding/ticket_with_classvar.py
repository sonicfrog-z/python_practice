class Ticket:
    next_ticket_number = 1

    def __init__(self):
        self.number = Ticket.next_ticket_number
        Ticket.next_ticket_number += 1

    def __str__(self):
        return '{}: ${}'.format(
            self.number, self.get_price()
        )

    def get_price(self):
        return NotImplemented


class MovieTicket(Ticket):
    minimum_days_in_advance = 10
    early_bird_price = 30
    full_price = 40

    def __init__(self, adays):
        super().__init__()
        self.days_in_advance = adays

    def get_price(self):
        return MovieTicket.early_bird_price\
            if self.days_in_advance >= MovieTicket.minimum_days_in_advance\
            else MovieTicket.full_price


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
