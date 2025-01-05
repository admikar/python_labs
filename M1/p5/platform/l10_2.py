# # elements = []
# # print(type(elements))
# # print("Введите элементы кортежа (для окончания ввода просто нажмите Enter):")
# # while True:
# #     element = input()
# #     if element == "":
# #         break
# #     elements.append(element)
# #
# # print(type(elements))
# # print(elements)
# # ## ---
#
# elements = []
# print("Введите 5 элементов кортежа:")
# for _ in range(5):
#     element = input()
#     elements.append(element)
#
# tuple_elements = tuple(elements)
#
# print("Введите индекс:")
# index = int(input())
# if index > len(tuple_elements)-1:
#     print("Index out of tuple")
# else:
#     print(tuple_elements[index])
#

# Запрашиваем 5 элементов у пользователя и создаем кортеж
elements = tuple(input(f"Введите элемент {i+1}: ") for i in range(5))

# Запрашиваем индекс элемента
index = int(input("Введите индекс элемента: "))

# Проверяем, находится ли индекс в пределах кортежа и выводим соответствующее сообщение
if 0 <= index < len(elements):
    print(f"Элемент с индексом {index}: {elements[index]}")
else:
    print("Индекс выходит за пределы кортежа")