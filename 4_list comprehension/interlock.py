from bisect import bisect_left
import time


def binary_search(word, words):
    index = bisect_left(words, word)
    return index != len(words) and words[index] == word


def get_interlock(fd):
    words = []
    for line in fd:
        words.append(line.strip())

    result = []

    for word in words:
        even_index_sub_word = word[::2]
        odd_index_sub_word = word[1::2]

        if binary_search(even_index_sub_word, words) and \
                binary_search(odd_index_sub_word, words):
            result.append(word)

    return result


with open('words.txt') as fin:
    start = time.time()
    result = get_interlock(fin)
    end = time.time()
    print(end - start)
    print(result)
