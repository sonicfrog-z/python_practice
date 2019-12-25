import time


def trace(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._wrapped_instance = cls(*args, **kwargs)

        def __getattr__(self, item):
            print('calling {} at {}'.format(
                item, time.strftime('%H:%M:%S')
            ))
            return getattr(self._wrapped_instance, item)

    return Wrapper


@trace
class Employee:
    def __init__(self, name, hours, rate):
        self._name = name
        self._hours = hours
        self._rate = rate

    def pay(self):
        return self._hours * self._rate

    def update_rate(self, rate):
        self._rate = rate


if __name__ == '__main__':
    john = Employee('John', 8, 20)
    print(john.pay())
    john.update_rate(40)
    print(john.pay())
