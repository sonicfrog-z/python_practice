class CurrencyUnit:
    conversion = 1.0

    def __get__(self, instance, owner):
        return instance._usd * self.conversion

    def __set__(self, instance, value):
        instance._usd = value / self.conversion


class Usd(CurrencyUnit):
    pass


class Euro(CurrencyUnit):
    conversion = 0.88


class Pound(CurrencyUnit):
    conversion = 0.78


class Rupee(CurrencyUnit):
    conversion = 71.61


class Currency:
    usd = Usd()
    euro = Euro()
    pound = Pound()
    rupee = Rupee()

    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        if usd:
            self.usd = usd
        elif euro:
            self.euro = euro
        elif pound:
            self.pound = pound
        elif rupee:
            self.rupee = rupee
        else:
            raise TypeError()

    def __str__(self):
        return '{} usd = {} euro = {} pound = {} rupee'.format(
            self.usd, self.euro, self.pound, self.rupee
        )


if __name__ == '__main__':
    currency = Currency(usd=1000)
    print(currency)  # 1000 usd = ... euro = ... pound = ... rupee
    currency.pound = 1000
    print(currency)  # ... usd = ... euro = 1000 pound = ... rupee
