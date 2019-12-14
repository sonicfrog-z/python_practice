# def letter_count(word):
#     result = {}
#
#     for letter in word:
#         if letter in result:
#             result[letter] += 1
#         else:
#             result[letter] = 1
#
#     return result


def letter_count(word):
    result = {}

    for letter in word:
        result.setdefault(letter, 0)
        result[letter] += 1

    return result


word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
d = letter_count(word)
print(d)
