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
    minimum_balance = 500
    penalty = 100

    def __str__(self):
        return '{}\nAccount Policy\nMinimum balance {} with penalty {}'.format(
            super().__str__(),
            HighBalanceAccount.minimum_balance,
            HighBalanceAccount.penalty
        )

    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < HighBalanceAccount.minimum_balance:
            super().withdraw(HighBalanceAccount.penalty)

    def adjust_penalty(penalty):
        HighBalanceAccount.penalty = penalty


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
    HighBalanceAccount.adjust_penalty(30)
    h.withdraw(100)
    print(h)

