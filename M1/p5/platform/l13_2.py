# nested_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# max_value = 0
# for inner_tuple in nested_tuples:
#     for num in inner_tuple:
#         if num > max_value:
#             max_value = num
#
# print(max_value)

# Создаем кортеж с вложенными кортежами
nested_tuples = ((1, 3, 5), (6, 3, 8), (2, 4, 0), (7, 9, -1))

# Инициализируем переменную для хранения максимального значения
max_value = float('-inf')
print(max_value)

# Проходим по каждому вложенному кортежу
for sub_tuple in nested_tuples:
    # Находим максимальное значение в текущем подкортеже и сравниваем с глобальным максимумом
    if max(sub_tuple) > max_value:
        max_value = max(sub_tuple)

print("Максимальное значение во вложенных кортежах:", max_value)
