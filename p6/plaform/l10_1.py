# string = input("Введите строку: ")
# new_string = string[3:9]
# another_string = string[5:]
#
# print(new_string)
# print(another_string)
# Принимаем строку от пользователя
input_string = input("Введите строку: ")

# Извлечение подстроки с 3-го по 8-й символ (индекс) включительно
substring1 = input_string[3:9]

# Извлечение подстроки с 5-го символа (индекса) до конца строки
substring2 = input_string[5:]

# Вывод обеих подстрок
print("Подстрока с 3-го по 8-й символ включительно:", substring1)
print("Подстрока с 5-го символа до конца строки:", substring2)
