def is_armstrong_number(number):
    sum_ = 0
    num_str = str(number)

    for digit_str in num_str:
        digit = int(digit_str)
        sum_ += digit ** len(num_str)

    return sum_ == number


for i in range(1, 10001):
    if is_armstrong_number(i):
        print(i)
