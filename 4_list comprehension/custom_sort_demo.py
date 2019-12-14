# fruits = ['grape', 'apple', 'banana', 'kiwi', 'papaya', 'strawberry']
#
# print(sorted(fruits))
#
# tuples = [(1, 2), (0, 3, 4), (2,)]
# print(sorted(tuples))
#
# fruits2 = [(5, 'grape'), (5, 'apple'), (6, 'banana'),
#           (4, 'kiwi'), (6, 'papaya'), (10, 'strawberry')]
# print(sorted(fruits2))
#
#
# def sort_by_length(words):
#     words_with_length = list(map(lambda word: (len(word), word), words))
#     sorted_words_with_length = sorted(words_with_length)
#     return list(map(lambda t: t[-1], sorted_words_with_length))
#
#
# def sort_by_last_letter(words):
#     words_with_last_letter = list(map(lambda word: (word[-1], word), words))
#     sorted_words_with_last_letter = sorted(words_with_last_letter)
#     return list(map(lambda t: t[-1], sorted_words_with_last_letter))
#
#
# print(sort_by_length(fruits))
# print(sort_by_last_letter(fruits))
#
#
# def sort_by(sort_func, words):
#     words_with_sorting_criteria = list(
#         map(
#             lambda word: (sort_func(word), word),
#             words
#         )
#     )
#     sorted_words_with_criteria = sorted(words_with_sorting_criteria)
#     return list(map(lambda t: t[-1], sorted_words_with_criteria))
#
#
# print(sort_by(lambda word: len(word), fruits))
# print(sort_by(lambda word: word[-1], fruits))

fruits = ['grape', 'apple', 'banana', 'kiwi', 'papaya', 'strawberry']

print(sorted(fruits, key=lambda word: (len(word), word), reverse=True))
