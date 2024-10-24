# import random
#
# # Создаем множество из случайных чисел в диапазоне от 1 до 50
# random_set_1 = {random.randint(1, 20) for _ in range(10)}
# print(random_set_1)
# random_set_2 = {random.randint(10, 30) for _ in range(10)}
# print(random_set_2)
# nm_1 = random_set_1.difference(random_set_2)
#
# nm_2 = random_set_1.symmetric_difference(random_set_2)
#
# print(nm_1)
# print(nm_2)

import random

# Создаем два множества из случайных чисел
set1 = set(random.randint(1, 20) for _ in range(10))
set2 = set(random.randint(10, 30) for _ in range(10))

# Находим разность первого множества со вторым
difference = set1.difference(set2)

# Находим симметрическую разность
symmetric_difference = set1.symmetric_difference(set2)

# Выводим результаты
print("Первое множество:", set1)
print("Второе множество:", set2)
print("Разность первого множества со вторым:", difference)
print("Симметрическая разность:", symmetric_difference)






