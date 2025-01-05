# elements = tuple(input(f"Введите элемент {i+1}: ") for i in range(7))
#
# print(elements[-3])
# print(elements[-2])

elements = []
for _ in range(7):
    element = input("Введите элемент: ")
    elements.append(element)

tuple_elements = tuple(elements)

print("Третий с конца элемент:", tuple_elements[-3])
print("Предпоследний элемент:", tuple_elements[-2])