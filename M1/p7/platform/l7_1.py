# fset1 = frozenset([1, 2, 3, 4])
# fset2 = frozenset("hello")
#
# print(fset1.union(fset2))
#
# print(fset1.intersection(fset2))
#
# print(fset1.difference(fset2))
#
# print(fset1.symmetric_difference(fset2))
#
# Создаем frozenset из списка
list_frozen = frozenset([1, 2, 3, 4, 5])

# Создаем frozenset из строки
string_frozen = frozenset("abcde")

# Объединение
union_result = list_frozen | string_frozen

# Пересечение
intersection_result = list_frozen & string_frozen

# Разность
difference_result = list_frozen - string_frozen

# Симметрическая разность
symmetric_difference_result = list_frozen ^ string_frozen

# Вывод результатов
print(f"Объединение: {union_result}")
print(f"Пересечение: {intersection_result}")
print(f"Разность: {difference_result}")
print(f"Симметрическая разность: {symmetric_difference_result}")

