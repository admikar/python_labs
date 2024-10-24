# from random import randrange
#
# fl = [randrange(0, 100) for _ in range(10)]
# sl = [randrange(50, 126) for _ in range(10)]
#
# fl_m = set(fl)
# sl_m = set(sl)
#
# commom_m = fl_m | sl_m
#
# print(len(commom_m))

import random

# Генерация списков случайных элементов
list1 = [random.randint(0, 99) for _ in range(100)]
list2 = [random.randint(50, 125) for _ in range(100)]

# Преобразование списков во множества
set1 = set(list1)
set2 = set(list2)

# Объединение множеств
combined_set = set1.union(set2)

# Вывод количества элементов полученного множества
print(len(combined_set))