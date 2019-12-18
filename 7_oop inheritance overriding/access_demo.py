class LoginRecord:
    def __init__(self, username, password, expiry):
        self.username = username
        self.__password = password  # "private"
        self._expiry = expiry  # "internal"


if __name__ == '__main__':
    john = LoginRecord('John', 'test123', 4)
    print(john.username)
    print(john._LoginRecord__password)  # do not do this
    print(john._expiry)  # do not do this