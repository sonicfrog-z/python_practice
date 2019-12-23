from collections.abc import Iterable, Iterator

colors = ['red', 'yellow', 'green', 'blue', 'black']

# for color in colors:
#     print(color)

# print(isinstance(colors, Iterable))
# color_iterator = iter(colors)
# print(isinstance(color_iterator, Iterator))
#
# print(next(color_iterator))
# print(next(color_iterator))
# print(next(color_iterator))
# print(next(color_iterator))
# print(next(color_iterator))
# # raise StopIteration
# print(next(color_iterator))

color_iterator = iter(colors)
while True:
    try:
        curr = next(color_iterator)
        print(curr)
    except StopIteration:
        break
