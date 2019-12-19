import random


class RandomWordGenerator:
    def __init__(self, filename, min_len, max_len):
        self._word_list = []

        with open(filename) as fin:
            for word in fin:
                word = word.strip().lower()
                if min_len <= len(word) <= max_len:
                    self._word_list.append(word)

    def _get_random_word(self):
        return random.choice(self._word_list)

    random_word = property(fget=_get_random_word)


if __name__ == '__main__':
    word_gen = RandomWordGenerator('words5000.txt', 5, 8)
    for i in range(10):
        print(word_gen.random_word)
