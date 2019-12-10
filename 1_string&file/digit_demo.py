def is_self_divisor(number):
    for digit_str in str(number):
        digit = int(digit_str)
        if digit == 0 or number % digit != 0:
            return False

    return True


print(is_self_divisor(128))
print(is_self_divisor(26))
print(is_self_divisor(101))

for i in range(2000):
    if is_self_divisor(i):
        print(i)
