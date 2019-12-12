cubes = [5, 13, 4, 6]
squares = [11, 2, 6, 7]
units = [9, 8, 4, 5]

# result = [
#     5**3 + 11**2 + 9,
#     13**3 + 2**2 + 8,
#     ...
# ]

result = list(map(lambda c, s, u: c**3 + s**2 + u, cubes, squares, units))

print(result)
