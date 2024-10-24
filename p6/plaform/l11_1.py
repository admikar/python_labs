# # strn = "Hello"
# # print(strn)
# # strn = strn.lower()
# # print(strn)
#
# s = input("Введите строку: ")
#
# s1 = s.strip()
# s2 = s.lower()
# s3 = s.upper()
#
# print(s1)
# print(s2)
# print(s3)

# Вводим строку от пользователя
user_input = input("Введите строку: ")

# Удаляем пробелы в начале и конце строки
stripped_string = user_input.strip()
print("Строка без пробелов в начале и в конце:", stripped_string)

# Преобразуем все символы строки в нижний регистр
lower_string = stripped_string.lower()
print("Строка в нижнем регистре:", lower_string)

# Преобразуем все символы строки в верхний регистр
upper_string = stripped_string.upper()
print("Строка в верхнем регистре:", upper_string)

