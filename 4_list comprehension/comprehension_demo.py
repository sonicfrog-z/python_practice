numbers = [1, 4, 2, 3, 5]

square_numbers = [number**2 for number in numbers]
print(square_numbers)

even_square_numbers = [number**2 for number in numbers if number % 2 == 0]
print(even_square_numbers)

even_square_numbers2 = [
    number**2 if number % 2 == 0 else -1 for number in numbers
]
print(even_square_numbers2)


names = ['Alice', 'bOB', 'david', 'eRIC', 'BOB', 'Eric']
formatted_names = {name.title() for name in names}
print(formatted_names)

letter_frq = {'a': 10, 'b': 34, 'A': 2, 'Z': 3}
merged_frq = {
    letter.lower(): letter_frq.get(letter.lower(), 0) +
                    letter_frq.get(letter.upper(), 0)
    for letter in letter_frq.keys()
}
print(merged_frq)
