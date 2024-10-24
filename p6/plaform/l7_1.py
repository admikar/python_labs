# inputs = input("Enter elements: ").split()
# mn_1 = set(inputs)
#
# inputs = input("Enter elements: ").split()
# mn_2 = set(inputs)
#
# #print(mn_1)
# #print(mn_2)
#
# mn_3 = mn_1.union(mn_2)
# mn_4 = mn_1.intersection(mn_2)
#
# print(mn_3)
# print(mn_4)

# Запрашиваем у пользователя элементы для первого множества
set1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))

# Запрашиваем у пользователя элементы для второго множества
set2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))

# Объединение множеств
union_set = set1.union(set2)
print("Объединение множеств:", union_set)

# Пересечение множеств
intersection_set = set1.intersection(set2)
print("Пересечение множеств:", intersection_set)