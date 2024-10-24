# elements = []
# for _ in range(5):
#     element = input("Введите элемент: ")
#     elements.append(element)
#
# tuple_elements = tuple(elements)
#
# new_el = input("Введите ещё один элемент: ")
# new_tuple_elements = list(tuple_elements)
# new_tuple_elements.append(new_el)
# new_new_tuple_elements = tuple(new_tuple_elements)
# print(new_new_tuple_elements)

# Создаем кортеж из 5 элементов, запрашиваемых у пользователя
elements = tuple(input(f"Введите элемент {i+1}: ") for i in range(5))

# Запрашиваем у пользователя новый элемент
new_element = input("Введите новый элемент для добавления в конец кортежа: ")

# Создаем новый кортеж, добавляя новый элемент к существующему кортежу
updated_tuple = elements + (new_element,)

# Выводим обновленный кортеж
print("Обновленный кортеж:", updated_tuple)
