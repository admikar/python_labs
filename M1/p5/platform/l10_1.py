# tuple_len = list(input("Enter elements of tuple: "))
# if len(tuple_len) == 0:
#     print("Tuple empty")
# else:
#     print(tuple_len[-1])

# element = " "
# new_list= []
# while (len(element) > 0):
#     element = input("Enter elements of tuple: ")
#     #print(new_list)
#     if len(element) > 0:
#         new_list.append(element)
#     #print(new_list)
#
# new_tuple = tuple(new_list)
# #print(new_list)
# #print(new_tuple)
#
# if len(new_tuple) == 0:
#     print("Tuple empty")
# else:
#     print(new_tuple[-1])

elements = []
print("Введите элементы кортежа (для окончания ввода просто нажмите Enter):")
while True:
    element = input()
    if element == "":
        break
    elements.append(element)

tuple_elements = tuple(elements)

if tuple_elements:
    print(f"Последний элемент кортежа: {tuple_elements[-1]}")
else:
    print("Кортеж пустой")