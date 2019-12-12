def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def calculate(calc_func, a, b):
    return calc_func(a, b)


print(calculate(add, 3, 4))
print(calculate(subtract, 3, 4))
print(calculate(multiply, 3, 4))
