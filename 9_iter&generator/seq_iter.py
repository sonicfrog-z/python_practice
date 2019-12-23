class SeqIter:
    def __init__(self, max_term):
        self._index = 0
        self._max = max_term

        self._denominator = 1
        self._sign = 1
        self._curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1

        if self._index > self._max:
            raise StopIteration

        self._curr += self._sign / self._denominator

        self._sign *= -1
        self._denominator += 2

        return 4 * self._curr


if __name__ == '__main__':
    for v in SeqIter(100):
        print(v)
