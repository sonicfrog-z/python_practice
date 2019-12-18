class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return '{}: ${}'.format(
            self.owner, self.balance
        )

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class HighBalanceAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < 500:
            super().withdraw(100)


if __name__ == '__main__':
    b = BankAccount('John Smith', 1000)
    print(b)  # John Smith: $1000
    b.deposit(600)
    print(b)  # John Smith: $1600
    b.withdraw(1200)
    print(b)  # John Smith: $400

    h = HighBalanceAccount('Jack Jone', 1000)
    print(h)  # Jack Jones: $1000
    h.deposit(600)
    print(h)  # Jack Jones: $1600
    h.withdraw(1200)
    # If the balance of h is less than 500
    # charge extra penalty of 100
    print(h)  # Jack Jones: $300
