# elements = []
# print("Введите элементы кортежа (для окончания ввода просто нажмите Enter):")
# while True:
#     element = input()
#     if element == "":
#         break
#     elements.append(element)
#
# tuple_elements = tuple(elements)
#
# print(tuple_elements[::-1])

elements = input("Введите элементы через пробел: ").split()
tuple_elements = tuple(elements)
reversed_tuple = tuple_elements[::-1]
print(reversed_tuple)
