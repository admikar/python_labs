# import random
#
# def generate_random_number():
#     print(random.randint(-200, 0))
#
#
# generate_random_number()
# generate_random_number()
# generate_random_number()
# generate_random_number()
# generate_random_number()
import random


def print_random(a, b, c):
    full = [a, b, c]
    result = random.choice(full)
    print(result)



print_random(1,2,3)
print_random(3,4,5)
print_random(6,7,8)