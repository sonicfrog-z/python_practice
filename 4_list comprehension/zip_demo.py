names = ['Alice', 'Bob', 'Charles', 'David']
ages = [19, 18, 17, 19]
schools = ['Stanford', 'Bekerley', 'UCSC', 'San Jose State']

result = list(zip(names, ages, schools))
print(result)
result2 = dict(zip(names, zip(ages, schools)))
print(result2)


def hamming_distance(word1, word2):
    distance = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            distance += 1
    return distance


print(hamming_distance('karolin', 'kathrin'))
