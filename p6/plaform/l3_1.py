# from random import randrange
#
# mm = {randrange(1,101) for _ in range(10)}
#
# n_mm = set(filter(lambda x: x % 2 == 0, mm))
#
# print(n_mm)

import random

# Создание множества из 10 случайных чисел в диапазоне от 1 до 100
random_numbers = {random.randint(1, 100) for _ in range(10)}

# Получение подмножества всех четных чисел
even_numbers = {num for num in random_numbers if num % 2 == 0}

# Вывод подмножества четных чисел
print(even_numbers)