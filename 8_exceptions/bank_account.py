class BankAccount:
    ERROR_CODE_INVALID_AMOUNT = 1
    ERROR_CODE_NOT_ENOUGH_MONEY = 2

    def __init__(self, balance):
        self.__balance = balance

    def __str__(self):
        return '${}'.format(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            return BankAccount.ERROR_CODE_INVALID_AMOUNT

    def withdraw(self, amount):
        if self.__balance >= amount > 0:
            self.__balance -= amount
        elif amount > 0:
            return BankAccount.ERROR_CODE_NOT_ENOUGH_MONEY
        else:
            return BankAccount.ERROR_CODE_INVALID_AMOUNT

    def _get_balance(self):
        return self.__balance

    balance = property(fget=_get_balance)


if __name__ == '__main__':
    def manage(acct_func, amount):
        code = acct_func(amount)
        if code == BankAccount.ERROR_CODE_INVALID_AMOUNT:
            print('Invalid amount')
        elif code == BankAccount.ERROR_CODE_NOT_ENOUGH_MONEY:
            print('Not enough money')

    acct = BankAccount(1000)
    print(acct.balance)
    manage(acct.deposit, 300)
    print(acct)
    manage(acct.withdraw, 1500)
    print(acct)
    manage(acct.deposit, -2000)
    print(acct)
    manage(acct.withdraw, -600)
    print(acct)

