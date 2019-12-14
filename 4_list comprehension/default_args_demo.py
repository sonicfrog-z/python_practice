# def calculate(a, b, c=2):
#     return a + b**2 + c**3
#
#
# print(calculate(1, 2, 3))
# print(calculate(4, 5))


def add_to(val, arr):
    arr.append(val)
    return arr


arr = []
print(add_to(3, arr))
print(add_to(4, arr))


def add_to2(val, arr=[]):
    arr.append(val)
    return arr


print(add_to2(3))
print(add_to2(4))

print(add_to2(3, []))
print(add_to2(4, []))


def add_to3(key_, val_, d={}):
    d[key_] = val_
    return d


print(add_to3('a', 1))
print(add_to3('b', 2))


def add_to4(val, arr=None):
    if arr is None:
        arr = []
    arr.append(val)
    return arr


print(add_to4(3))
print(add_to4(4))
print(add_to4(5, [3]))
print(add_to4(6))
