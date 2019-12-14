def sum_avg(numbers):
    sum_ = sum(numbers)
    return sum_, sum_/len(numbers)


def max_min(numbers):
    return max(numbers), min(numbers)


def average(numbers):


s, a = sum_avg([7, 4, 9, 8, 12, 4, 3])
print(s, a)
ma, mi = max_min([4, 8, 27, 1, 3, 0, 9])
print(ma, mi)
mean, median = average([8, 3, 5, 7, 1, 2, 3, 6])
print(mean, median)