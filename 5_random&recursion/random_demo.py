import random

colors = ['red', 'blue', 'pink', 'yellow', 'green', "purple"]

for _ in range(10):
    # print(random.randint(1, 6))
    # print(random.random())
    print(random.choice(colors))

numbers = [i for i in range(1, 51)]
print(numbers)
random.shuffle(numbers)
print(numbers)
