# def sum_avg(*numbers):
#     sum_ = sum(numbers)
#     return sum_, sum_/len(numbers)
#
#
# s, a = sum_avg(7, 4, 9, 8, 12, 4, 3)
# print(s, a)
# s, a = sum_avg(7, 4, 9)
# print(s, a)
# s, a = sum_avg(7, 4, 9, 8, 12, 4, 3, 10, 2, 3)
# print(s, a)
#
#
# def max_min(*numbers):
#     return max(numbers), min(numbers)
#
#
# def average(*numbers):
#     mean = sum(numbers) / len(numbers)
#     mid = len(numbers) // 2
#     sorted_numbers = sorted(numbers)
#     if len(numbers) % 2 == 0:
#         median = (sorted_numbers[mid-1] + sorted_numbers[mid])/2
#     else:
#         median = sorted_numbers[mid]
#     return mean, median
#
#
# ma, mi = max_min(4, 8, 27, 1, 3, 0, 9)
# print(ma, mi)
# mean, median = average(8, 3, 5, 7, 1, 2, 3, 6)
# print(mean, median)


def foo(a, b, *rest):
    print(a)
    print(b)
    print(rest)


foo(1, 2, 4, 5, 3, 2, 1)
foo(1, 2)