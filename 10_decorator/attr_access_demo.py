class Square:
    sides = 4

    def __init__(self, length):
        self._length = length

    def __getattr__(self, item):
        if item == 'size':
            return self._length * self.sides
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        valid_keys = ['_length', 'name']
        if key in valid_keys:
            super().__setattr__(key, value)
        else:
            raise AttributeError('cannot set {}'.format(key))


if __name__ == '__main__':
    s = Square(10)
    s.name = 'John'
    print(s._length)
    print(s.size)
    print(s.name)
    super(Square, s).__setattr__('color', 'red')
    #s.color = 'red'
    print(s.color)
