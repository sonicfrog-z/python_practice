def square(numbers):
    result = []

    for number in numbers:
        result.append(number**2)

    return result


def times10(numbers):
    result = []

    for number in numbers:
        result.append(number * 10)

    return result


arr = [1, 4, 3, 6, 5]
squares = square(arr)
print(squares)  # [1, 16, 9, 36, 25]
t10 = times10(arr)
print(t10)
