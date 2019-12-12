def process(numbers, process_func):
    result = []

    for number in numbers:
        result.append(process_func(number))

    return result


arr = [1, 4, 3, 6, 5]
squares = process(arr, lambda a: a**2)
print(squares)  # [1, 16, 9, 36, 25]
t10 = process(arr, lambda b: b*10)
print(t10)
