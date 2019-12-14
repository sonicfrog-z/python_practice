import time


def get_interlock(fd):
    words = set()
    for line in fd:
        words.add(line.strip())

    result = []

    for word in words:
        even_index_sub_word = word[::2]
        odd_index_sub_word = word[1::2]

        if even_index_sub_word in words and odd_index_sub_word in words:
            result.append(word)

    return result


with open('words.txt') as fin:
    start = time.time()
    result = get_interlock(fin)
    end = time.time()
    print(end - start)
    print(result)
