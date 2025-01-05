# string = input("Введите строку: ")
# print(len(string))
# ind = int(input("Введите index: "))
# if ind in range(len(string)):
#     print(string[ind])
# else:
#     print("out of range")

string = input("Введите строку: ")
length = len(string)
print(f"Длина строки: {length}")


index = int(input("Введите индекс: "))
if index < 0 or index >= length:
    print("Индекс выходит за пределы строки")
else:
    print(f"Символ по индексу {index}: {string[index]}")


