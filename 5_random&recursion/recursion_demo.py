def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(20))


def fib(n):
    if n <= 0:
        return -1
    elif n == 1 or n == 2:
        return n-1
    else:
        return fib(n-1) + fib(n-2)


print(fib(20))


def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and palindrome(word[1:-1])


print(palindrome('abcdcba'))
print(palindrome('abcdbca'))


def abecedarian(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] <= word[1] and abecedarian(word[1:])


print(abecedarian('accept'))
print(abecedarian('brother'))
