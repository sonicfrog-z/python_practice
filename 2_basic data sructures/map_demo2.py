def process(numbers, process_func):
    result = []

    for number in numbers:
        result.append(process_func(number))

    return result


def square(number):
    return number ** 2


def times10(number):
    return number * 10


arr = [1, 4, 3, 6, 5]
squares = process(arr, square)
print(squares)  # [1, 16, 9, 36, 25]
t10 = process(arr, times10)
print(t10)
