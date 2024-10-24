# user_string = input("Enter string: ")
# user_substring = input("Enter sub string: ")
#
# print(user_substring in user_string)
#
# print(user_string.find(user_substring))
#
# print(user_string.count(user_substring))
# Ввод строки и подстроки от пользователя
string = input("Введите строку: ")
substring = input("Введите подстроку: ")

# Проверка вхождения подстроки в строку с использованием оператора in
is_in = substring in string

# Нахождение первого вхождения подстроки с использованием метода find()
first_occurrence = string.find(substring)

# Подсчет количества вхождений подстроки с использованием метода count()
count_occurrences = string.count(substring)

# Вывод результатов
print(f"Подстрока входит в строку: {is_in}")
print(f"Первое вхождение подстроки в строку: {first_occurrence}")
print(f"Количество вхождений подстроки в строку: {count_occurrences}")

