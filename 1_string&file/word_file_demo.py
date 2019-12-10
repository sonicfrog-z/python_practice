# step1: read words from words.txt and print all palindrome words
# step2: find the longest palindrome word


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


with open('words.txt') as fin:
    longest_palindrome_so_far = ''
    longest_abecedarian_so_far = ''
    for line in fin:
        word = line.strip()
        if is_palindrome(word) and len(word) >= len(longest_palindrome_so_far):
            longest_palindrome_so_far = word
        if is_abecedarian(word) and len(word) >= len(longest_abecedarian_so_far):
            longest_abecedarian_so_far = word
    print(longest_palindrome_so_far)
    print(longest_abecedarian_so_far)
