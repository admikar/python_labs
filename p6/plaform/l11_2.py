# user_input = input("Введите строку: ")
#
# parts = user_input.split(',')
# print(parts)
#
# joined_text = ' '.join(parts)
# print(joined_text)
#
#
input_str = input("Введите строку из нескольких слов, разделенных запятыми: ")

# Разделение строки на список слов
words_list = input_str.split(',')

# Вывод списка слов
print("Список слов:", words_list)

# Объединение списка слов в одну строку с пробелами
joined_str = ' '.join(words_list)

# Вывод объединенной строки
print("Объединенная строка:", joined_str)
