memo = {1: 0, 2: 1}


def fib(n):
    if n <= 0:
        return -1
    elif n in memo:
        return memo[n]
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result


print(fib(2000))
