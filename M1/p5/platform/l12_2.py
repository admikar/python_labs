# elements = tuple(input(f"Input elements {i+1}: ") for i in range(6))
#
# n1_tuple = elements[0:2]
# n2_tuple = elements[2:4]
# n3_tuple = elements[4:6]
#
# print(n1_tuple)
# print(n2_tuple)
# print(n3_tuple)
#
# elements = n1_tuple + n3_tuple
# print(elements)

# Запрашиваем у пользователя 6 элементов и создаем кортеж
elements = tuple(input("Введите элемент {}: ".format(i + 1)) for i in range(6))

# Группируем элементы в 3 кортежа по 2 элемента
tuple1 = elements[:2]
tuple2 = elements[2:4]
tuple3 = elements[4:]

# Объединяем 1 и 3 кортежи
combined_tuple = tuple1 + tuple3

# Выводим обновленный кортеж на экран
print("Обновленный кортеж:", combined_tuple)