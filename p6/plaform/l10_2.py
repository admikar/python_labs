# input_string = input("Введите строку: ")
#
# substring1 = input_string[-3:]
# substring2 = input_string[:-1]
# substring3 = input_string[::-1]
#
# print(substring1)
# print(substring2)
# print(substring3)

# Ввод строки от пользователя
s = input("Введите строку: ")

# Извлекает последние три символа строки
last_three = s[-3:]

# Извлекает строку, исключая последний символ
excluding_last = s[:-1]

# Переворачивает строку
reversed_s = s[::-1]

# Выводит все три результата
print(last_three)
print(excluding_last)
print(reversed_s)

