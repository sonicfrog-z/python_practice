class ReverseIterable:
    def __init__(self, itrbl):
        self._list = list(itrbl)
        self._curr_index = len(self._list)

    def __iter__(self):
        return self

    def __next__(self):
        self._curr_index -= 1
        if self._curr_index < 0:
            raise StopIteration
        else:
            return self._list[self._curr_index]


if __name__ == '__main__':
    reverse_list = ReverseIterable(
        [10, 3, 'abc', 'sda', 47, 100, 'hello', 9]
    )
    for item in reverse_list:
        print(item)

    print('=' * 40)

    reverse_msg = ReverseIterable('Hello world!')
    for letter in reverse_msg:
        print(letter)

    print('=' * 40)

    reverse_range = ReverseIterable(range(3, 18, 5))
    for number in reverse_range:
        print(number)

