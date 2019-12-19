class InvalidAmountException(Exception):
    pass


class NotEnoughMoneyException(Exception):
    def __init__(self, balance):
        self.__user_balance = balance

    def _get_user_balance(self):
        return self.__user_balance

    user_balance = property(fget=_get_user_balance)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __str__(self):
        return '${}'.format(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise InvalidAmountException()

    def withdraw(self, amount):
        if self.__balance >= amount > 0:
            self.__balance -= amount
        elif amount > 0:
            raise NotEnoughMoneyException(self.__balance)
        else:
            raise InvalidAmountException()

    def _get_balance(self):
        return self.__balance

    balance = property(fget=_get_balance)


if __name__ == '__main__':
    def manage(acct_func, amount):
        try:
            acct_func(amount)
        except InvalidAmountException:
            print('Invalid amount')
        except NotEnoughMoneyException as ne:
            print('Not enough money with balance: {}'.format(ne.user_balance))

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

