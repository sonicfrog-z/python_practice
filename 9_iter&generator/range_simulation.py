# first step: a dummy iterable + iterator
# class NumberStepIterator:
#     # make NumberStepIterator iterator
#     def __next__(self):
#         return 0
#
#
# class NumberStep:
#     def __init__(self, start, end, step):
#         pass
#
#     # make NumberStep iterable
#     def __iter__(self):
#         return NumberStepIterator()

# for i in range(3, 18, 5):
#     print(i)


# second step: have iterable and iterator as separate classes
# class NumberStepIterator:
#     def __init__(self, start, end, step):
#         self._current = start - step
#         self._end = end
#         self._step = step
#
#     # make NumberStepIterator iterator
#     def __next__(self):
#         self._current += self._step
#
#         if self._current >= self._end:
#             raise StopIteration
#         else:
#             return self._current
#
#
# class NumberStep:
#     def __init__(self, start, end, step):
#         self._start = start
#         self._end = end
#         self._step = step
#
#     # make NumberStep iterable
#     def __iter__(self):
#         return NumberStepIterator(
#             self._start,
#             self._end,
#             self._step
#         )


class NumberStep:
    def __init__(self, start, end, step):
        self._current = start - step
        self._end = end
        self._step = step

    # make NumberStep iterable
    def __iter__(self):
        return self

    # make NumberStepIterator iterator
    def __next__(self):
        self._current += self._step

        if self._current >= self._end:
            raise StopIteration
        else:
            return self._current


for i in NumberStep(3, 18, 5):
    print(i)
