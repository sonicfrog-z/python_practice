def letter_count(word):
    result = {}

    for letter in word:
        result.setdefault(letter, 0)
        result[letter] += 1

    return result


# count_dict =
# {'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2,
# 'o': 9, 'l': 3, 't': 1, 'r': 2, 'a': 2,
# 'i': 6, 'c': 6, 's': 4, 'v': 1}
def reverse_count(count_dict):
    result = {}

    for letter, freq in count_dict.items():
        result.setdefault(freq, [])
        result[freq].append(letter)

    return result


word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
d = letter_count(word)
print(d)
r = reverse_count(d)
print(r)

# r = {2: ['p', 'u', 'm', 'r', 'a'], 4: ['n', 's'],
# 1: ['e', 't', 'v'], 9: ['o'], 3: ['l'], 6: ['i', 'c']}
most_freq = r[max(r.keys())]
least_freq = r[min(r.keys())]
print(most_freq)
print(least_freq)
