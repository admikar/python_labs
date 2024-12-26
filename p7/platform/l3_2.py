# # Лига Плюща
#
# # Напишите программу, которая создает словарь с информацией о студенте (например, имя, возраст, университет).
# # Программа должна:
# # Проверить наличие значения "MIT" с использованием метода values().
# # Проверить наличие значения "Harvard" с использованием функции set().
# # Проверить наличие значения 22 с использованием генератора.
#
# # Напишите тут ваш код
# student_info = {
#     "Name": "To Kill a Mockingbird",
#     "year": 22,
#     "University": "MIT"
# }
#
# print("MIT" in student_info.values())
# values_set = set(student_info.values())
# if "Harvard" in values_set:
#     print("Значение 'Harvard' найден")
# else:
#     print("Значение 'Harvard' ненайден")
#
# value_to_find = 22
#
# # Используем генератор для проверки наличия значения
# if any(value == value_to_find for value in student_info.values()):
#     print(f"Значение {value_to_find} присутствует в словаре.")
# else:
#     print(f"Значение {value_to_find} отсутствует в словаре.")

# Создание словаря с информацией о студенте
student_info = {
    "name": "John Doe",
    "age": 22,
    "university": "MIT"
}

# Проверка наличия значения "MIT" с использованием метода values()
contains_mit = "MIT" in student_info.values()
print(f"Contains MIT: {contains_mit}")

# Проверка наличия значения "Harvard" с использованием функции set()
contains_harvard = "Harvard" in set(student_info.values())
print(f"Contains Harvard: {contains_harvard}")

# Проверка наличия значения 22 с использованием генератора
contains_22 = any(value == 22 for value in student_info.values())
print(f"Contains 22: {contains_22}")

