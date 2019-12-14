numbers = [0, 8, 9, 4, 1, 3]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)

text = 'A tiresome tree overlooks a straight biography. A fashion teaches a huge color outside the champagne.'
length_threshold = 10
long_words = list(
    filter(
        lambda word: len(word) >= length_threshold,
        text.split()
    )
)
print(long_words)

numbers = [5, 30, 20, 12, 9, 8, 19, 4]
excludes = [9, 12, 8, 4, 17, 32]

result = list(
    filter(
        lambda number: number not in excludes, numbers
    )
)
print(result)

numbers = [0, 8, 9, 4, 1, 3]

squared_even_numbers = list(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers)
    )
)
print(squared_even_numbers)