# elements = list(input(f"Введите элемент {i+1}: ") for i in range(10))
#
# mn_elements = set(elements)
#
# print(mn_elements)

elements = []
for _ in range(10):
    element = input("Введите элемент: ")
    elements.append(element)

unique_elements = set(elements)
print(unique_elements)