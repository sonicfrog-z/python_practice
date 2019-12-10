def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def is_abecedarian(word):
    word = word.lower()
    for index in range(len(word)-1):
        curr_letter = word[index]
        next_letter = word[index+1]
        if curr_letter > next_letter:
            return False

    return True


print(is_palindrome('Kayak'))
print(is_palindrome('hello'))

print(is_abecedarian('accepT'))
print(is_abecedarian('brother'))
