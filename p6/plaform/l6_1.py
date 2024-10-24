# from random import randint
#
# my_set = {randint(1, 50) for i in range(10)}
#
# for index, element in enumerate(my_set):
#     print(index, "", element)
#
import random

# Создаем множество из случайных чисел в диапазоне от 1 до 50
random_set = {random.randint(1, 50) for _ in range(10)}

# Вывод элементов множества вместе с их "индексами"
for index, value in enumerate(random_set):
    print(f"{index}: {value}")